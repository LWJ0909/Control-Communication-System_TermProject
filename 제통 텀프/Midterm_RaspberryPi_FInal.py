import threading
import time
import socket
import select
import cv2
import numpy as np
from gpiozero import Button, DigitalOutputDevice, PWMOutputDevice, LED
from picamera2 import Picamera2

# -------------------- Camera Class --------------------

class MyPiCamera():
    def __init__(self, width, height):
        self.cap = Picamera2()
        self.width = width
        self.height = height
        self.is_open = True

        try:
            self.config = self.cap.create_video_configuration(main={"format": "RGB888", "size": (width, height)})
            self.cap.align_configuration(self.config)
            self.cap.configure(self.config)
            self.cap.start()
        except Exception as e:
            print("Camera init failed:", e)
            self.is_open = False

    def read(self):
        if self.is_open:
            return True, self.cap.capture_array()
        else:
            return False, np.zeros((self.height, self.width, 3), dtype=np.uint8)

    def release(self):
        if self.is_open:
            self.cap.close()
        self.is_open = False

# -------------------- GPIO Setup --------------------

SW1 = Button(5, pull_up=False)
SW2 = Button(6, pull_up=False)
SW3 = Button(13, pull_up=False)
SW4 = Button(19, pull_up=False)

PWMA = PWMOutputDevice(18)
AIN1 = DigitalOutputDevice(22)
AIN2 = DigitalOutputDevice(27)

PWMB = PWMOutputDevice(23)
BIN1 = DigitalOutputDevice(25)
BIN2 = DigitalOutputDevice(24)

led1 = LED(26)  # Front left
led2 = LED(16)  # Front right
led3 = LED(20)  # Rear left
led4 = LED(21)  # Rear right

# -------------------- LED Blinking Control --------------------

blinker_thread = None
blinker_running = False

def blink_leds(led_a, led_b):
    global blinker_running
    blinker_running = True
    while blinker_running:
        led_a.on(); led_b.on()
        time.sleep(0.3)
        led_a.off(); led_b.off()
        time.sleep(0.3)

def start_blinking(led_a, led_b):
    global blinker_thread, blinker_running
    stop_blinking()
    blinker_thread = threading.Thread(target=blink_leds, args=(led_a, led_b))
    blinker_thread.daemon = True
    blinker_thread.start()

def stop_blinking():
    global blinker_running, blinker_thread
    blinker_running = False
    if blinker_thread is not None:
        blinker_thread.join()
        blinker_thread = None

# -------------------- Motor Control --------------------

def motor_go(speed):
    stop_blinking()
    led1.on(); led2.on()
    led3.off(); led4.off()
    AIN1.off(); AIN2.on()
    PWMA.value = speed
    BIN1.off(); BIN2.on()
    PWMB.value = speed

def motor_back(speed):
    start_blinking(led3, led4)
    AIN1.on(); AIN2.off()
    PWMA.value = speed
    BIN1.on(); BIN2.off()
    PWMB.value = speed

def motor_left(speed):
    start_blinking(led1, led3)
    AIN1.on(); AIN2.off()
    PWMA.value = speed
    BIN1.off(); BIN2.on()
    PWMB.value = speed

def motor_right(speed):
    start_blinking(led2, led4)
    AIN1.off(); AIN2.on()
    PWMA.value = speed
    BIN1.on(); BIN2.off()
    PWMB.value = speed

def motor_stop():
    stop_blinking()
    led1.off(); led2.off(); led3.off(); led4.off()
    AIN1.off(); AIN2.off()
    PWMA.value = 0
    BIN1.off(); BIN2.off()
    PWMB.value = 0

# -------------------- TCP Listener with select --------------------

def tcp_listener_select():
    global current_action
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)
    print('Waiting for connection...')
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    conn.setblocking(False)

    try:
        while True:
            ready, _, _ = select.select([conn], [], [], 0.1)
            if ready:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode().strip()
                print(f"Received: {message}")

                if message == "front":
                    if current_action == "front":
                        motor_stop(); current_action = "stop"
                    else:
                        motor_go(1.0); current_action = "front"

                elif message == "back":
                    if current_action == "back":
                        motor_stop(); current_action = "stop"
                    else:
                        motor_back(0.5); current_action = "back"

                elif message == "left":
                    if current_action == "left":
                        motor_stop(); current_action = "stop"
                    else:
                        motor_left(0.5); current_action = "left"

                elif message == "right":
                    if current_action == "right":
                        motor_stop(); current_action = "stop"
                    else:
                        motor_right(0.5); current_action = "right"

                else:
                    print("Unknown command.")
                    motor_stop()
                    current_action = "stop"

            # 버튼 입력 확인
            if SW1.is_pressed or SW2.is_pressed or SW3.is_pressed or SW4.is_pressed:
                print("Button pressed! Stopping motors.")
                motor_stop()
                current_action = "stop"

    finally:
        motor_stop()
        conn.close()
        server_socket.close()

# -------------------- Main Camera Display --------------------

def camera_loop():
    camera = MyPiCamera(640, 480)
    while camera.is_open:
        ret, img = camera.read()
        img = cv2.flip(img, -1)
        cv2.imshow("My Camera", img)
        if cv2.waitKey(1) == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

# -------------------- Main --------------------

if __name__ == "__main__":
    current_action = "stop"
    tcp_thread = threading.Thread(target=tcp_listener_select, daemon=True)
    tcp_thread.start()
    camera_loop()

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:12:47 2025

@author: won01
"""

import serial
import socket
import sys
import time  # 추가

# UART 포트 오픈
try:
    ser = serial.Serial('COM7', 115200, timeout=1)
    print("Serial port COM7 opened successfully.")
except serial.SerialException as e:
    print(f"[Error] Could not open serial port COM7: {e}")
    sys.exit(1)

# TCP 소켓 연결 (서버 준비될 때까지 계속 시도)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        sock.connect(('192.168.137.49', 12345))  # 라즈베리파이 IP
        print("TCP socket connected successfully.")
        break  # 연결 성공하면 루프 탈출
    except socket.error as e:
        print("[Warning] TCP connection failed, retrying in 1 second...")
        time.sleep(1)  # 1초 기다리고 재시도

# 메인 통신 루프
try:
    while True:
        data = ser.readline()

        if data:
            print(f"UART received: {data}")
            sock.sendall(data)

except KeyboardInterrupt:
    print("\n[Info] Program terminated by user.")

except Exception as e:
    print(f"[Error] {e}")

finally:
    print("[Info] Closing connections.")
    if ser.is_open:
        ser.close()
    sock.close()

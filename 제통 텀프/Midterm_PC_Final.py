# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:01:42 2025

@author: won01
"""
import serial
import socket
import sys

# UART 포트 오픈
try:
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    print("Serial port COM7 opened successfully.")
except serial.SerialException as e:
    print(f"[Error] Could not open serial port COM7: {e}")
    sys.exit(1)  # 프로그램 강제 종료

# TCP 소켓 연결
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('10.42.0.42', 12345))  # 라즈베리파이 IP와 포트
    print("TCP socket connected successfully.")
except socket.error as e:
    print(f"[Error] Could not connect to Raspberry Pi TCP server: {e}")
    ser.close()  # 소켓 연결 실패하면 UART도 닫기
    sys.exit(1)

# 메인 통신 루프
try:
    while True:
        # UART로부터 메시지 읽기
        data = ser.readline()

        if data:  # 빈 데이터가 아닐 때만
            print(f"UART received: {data}")
            sock.sendall(data)

except KeyboardInterrupt:
    print("\n[Info] Program terminated by user.")

except Exception as e:
    print(f"[Error] {e}")

finally:
    # 프로그램 종료시 자원 정리
    print("[Info] Closing connections.")
    if ser.is_open:
        ser.close()
    sock.close()
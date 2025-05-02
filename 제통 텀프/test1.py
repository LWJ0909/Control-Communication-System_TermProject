# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:01:27 2025

@author: won01
"""

import serial
import socket

# UART 포트 열기
ser = serial.Serial('COM3', 115200)  # Windows는 COM 포트로 바꿔야 해

# TCP 소켓 열기
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.137.49', 12345))  # 라즈베리파이 IP주소 입력

while True:
    try:
        data = ser.readline()  # UART에서 한 줄 읽기
        sock.sendall(data)     # 읽은 데이터 TCP로 보내기
    except Exception as e:
        print(f"Error: {e}")
        break  # 문제 생기면 루프 탈출

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:03:44 2025

@author: won01
"""

import serial

# UART 포트 열기
ser = serial.Serial('COM7', 115200, timeout=1)  # 포트와 속도 맞게 수정

print("[Info] UART 수신 시작\n")

while True:
    data = ser.readline()

    if data:
        print(data.decode('utf-8').strip())

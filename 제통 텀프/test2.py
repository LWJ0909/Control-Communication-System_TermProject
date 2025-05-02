# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:16:13 2025

@author: won01
"""
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.137.49', 12345))  # 라즈베리파이 IP 주소 넣기

while True:
    msg = input('보낼 메시지 입력: ')
    sock.sendall(msg.encode())  # 입력한 걸 보내기

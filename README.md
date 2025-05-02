# 🚗 Control Communication Systems_TermProject
My ROS2 + Embedded development journal

> My ROS 2 + Embedded system development notes for Raspberry Pi 5

---
## 🧭 Final Goals  
<!-- 내가 최종적으로 구현하고자 하는 프로젝트 목표 정리 -->

1. 📡 **Sensor Data Exchange between STM32 and Raspberry Pi Car**
   - STM32 board handles **ultrasonic** and **gyroscope sensors** (similar to Tesla’s)
   - Sensor values are exchanged with Raspberry Pi-based autonomous vehicle
   - STM32 firmware will follow **RTOS architecture principles** for task separation and timing control
   <!-- STM32 보드에서 초음파/자이로 센서값을 RTOS 구조로 처리하고, 라즈베리파이 차량과 송수신 -->

2. 🛰 **Vehicle-to-Everything (V2X) and V2V Communication with Control Tower**
   - The **PC acts as the central control tower**, while the Raspberry Pi acts as a **vehicle node**
   - Implement **V2X communication** using ROS 2 topics and services
   - Aim to enable **V2V data sharing** for cooperative traffic management and hazard avoidance
   <!-- PC는 관제탑, Pi는 차량으로 설정하여 ROS 기반의 V2X/V2V 통신 구현 및 교통 문제 해결 -->

3. 🌐 **ROS 2 as the Core Communication Framework**
   - Use ROS 2 (Iron → later migrate to Jazzy) for all inter-device communication
   - Nodes include: STM32 interface, camera stream, YOLO object detection, PC control interface
   <!-- 모든 센서 및 제어 시스템 간 통신은 ROS 2를 사용하며, 향후 Jazzy 버전으로 전환 예정 -->

4. 🚗 **YOLO-based Autonomous Driving Features**
   - Equip the Pi car with a camera and run **YOLOv5 or YOLOv8** for object detection
   - Implement core self-driving behaviors: obstacle detection, lane following, basic decision-making
   <!-- Pi 차량에 카메라 + YOLO로 기본적인 자율주행 기능(장애물 감지, 차선 인식 등) 구현 -->

5. 🔐 **(Optional) Embedded Security Layer**
   - If time allows, explore methods to **prevent traffic data hijacking or malicious control**
   - Research basic encryption, authentication, and secure ROS 2 communication (DDS security)
   <!-- 여유가 된다면, 외부 해킹 방지를 위한 통신 보안 기능도 설계 및 구현 시도 -->


---
## 📘 ROS 2 Plans

- Initially planned to install **ROS 2 Iron**
- BUT Iron is still not fully stable on Ubuntu 24.04 and Raspberry Pi  
  <!-- iron은 24.04에서 공식 릴리스 됐지만, 일부 패키지 부족하거나 이슈 있음 -->

> 🔁 **Plan to migrate to ROS 2 Jazzy** when it officially releases with better support

- GitHub repo will track all config/scripts for future portability
- Will version changes per ROS release for compatibility

---
## 📚 Daily Logs

- [🗓️ May 2, 2025](logs/2025-05-02.md)
- [🗓️ May 3, 2025](logs/2025-05-03.md)  


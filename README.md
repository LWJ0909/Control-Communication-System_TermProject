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

## 📅 Date  
## 🗓️ May 2, 2025 – Daily Log

### 🎯 Goal  
Install Ubuntu 24.04 on both my **laptop (control tower)** and **Raspberry Pi 5 (vehicle)**  
and verify mutual communication (e.g., SSH or VNC), since Ubuntu 22.04 is **not supported on Pi 5**.

<!-- 오늘의 목표: 라즈베리파이5에는 22.04가 안 되기 때문에, 24.04를 노트북과 Pi 모두에 설치하고 서로 연결 테스트까지 해보는 것 -->

---


## 🔨 Installation Attempts

### 1. Ubuntu 24.04 for laptop

- 💻 Upgraded my **laptop from Ubuntu 22.04 → 24.04**
  - Successfully performed full release upgrade
  - Removed ROS 2 Humble, planned for Iron → Jazzy

---

### 2. Ubuntu 24.04 Server (64-bit)

- ✅ **What I Tried**:
  - Used **Raspberry Pi Imager v1.9.3**
  - OS: `Ubuntu Server 24.04.2 LTS (64-bit)`
  - Customizations:
    - Hostname (`raspi5-1.local`)
    - Username/password (`lwj` / `123456789`)
    - Wi-Fi: `LWJ / 123456789`
    - SSH enabled  

- ❌ **Problems**:
  - No HDMI display
  - Green LED blinking irregularly → possible boot error
  - SSH refused connection
  - `/boot` lacked `userconf.txt`, `network-config`, `ssh`

- 💡 **Troubleshooting Notes**:
  - Server version has no GUI (expected)
  - Possibly failed OS customization
  - SD card may not have flashed properly
  - Dealing with so many boot errors really drained me.

---

### 3. Ubuntu 24.04 Desktop (64-bit)

- ✅ **What I Tried**:
  - Switched to `Ubuntu Desktop 24.04.2 LTS`
  - Re-applied same customization

- ❌ **Problems**:
  - Headless boot attempted multiple times without success
  - `/boot` contained `user-data`, `meta-data`, but GUI setup was blocked
  - No HDMI monitor available → couldn't complete first-time configuration

---

## ⚠️ Issues & Observations

- SD card sometimes not detected in Raspberry Pi Imager  
  ➤ Resolved using GParted to unmount or clear partitions

- RPi wouldn't connect to PC's Wi-Fi hotspot  
  ➤ But **connected successfully to smartphone hotspot**

- LED blink patterns useful for diagnosing boot status  
  ➤ E.g., consistent fast blinking = trying to boot, then stalls

- Safe shutdown is hard on Ubuntu Server  
  ➤ No GUI means force shutdown may be unavoidable

---


### ❌ Final Outcome

- 🟥 Raspberry Pi could not fully boot or complete first login without HDMI
- 🟥 No SSH/VNC access possible due to missing user initialization
- ✅ Laptop upgrade + ROS preparation was successful

> ❗ **Ultimately, the setup had to be paused due to the lack of an HDMI cable.**
> Will retry later using a monitor or by preparing a Pi OS image with auto-login enabled.

<!-- HDMI 선이 없어서 GUI 진입 실패 → SSH/VNC 접속도 불가능했고 결국 설치 포기 -->

---
## ✅ Next Steps

- Finish ROS 2 installation + minimal test (Iron → Jazzy prep)
- Connect STM32 sensor via serial/UART
- Start YOLO + camera integration
- Enable VNC for GUI-less control (just in case)


---

## 🗓️ May 3, 2025 – Daily Log

### 🎯 Goal  
...

### 🔨 What I Did  
...

### ⚠️ Issues & Notes  
...

### ✅ Outcome  
...



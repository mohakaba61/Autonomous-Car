# 🏎️ Mini-Autonomous-Car

A palm-sized self-driving car built on a Raspberry Pi that combines real-time computer vision, embedded control, and IoT connectivity.  
**Goal:** prove you can get >90 % object-detection accuracy and collision-free navigation in 95 % of test runs—on hardware that fits in a shoebox.

---

## ✨ Key Features
| Capability | Detail |
|------------|--------|
| **Real-time perception** | TensorFlow Lite + OpenCV @ 20 FPS on-board |
| **Path planning** | A* search with dynamic replanning |
| **Control loop** | PID throttle + steering, 30 % lower latency after C++/Python optimizations |
| **Connectivity** | Bluetooth & Wi-Fi for telemetry + OTA commands |
| **UIs** | Flutter mobile dashboard • ElectronJS desktop console |
| **Data logging** | JSON over MQTT, auto-sync to AWS S3 |

---

## 🛠️ Hardware
- Raspberry Pi 4 B (4 GB)  
- Pi Camera v2  
- HC-SR04 ultrasonic sensor  
- L298N dual H-bridge + 2× 9 g micro-servos  
- 18650 Li-ion battery pack w/ BMS  
*(full BOM in `/docs/hardware.md`)*

## 📦 Software Stack
| Layer | Tech |
|-------|------|
| **Vision** | OpenCV 4, TensorFlow Lite, NumPy |
| **Control** | Custom C++ drivers + Python wrappers |
| **Comms** | MQTT (paho), Flask REST endpoints |
| **Dashboards** | Flutter, ElectronJS |
| **DevOps** | Docker, GitHub Actions CI |  

---

## 🚀 Quick Start

1. **Flash & SSH**  
   ```bash
   # Raspberry Pi OS Lite
   sudo raspi-config  # enable I2C, SPI, camera

# 🚀 Linux System Monitoring & Debugging Tool

A Python-based system-level monitoring and debugging tool designed to analyze real-time system performance, inspect processes, and track file descriptors — inspired by tools like `top`, `htop`, and `lsof`.

---

## 📌 Features

### 🔹 System Monitoring
- Real-time CPU usage tracking
- Memory usage analysis
- Top processes by CPU consumption
- Live terminal dashboard using Rich

### 🔹 Debug Mode (Key Feature)
- Inspect any process using PID
- View:
  - Process name & status
  - CPU & memory usage
  - Thread count
  - Executable path

### 🔹 File Descriptor Tracking
- Displays open files of a process
- Helps understand resource usage
- Similar to `lsof` functionality

### 🔹 Logging & Alerts
- Logs high CPU/memory usage
- Helps detect anomalies

---

##  Tech Stack

- Python
- psutil (system monitoring)
- rich (CLI UI)
- argparse (CLI handling)

---

##  Concepts Covered

- Operating Systems (Processes, Memory)
- System Monitoring
- Debugging & Observability
- File Descriptors
- Linux/macOS System APIs

---

##  Installation

```bash
git clone https://github.com/YOUR_USERNAME/linux-system-monitoring-tool.git
cd linux-system-monitoring-tool

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python3 main.py


## Usage

```bash
python3 main.py

Enter Debug Mode:
Press: Ctrl + C

Then enter a PID to inspect the process.

##  Project Structure
linux_system_monitoring_debugging_tool/
│── main.py
│── monitor/
│   ├── cpu.py
│   ├── memory.py
│   ├── process.py
│   ├── debug.py
│── utils/
│   ├── logger.py
│── requirements.txt


Author

Raunak Jain
B.Tech CSE (Cybersecurity)
Aspiring Systems & Platform Engineer

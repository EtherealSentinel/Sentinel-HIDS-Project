# 📘 Sentinel-HIDS - Usage Guide

## 🚀 Introduction

Sentinel-HIDS is a lightweight Host-Based Intrusion Detection System (HIDS) built in Python.  
It monitors a specified directory for file system events such as creation, deletion, and modification.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EtherealSentinel/Sentinel-HIDS-Project.git
   ```
2. Navigate into the project directory:
   ```bash
   cd Sentinel-HIDS-Project
   ```
3. Install the required Python packages:
   ```bash
   pip install watchdog rich
   ```

---

## ⚙️ Configuration

You can configure the monitored directory by editing the `config.json` file:

```json
{
    "monitor_path": "./test_directory"
}
```
- Set the `monitor_path` to the folder you want to monitor.
- By default, it monitors the `./test_directory` directory inside the project.

---

## 🛡️ Running the HIDS

Simply run the `main.py` file:

```bash
python main.py
```

- You will see color-coded alerts in your terminal:
  - 🟩 Green → File created
  - 🔵 Red → File deleted
  - 🟨 Yellow → File modified

- All events are also logged in the `alerts.log` file.

---

## 📝 Notes

- Modified events are filtered to avoid duplicate logging within a short period.
- The system is lightweight and intended for educational and research purposes.

---

## 📈 Roadmap

- [ ] Hash-based modification detection
- [ ] Webhook or email alert integration
- [ ] Multi-directory monitoring
- [ ] GUI development (optional)

---

## 📜 License

This project is licensed under the MIT License — see the `LICENSE` file for details.

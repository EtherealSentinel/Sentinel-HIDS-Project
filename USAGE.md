# 📘 Sentinel-HIDS - Usage Guide

## 🚀 Introduction

Sentinel-HIDS is a lightweight Host-Based Intrusion Detection System (HIDS) built with Python.
It monitors multiple directories for file system events such as creation, deletion, and modification in real time.

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
   pip install watchdog rich psutil requests
   ```

---

## ⚙️ Configuration

You can configure which directories to monitor by editing the config.json file.
This allows for easy customization.

```json
{
    "monitor_paths": ["./test_directory", "./another_directory"],
    "webhook_url": "https://your_webhook_url_here"
}

```
- monitor_paths: List of directories you want to monitor (can include multiple paths).
- webhook_url: Optional — URL for sending critical alerts via Webhook.

---

## 🛡️ Running the HIDS

Simply run the `main.py` file:

```bash
python main.py
```

- You will see color-coded alerts in your terminal:
  - 🟩 Green → File created
  - 🔴 Red → File deleted
  - 🟨 Yellow → File modified

- All events are also logged in the `alerts.log` file.
- Critical events such as file deletions and hash changes are separately logged in `critical_alerts.log`.

---

## 📝 Notes

- Modified events are filtered to avoid duplicate logging within a short period (to avoid redundancy).
- SHA-256 hashes are calculated for files to detect real content changes.
- The system is lightweight and primarily intended for educational and research purposes.

---

## 📈 Roadmap

- [x] Hash-based modification detection
- [x] Webhook integration for real-time alerts
- [x] Multi-directory monitoring
- [ ] GUI development (optional future update) 

---

## 📜 License

This project is licensed under the MIT License — see the `LICENSE` file for details.

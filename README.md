# Sentinel-HIDS (Host-Based Intrusion Detection System)

This is a personal Blue Team project designed to monitor file system activity on a local machine.

The tool detects file creation, modification, and deletion events within a specified directory and logs them in real time.

🚨 **Current Scope**:
- 📂 Watch Multiple Directories: Now supports monitoring multiple directories simultaneously, providing broader coverage for file system activity detection. (using     watchdog)
- 🖥️ Color-coded terminal alerts (via rich)
- 📝 General logging to alerts.log
- 🔐 File integrity check via SHA-256 hash
- 📛 Critical alerts (deletions, hash changes) logged separately in critical_alerts.log
- ⚙️ Dynamic Configuration: Easily customizable settings through config.json to suit different monitoring needs.
- 🖧 Webhook Alerts: Real-time notifications sent via webhooks for critical changes, enabling faster responses and integrations with other systems.

🔧 **Tech Stack**:
- Python 3
- watchdog
- psutil
- rich (for terminal styling)
- hashlib
- logging

🛡️ **Purpose**:
This project is part of my cybersecurity learning journey, especially focused on Blue Team practices and SOC tooling.
It is intended for educational and research purposes only, not for production deployment.

👤 Author: [EtherealSentinel](https://github.com/EtherealSentinel)

🚧 **Status: Still under active development**.
- Advanced Webhook Customization: Further flexibility in webhook integration and alert management.
- GUI Interface: A graphical interface for easier management and monitoring.
- Additional File Integrity Checks: Exploring more robust file integrity verification techniques.

- still under development

# Sentinel-HIDS (Host-Based Intrusion Detection System)

This is a personal Blue Team project designed to monitor file system activity on a local machine.

The tool detects file creation, modification, and deletion events within a specified directory and logs them in real time.

🚨 **Current Scope**:
- 📂 Watch a directory for changes (using watchdog)
- 🖥️ Color-coded terminal alerts (via rich)
- 📝 General logging to alerts.log
- 🔐 File integrity check via SHA-256 hash
- 📛 Critical alerts (deletions, hash changes) logged separately in critical_alerts.log
- ⚙️ Dynamic configuration through config.json

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
- Future plans include multi-directory monitoring, webhook alerts, and potential GUI interface.
- still under development

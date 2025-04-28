# Sentinel-HIDS (Host-Based Intrusion Detection System)

This is a personal Blue Team project designed to monitor file system activity on a local machine.

The tool detects file creation, modification, and deletion events within a specified directory and logs them in real time.

🚨 **Current Scope**:
- 📂 Multi-Directory Monitoring: Watch multiple directories simultaneously (using watchdog).
- 🖥️ Color-Coded Terminal Alerts: Real-time colored alerts (via rich library)
- 📝 General logging to alerts.log
- 🔐 File Integrity Checking: Detects changes with SHA-256 hash validation.
- 📛 Critical alerts (deletions, hash changes) logged separately in critical_alerts.log
- ⚙️  Dynamic Configuration: Easily customize settings via config.json.
- 🖧 🖧 Webhook Integration: Send real-time critical alerts via Webhooks (e.g., Discord, Slack).

🔧 **Tech Stack**:
- Python 3
- watchdog
- psutil
- rich (for terminal styling)
- hashlib
- logging
- requests

🛡️ **Purpose**:
This project is part of my cybersecurity learning journey, especially focused on Blue Team practices and SOC tooling.
It is intended for educational and research purposes only, not for production deployment.

👤 Author: [EtherealSentinel](https://github.com/EtherealSentinel)

🚧 **Status: Still under active development**.
- Advanced webhook customization (e.g., custom payloads, multiple endpoints).
- Basic GUI Interface for easier management.
- Additional file integrity validation techniques.

- still under development

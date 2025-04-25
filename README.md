# Sentinel-HIDS (Host-Based Intrusion Detection System)

This is a personal Blue Team project designed to monitor file system activity on a local machine.

The tool detects file creation, modification, and deletion events within a specified directory and logs them in real time.

🚨 **Current Scope**:
- Watch directory for changes (based on watchdog)
- Log alerts with timestamps to a local file
- Print terminal notifications for each event

🔧 **Tech Stack**:
- Python 3
- watchdog
- psutil
- rich (for terminal styling)

🛡️ **Purpose**:
This project is part of my cybersecurity learning journey, focusing on Blue Team practices and SOC tooling.  
It's not intended for production use — purely educational.

👤 Author: [EtherealSentinel](https://github.com/EtherealSentinel)

- still under development

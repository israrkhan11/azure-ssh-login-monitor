# Azure VM SSH Login Monitoring (Mini Project)

## Overview
This mini cybersecurity project monitors failed SSH login attempts on a Linux-based Azure Virtual Machine using Python.

## Technologies
- Azure Linux VM
- Ubuntu
- Python 3
- SSH

## How It Works
- Reads authentication logs from `/var/log/auth.log`
- Detects `Failed password` entries
- Alerts for suspicious login attempts

## How to Run
```bash
sudo python3 login_monitor.py

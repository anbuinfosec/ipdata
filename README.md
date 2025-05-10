# IP Info Checker

A simple Python tool to fetch IP address information using the [ipdata.co](https://ipdata.co) API.  
Supports random User-Agent generation, IPv4/IPv6 validation, and threat detection info.

---

## Features

- Validate IPv4 and IPv6 addresses
- Query IP geolocation and threat data
- Random User-Agent headers
- Supports both CLI arguments and interactive input
- Colorized terminal output

---

## Requirements

- Python 3.6+
- `requests`

Install dependencies:
```bash
pip install -r requirements.txt
````

---
## Install
```bash
pkg install python -y
pkg install git -y
git clone https://github.com/anbuinfosec/ipdata
```

## Usage

### Command Line

```bash
python main.py -i 8.8.8.8
```

### Interactive

```bash
python main.py
```

---

## File Structure

```
.
├── main.py         # Entry script with CLI support
├── function.py     # Core logic and reusable functions
├── color.py        # ANSI color codes
├── key.txt         # Your ipdata API key (Python format)
└── README.md       # Project documentation
```
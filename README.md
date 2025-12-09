# Awqaat – Islamic Prayer Time & Qibla Application

Awqaat is a Python/Kivy-based application developed for the COSC-3411 course project.  
It provides accurate daily Islamic prayer times, calculates the Qibla direction, and displays all results through a clean graphical interface.

The project is designed with modular architecture, making it easy to expand, maintain, and test.

---

# 📌 Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Project Structure](#project-structure)  
5. [Requirements](#requirements)  
6. [Installation](#installation)  
7. [Running the Application](#running-the-application)  
8. [Configuration](#configuration)  
9. [Usage Examples](#usage-examples)  
10. [Prayer Time Calculation](#prayer-time-calculation)  
11. [Qibla Calculation Method](#qibla-calculation-method)  
12. [API Integration (AlAdhan)](#api-integration-aladhan)  
13. [Troubleshooting](#troubleshooting)  
14. [Future Improvements](#future-improvements)  
15. [License](#license)

---

# 📘 Project Overview

Awqaat helps users:

- Know accurate Islamic prayer times  
- Determine the Qibla direction  
- Automatically detect their current location  
- View everything inside a user-friendly Kivy UI  

This project was built following COSC-3411 project requirements:

✔ Fully working implementation  
✔ Uploaded to GitHub under the correct path  
✔ Includes README with setup instructions  
✔ Includes presentation summarizing design and demo  

---

# ⭐ Features

### 🔹 **1. Automatic Location Detection**
Retrieves:
- City name  
- Latitude  
- Longitude  
Using geolocation APIs or system info.

### 🔹 **2. Prayer Time Calculation**
Two modes:

#### **A. Offline Local Calculation**
Traditional Muslim prayer algorithms implemented directly.

#### **B. Online API Calculation**
Uses **AlAdhan API** to fetch:
- Fajr  
- Sunrise  
- Dhuhr  
- Asr  
- Maghrib  
- Isha  

### 🔹 **3. Qibla Direction Calculation**
Computes the angle between user location and the Kaaba using spherical trigonometry.

### 🔹 **4. Clean Graphical Interface**
- Built using Kivy  
- Screens controlled via ScreenManager  
- Simple and efficient UI  

### 🔹 **5. Modular Architecture**
All logic is split into:
- `prayer_calculation.py`
- `location_fetcher.py`
- `qibla_calculator.py`

---

# ⚙ Technologies Used

- **Python 3.10–3.14**
- **Kivy** (UI)
- **Requests** (API calls)
- **Geopy** (optional geolocation)
- **Math + trigonometry** (Qibla and sun-angle calculations)

---

# 📋 Requirements

Before installing Awqaat, ensure you have:

- **Python 3.11 or higher** installed
- **Git** for cloning the repository
- **uv** package manager for dependency management
- Internet connection (for API-based prayer times)

---

# 🚀 Installation

Follow these 5 simple steps to get Awqaat up and running:

## Step 1: Install Python

### Windows:
1. Download Python from [python.org/downloads](https://www.python.org/downloads/)
2. **Important:** Check ✅ **"Add Python to PATH"** during installation
3. Run the installer and click **"Install Now"**

**Direct Download Links:**
- [Python 3.12 (64-bit)](https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe)
- [Python 3.11 (64-bit)](https://www.python.org/ftp/python/3.11.11/python-3.11.11-amd64.exe)

**Alternative - Microsoft Store:**
```bash
# Search "Python 3.12" in Microsoft Store and install
```

### Linux (Debian/Ubuntu/Kali):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### macOS:
```bash
brew install python@3.12
```

**Verify Installation:**
```bash
python --version
# or
python3 --version
```

---

## Step 2: Clone the Repository

Open your terminal (Command Prompt, PowerShell, or Terminal) and run:

```bash
git clone --branch v0.0.1 https://github.com/Bones-0/COSC-3411-AwqaatGroup.git
```

Navigate into the project directory:

```bash
cd COSC-3411-AwqaatGroup
```

---

## Step 3: Install UV Package Manager

**uv** is a fast Python package manager that handles all dependencies automatically.

### Windows (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Windows (using pip):
```bash
pip install uv
```

### Linux/macOS:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

**Verify Installation:**
```bash
uv --version
```

---

## Step 4: Install Dependencies

From inside the project directory, run:

```bash
uv sync
```

This command will:
- ✅ Create a virtual environment (`.venv`)
- ✅ Install all required dependencies:
  - `kivy>=2.3.1`
  - `requests>=2.32.5`
  - `geopy>=2.4.1`
  - `geocoder>=1.38.1`
  - `ffpyplayer>=4.5.3`
  - `playsound==1.2.2`

**Note:** This may take a few minutes on first run.

---

## Step 5: Run the Application

Start Awqaat with:

```bash
uv run python src/main.py
```

**Alternative Method (Manual activation):**

### Windows:
```bash
.venv\Scripts\activate
python src/main.py
```

### Linux/macOS:
```bash
source .venv/bin/activate
python src/main.py
```

---

# 🎯 Quick Start Summary

```bash
# 1. Install Python (see Step 1 above)

# 2. Clone the repository
git clone --branch v0.0.1 https://github.com/Bones-0/COSC-3411-AwqaatGroup.git
cd COSC-3411-AwqaatGroup

# 3. Install uv
pip install uv

# 4. Install dependencies
uv sync

# 5. Run the application
uv run python src/main.py
```

---

# 📁 Project Structure

```
COSC-3411-AwqaatGroup/
├── src/
│   ├── main.py                 # Main application entry point
│   ├── prayer_calculation.py   # Prayer time algorithms
│   ├── location_fetcher.py     # Location detection
│   └── qibla_calculator.py     # Qibla direction calculation
├── UserInterface/
│   └── *.kv                    # Kivy UI files
├── images/                     # App images and icons
├── sounds/                     # Audio files
├── pyproject.toml              # Project dependencies
├── uv.lock                     # Locked dependencies
└── README.md                   # This file
```

---

# ⚙ Configuration

The application automatically detects your location. You can also manually configure:

- Prayer calculation method
- Location coordinates
- API preferences

Edit configuration in the app settings or modify `src/config.py` if available.

---

# 📖 Usage Examples

1. **View Prayer Times:** Launch the app to see today's prayer times
2. **Check Qibla Direction:** Navigate to the Qibla screen
3. **Change Location:** Update location in settings for accurate times
4. **Toggle Calculation Mode:** Switch between offline and API-based calculations

---

# 🕌 Prayer Time Calculation

### Offline Mode
Implements traditional Islamic astronomical calculations:
- Solar declination
- Equation of time
- Sun altitude angles
- Twilight angles for Fajr/Isha

### Online Mode (AlAdhan API)
Fetches accurate times from the AlAdhan API with support for various calculation methods.

---

# 🧭 Qibla Calculation Method

Uses spherical trigonometry to calculate the bearing from user location to Kaaba (Mecca):

```
Kaaba Coordinates: 21.4225° N, 39.8262° E
```

Formula uses:
- Great circle distance
- Azimuth angle calculation
- Haversine formula

---

# 🌐 API Integration (AlAdhan)

**Base URL:** `https://api.aladhan.com/v1/timings`

**Parameters:**
- `latitude` & `longitude`
- `method` (calculation method)
- `date` (ISO format)

**Response includes:** Fajr, Sunrise, Dhuhr, Asr, Maghrib, Isha

---

# 🛠 Troubleshooting

### Issue: `python: command not found`
**Solution:** Use `python3` or `py` instead of `python`

### Issue: `uv: command not found`
**Solution:** 
- Close and reopen terminal after installing uv
- Add to PATH manually: `source $HOME/.cargo/env` (Linux/macOS)

### Issue: Kivy won't start
**Solution (Linux):**
```bash
sudo apt install python3-dev libsdl2-dev libsdl2-image-dev \
                 libsdl2-mixer-dev libsdl2-ttf-dev
```

### Issue: Dependencies conflict
**Solution:**
```bash
rm -rf .venv
uv sync --reinstall
```

### Issue: Location not detected
**Solution:** 
- Check internet connection
- Grant location permissions
- Manually enter coordinates in settings

---

# 🔮 Future Improvements

- [ ] Notification system for prayer times
- [ ] Multiple location profiles
- [ ] Dark mode theme
- [ ] Widget for desktop
- [ ] Mobile app version (Kivy for Android)
- [ ] Hijri calendar integration
- [ ] Customizable adhan sounds

---

# 📄 License

This project is developed for educational purposes as part of COSC-3411.

---

# 📞 Support

For issues or questions:
- Open an issue on [GitHub](https://github.com/Bones-0/COSC-3411-AwqaatGroup/issues)
- Contact the development team

---
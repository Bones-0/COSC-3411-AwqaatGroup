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
15. [Group Members](#group-members)  
16. [License](#license)

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

# 📁 Project Structure

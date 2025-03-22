# Pygame Countdown Timer - Documentation

**Made by Nosa**  
© 2025 Nosa. All rights reserved.

---

## 🌟 Project Overview

This project is a **countdown timer** that displays time in a **separate window**.  
It starts from a user-defined time and **automatically updates** when the script is modified and saved.

### ✅ Features:
- Timer stays **centered** on the screen, even when resized.
- Press **Spacebar** to **Pause/Resume** the timer.
- If the countdown reaches **00:00**, it displays **"TIME UP"**.
- **Auto-restarts** when you change the `TIMER_START` value and save the file.

---

## 🛠️ Setup Instructions

### **1. Install Python**
Ensure you have **Python 3.10+** installed on your system.

Check by running:
```sh
python --version
```
or  
```sh
python3 --version
```

If Python is not installed, download it from:  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### **2. Install a Code Editor**
Recommended:
- **VS Code**: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- **PyCharm**: [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

You can use any text editor or IDE of your choice.

---

### **3. Create and Activate a Virtual Environment**
It’s recommended to run the project inside a **virtual environment**.

#### **Mac/Linux Commands**
```sh
python3 -m venv test  # Create a virtual environment named 'test'
source test/bin/activate  # Activate the virtual environment
```

#### **Windows Commands (Command Prompt)**
```sh
python -m venv test  # Create a virtual environment named 'test'
test\Scripts\activate  # Activate the virtual environment
```

#### **Windows Commands (PowerShell)**
```sh
python -m venv test
test\Scripts\Activate.ps1
```
If PowerShell gives a permission error, run this command first:
```sh
Set-ExecutionPolicy Unrestricted -Scope Process
```

Once activated, you should see **(test)** in your terminal prompt, indicating the virtual environment is active.

---

### **4. Install Dependencies**
With the virtual environment activated, install the required packages:
```sh
pip install pygame watchdog
```
This installs:
- **pygame** → For rendering the countdown timer.
- **watchdog** → For detecting file changes and auto-restarting the script.

---

## 🚀 Running the Timer

### **1. Start the Timer**
Once dependencies are installed, run the script:

#### **Mac/Linux**
```sh
python timer.py
```
#### **Windows**
```sh
python timer.py
```
The **countdown timer window** will open.

---

### **2. Auto-Restart When Changing `TIMER_START`**
To enable **automatic restart** when modifying the timer:

#### **Mac/Linux**
```sh
watchmedo auto-restart --patterns="*.py" --recursive -- python timer.py
```

#### **Windows (Command Prompt)**
```sh
watchmedo auto-restart --patterns="*.py" --recursive -- python timer.py
```

#### **Windows (PowerShell)**
```sh
watchmedo auto-restart --patterns="*.py" --recursive -- python timer.py
```

Now, when you change `TIMER_START` in `timer.py` and save, the script **automatically restarts**.

---

## ⌨️ Controls
- **Spacebar** → **Pause/Resume** the countdown.  
- **Resize Window** → Timer text remains **centered**.  
- **Change `TIMER_START` and Save** → Auto-restarts the script with new time.  

---

## 📝 Editing Timer Duration

To change the countdown start time:
1. Open `timer.py` in a text editor.
2. Modify the `TIMER_START` value:
   ```python
   TIMER_START = 10  # Change to 10 minutes
   ```
3. Save the file. If you are using `watchmedo`, the script **automatically restarts**.

---

## 🐞 Troubleshooting

### **1. "ModuleNotFoundError: No module named 'pygame'"**
**Solution:** Ensure the virtual environment is activated and run:
```sh
pip install pygame
```

### **2. Auto-restart not working**
Ensure `watchdog` is installed:
```sh
pip install watchdog
```
Then run:
```sh
watchmedo auto-restart --patterns="*.py" --recursive -- python timer.py
```

### **3. Virtual environment not activating (Mac/Linux)**
If `source test/bin/activate` doesn’t work, try:
```sh
chmod +x test/bin/activate
source test/bin/activate
```

### **4. PowerShell Execution Policy Error (Windows)**
If PowerShell prevents activation, run:
```sh
Set-ExecutionPolicy Unrestricted -Scope Process
```
Then try:
```sh
test\Scripts\Activate.ps1
```

---

## 📜 Copyright Notice

**© 2025 Nosa. All rights reserved.**  
This software is provided for **educational and personal use**.  
Unauthorized reproduction, distribution, or commercial use is **prohibited**.  

---


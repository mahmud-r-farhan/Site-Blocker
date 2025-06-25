# 🛡️ Website Blocker (Windows)

A simple desktop tool to **block or unblock websites** on a Windows machine using a graphical interface. It works by modifying the `hosts` file to redirect unwanted domains to `127.0.0.1`.

Built with **Python + Tkinter**, packaged into a `.exe` with PyInstaller.

---

##  Features

- ✅ Block any website (e.g., `adult website`, `youtube.com`)
- ✅ View currently blocked websites
- ✅ Unblock websites easily
- ✅ Simple GUI, no terminal needed
- ✅ Single `.exe` file with icon

---

##  How It Works

This app modifies the Windows `hosts` file:


```

C:\Windows\System32\drivers\etc\hosts

```

It maps domains to `127.0.0.1`, effectively blocking them:


```

127.0.0.1 facebook.com

```

---

##  Installation

1. **Right-click the `.exe` and choose _"Run as Administrator"_**.
2. Use the buttons to:
   - Block new websites
   - Unblock selected websites
   - View the current list

---

## 🛠 Build It Yourself (For Developers)

> Make sure Python 3.x is installed and added to PATH.

### 1. Install dependencies:

```bash
pip install pyinstaller

```

### 2. Prepare the project files:

-   `main.py` → main Python script
    
-   `icon.ico` → (optional) icon file
    
-   `admin.manifest` → Windows manifest file to request admin rights
    

### 3. Build the `.exe`:

```bash
pyinstaller --onefile --windowed --icon=icon.ico --manifest=admin.manifest main.py

```

Output will be in the `dist/` folder.

----------

## ⚠️ Administrator Rights Required

This app **must run as administrator** to modify system files. If you see "Permission Denied", do the following:

-   Right-click the `.exe` → Choose **Run as Administrator**
    
-   Accept the UAC prompt
    

----------

## 🔐 Security & Safety

-   The app only modifies your local `hosts` file
    
-   No data is sent online or stored externally
    
-   Code is open-source and inspectable
    

----------

##  Screenshots

![GUI Screenshot](https://res.cloudinary.com/dqovjmmlx/image/upload/v1750831241/Screenshot_2025-06-25_115945_seqjts.png)
![GUI Screenshot](https://res.cloudinary.com/dqovjmmlx/image/upload/v1750831240/Screenshot_2025-06-25_120019_y2kuhj.png)

----------


##  Author
Contact: [[dev@devplus.fun](mailto:dev@devplus.fun)]  

----------
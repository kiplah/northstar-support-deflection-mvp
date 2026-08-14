# Northstar Support Deflection MVP

This repository contains the MVP for the Northstar Support Deflection system, built by Pod G29.

## Getting Started

If you are a teammate pulling this code for the first time, follow these steps to get the project running locally.

### 1. Clone the repository
```bash
git clone https://github.com/kiplah/northstar-support-deflection-mvp.git
cd northstar-support-deflection-mvp
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **On Windows (PowerShell):**
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  .\venv\Scripts\Activate.ps1
  ```
- **On Windows (Command Prompt):**
  ```bat
  .\venv\Scripts\activate.bat
  ```
- **On Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```
*(You will know it's activated when you see `(venv)` appear at the beginning of your terminal prompt).*

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Server
```bash
python app.py
```
Open your browser and navigate to `http://localhost:5000` to view the chat interface.

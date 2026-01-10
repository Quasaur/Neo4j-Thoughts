Great choice, Calvin — VS Code pairs beautifully with Zorin OS for modular development. Here’s how to install it cleanly and avoid Flatpak sandboxing issues that can interfere with SDK access:

---

### 🛠️ Recommended Method: Install via `.deb` Package

This gives you full system integration and avoids container limitations.

#### **Step-by-step:**

1. **Download the `.deb` installer**  
    Head to the [official VS Code download page](https://code.visualstudio.com/docs/setup/linux) and grab the `.deb` file for Debian/Ubuntu-based systems.
    
2. **Install via terminal**  
    Open a terminal and run:
    
    ```bash
    sudo apt install ./<filename>.deb
    ```
    
    Replace `<filename>.deb` with the actual file name you downloaded.
    
3. **(Optional) Enable auto-updates**  
    If you want VS Code to update automatically via APT:
    
    ```bash
    sudo apt-get install wget gpg
    wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
    sudo install -D -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/microsoft.gpg
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
    sudo apt update
    sudo apt install code
    ```
    

---

### ⚠️ Avoid Flatpak (Unless You Need It)

Flatpak versions run in a sandbox and may block access to host SDKs, compilers, or shells — which can be a headache for advanced workflows. If you’ve already installed it via Flatpak and hit limitations, switching to the `.deb` version will give you full control.

---

Let me know if you want to automate this install with a script or integrate it into your backup provisioning flow. I can help you modularize it for future deployments.
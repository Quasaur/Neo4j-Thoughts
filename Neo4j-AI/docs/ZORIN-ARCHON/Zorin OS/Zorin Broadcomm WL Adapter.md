Q: how do i get the Broadcom wireless adapter on my 2012 Intel Mac Mini to work with Zorin OS?

Getting the Broadcom wireless adapter working on your 2012 Intel Mac Mini with Zorin OS takes a few steps, especially if you're starting without internet access. Here's a streamlined guide based on successful setups:

---

### 🛠️ Step-by-Step: Enable Broadcom Wi-Fi on Zorin OS

#### 1. **Identify Your Adapter**

Open a terminal and run:

```
lspci -nn | grep Network
```

Look for something like `Broadcom BCM43xx` to confirm the chipset.

---

#### 2. **Remove Conflicting Drivers**

Before installing the correct firmware, clean out any conflicting Broadcom drivers:

```
sudo apt remove broadcom-sta-dkms bcmwl-kernel-source
```

---

#### 3. **Install the Correct Firmware**

If you have Ethernet access:

```
sudo apt update
sudo apt install firmware-b43-installer
```

If you **don’t** have internet on the Mac Mini:

- Use another computer to run:
    
    ```
    sudo apt install --download-only firmware-b43-installer b43-fwcutter
    ```
    
- Copy the `.deb` files from `/var/cache/apt/archives/` to a USB stick.
    
- Transfer them to your Mac Mini and install:
    
    ```
    sudo dpkg -i b43-fwcutter*.deb
    sudo dpkg -i firmware-b43-installer*.deb
    ```
    

---

#### 4. **Handle the Firmware Download Dependency**

The installer tries to fetch [`broadcom-wl-5.100.138.tar`](https://broadcom-wl-5.100.138.tar)`.bz2` from the internet. If you're offline:

- Download it manually from [lwfinger.com](https://www.lwfinger.com/b43-firmware/broadcom-wl-5.100.138.tar.bz2) on another machine.
    
- Place it in a local directory on your Mac Mini.
    
- Trick the installer by editing `/etc/hosts`:
    
    ```
    sudo nano /etc/hosts
    ```
    
    Add:
    
    ```
    127.0.0.1 www.lwfinger.com
    ```
    
- Start a local web server:
    
    ```
    cd /path/to/firmware
    python3 -m http.server 80
    ```
    
- Then re-run the installer.
    

---

#### 5. **Reboot**

After installation:

```
sudo reboot
```

Your Wi-Fi should now be active. If not, let me know the chipset ID and I’ll help troubleshoot further.

Would you like to bundle this into a reusable install script or modular setup for future installs?
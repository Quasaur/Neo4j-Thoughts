# Zorin OS 17.3 Pro Headless Setup Guide for Mac Mini6
## Prerequisites & Hardware Compatibility **Mac Mini6 (2012) Specs to Verify:
- Model: A1347 (Late 2012) 
- CPU: Intel Core i5/i7 (Ivy Bridge) 
- RAM: Minimum 4GB (8GB+ recommended) 
- Storage: 
Available space for Linux installation **Required Items:** 
- USB keyboard and mouse (temporary, for initial setup) 
- Monitor/TV with HDMI or Thunderbolt (temporary) 
- USB flash drive (8GB+) for installation media 
- Ethernet cable (recommended for stable connection) 
- Your M1 MacBook for remote access 
## Phase 1: Preparation (On M1 MacBook) 
### Step 1: Download Zorin OS 17.3 Pro 
1. Download Zorin OS 17.3 Pro ISO from zorin.com 
2. Verify the ISO checksum for integrity 
### Step 2: Create Bootable USB 
1. Install balenaEtcher or use built-in tools: 
```bash 
# Using dd command (be very careful with device names) 
diskutil list 
diskutil unmountDisk /dev/diskX 
sudo dd if=zorin-os-17.3-pro.iso of=/dev/diskX bs=1m 
``` 
2. Safely eject the USB drive 
### Step 3: Configure Mac Mini BIOS Settings 
1. Connect keyboard, mouse, and monitor to Mac Mini 
2. Power on while holding Option key 
3. Boot from USB drive 
4. In BIOS/EFI settings: 
- Disable Secure Boot 
- Enable Legacy Boot support -
- Set USB as first boot priority 
- ## Phase 2: Initial Installation 
### Step 4: Install Zorin OS 
1. Boot from USB installer 
2. Choose "Install Zorin OS" 
3. **Critical Installation Settings:** 
- Select "Minimal installation" to reduce bloat 
- Enable "Install third-party software" for hardware drivers 
- Choose "Erase disk and install" (or manual partitioning if dual-booting) 
- Create user account with strong password 
### Step 5: Initial System Configuration 
1. Complete first-boot setup 
2. Connect to your network via Ethernet (preferred) or WiFi 
3. Update system immediately: 
```bash 
sudo apt update && sudo apt upgrade -y 
``` 
## Phase 3: Install and Configure XFCE4 
### Step 6: Install XFCE4 Desktop Environment 
```bash 
# Install XFCE4 and essential components 
sudo apt install xfce4 xfce4-goodies lightdm -y 

# Set XFCE as default desktop 
sudo update-alternatives --config x-session-manager 

# Select XFCE session 
# Reboot to load XFCE sudo reboot 
``` 
### Step 7: Configure XFCE for Headless Operation 
1. Login to XFCE desktop 
2. Configure minimal resource usage: 
- Disable unnecessary startup applications 
- Reduce visual effects 
- Configure power management to prevent sleep 
## Phase 4: Remote Access Setup 
### Step 8: Install SSH Server 
```bash 
# Install OpenSSH server 
sudo apt install openssh-server -y 

# Enable and start SSH service 
sudo systemctl enable ssh 
sudo systemctl start ssh 

# Configure SSH for security 
sudo nano /etc/ssh/sshd_config 
``` 
**Key SSH Configuration Changes:** 
``` 
Port 22 PermitRootLogin no PasswordAuthentication yes 

# Change to 'no' after setting up key 
auth PubkeyAuthentication yes X11Forwarding yes 
``` 
Restart SSH: 
`sudo systemctl restart ssh` 
### Step 9: Set Up VNC Server for GUI Access 
```bash 
# Install TigerVNC server 
sudo apt install tigervnc-standalone-server tigervnc-xorg-extension -y 

# Configure VNC password 
vncpasswd 

# Create VNC startup script 
nano ~/.vnc/xstartup 
``` 

**VNC Startup Script Content:** 
```bash 
#!/bin/bash 
unset SESSION_MANAGER 
unset DBUS_SESSION_BUS_ADDRESS 
exec startxfce4 
``` 
Make executable: 
`chmod +x ~/.vnc/xstartup` 
### Step 10: Configure VNC Service 
```bash 
# Create systemd service file 
sudo nano /etc/systemd/system/vncserver@.service 
``` 
**Service File Content:** 
```ini 
[Unit] 
Description=Start TigerVNC server at startup 
After=syslog.target network.target 

[Service] 
Type=forking 
User=yourusername 
Group=yourusername 
WorkingDirectory=/home/yourusername 

PIDFile=/home/yourusername/.vnc/%H:%i.pid 
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1 
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 :%i 
ExecStop=/usr/bin/vncserver -kill :%i 

[Install] 
WantedBy=multi-user.target 
``` 
Enable VNC service: 
```bash 
sudo systemctl daemon-reload 
sudo systemctl enable vncserver@1.service 
udo systemctl start vncserver@1.service 
``` 
## Phase 5: Network Configuration 
### Step 11: Configure Static IP (Recommended) 
```bash 
# Find network interface name 
ip addr show 
# Edit netplan configuration 
sudo nano /etc/netplan/01-netcfg.yaml 
``` 
**Static IP Configuration:** 
```yaml 
network: version: 2 
renderer: networkd 
ethernets: enp0s25: 
# Replace with your interface name 
dhcp4: false addresses: - 192.168.1.100/24 

# Choose available IP in your subnet 
gateway4: 192.168.1.1 
nameservers: 
addresses: [8.8.8.8, 1.1.1.1] 
``` 
Apply configuration: 
`sudo netplan apply` 
### Step 12: Configure Firewall 
```bash 
# Enable UFW firewall 
sudo ufw enable 

# Allow SSH access 
sudo ufw allow ssh 

# Allow VNC access 
sudo ufw allow 5901/tcp 

# Check firewall status 
sudo ufw status 
``` 
## Phase 6: Optimize for Headless Operation 
### Step 13: Disable Unnecessary Services 
```bash 
# Disable services not needed for headless operation 
sudo systemctl disable bluetooth 
sudo systemctl disable cups 
sudo systemctl disable avahi-daemon 

# Optional: Disable GUI login manager if only using remote access 
# sudo systemctl set-default multi-user.target 
``` 
### Step 14: Configure Automatic Login (Optional) 
If you want GUI to start automatically: 
```bash 
sudo nano /etc/lightdm/lightdm.conf 
``` 
Add under `[Seat:*]` section: 
``` 
autologin-user=yourusername 
autologin-user-timeout=0 
``` 
## Phase 7: Remote Access from M1 MacBook 
### Step 15: SSH Access Setup On your M1 MacBook: 
```bash 
# Generate SSH key pair (if not already done) 
ssh-keygen -t ed25519 -C "your_email@example.com" 

# Copy public key to Mac Mini 
ssh-copy-id username@192.168.1.100 

# Test SSH connection 
ssh username@192.168.1.100 
``` 
### Step 16: VNC Client Setup On your M1 MacBook: 
**Option A: Built-in Screen Sharing** 
1. Open Finder 
2. Press Cmd+K 
3. Enter: `vnc://192.168.1.100:5901` 
4. Enter VNC password when prompted 

*Option B: Third-party VNC Client** 
- Install RealVNC Viewer or TigerVNC Viewer 
- Connect to `192.168.1.100:5901` 

### Step 17: Alternative Remote Desktop (Optional) 
For better performance, consider XRDP: 
```bash 
# On Mac Mini 
sudo apt install xrdp -y 
sudo systemctl enable xrdp 
sudo systemctl start xrdp 

# Allow RDP through firewall 
sudo ufw allow 3389/tcp 
``` 
Connect from Mac using Microsoft Remote Desktop app. 
## Phase 8: Final Headless Configuration 
### Step 18: Test Headless Boot 
1. Shut down Mac Mini: `sudo shutdown -h now` 
2. Disconnect keyboard, mouse, and monitor 
3. Power on Mac Mini 
4. Wait 2-3 minutes for boot completion 
5. Test remote connections from MacBook 
### Step 19: Create Connection Aliases 
On your M1 MacBook, add to `~/.ssh/config`: 
``` 
Host macmini 
	HostName 192.168.1.100 
	User yourusername 
	Port 22 
	IdentityFile ~/.ssh/id_ed25519 
``` 
Now you can connect with: `ssh macmini` 
## Phase 9: Maintenance & Troubleshooting 
### Step 20: Setup Monitoring & Maintenance 
```bash 
# Install system monitoring tools 
sudo apt install htop iotop nethogs -y 

# Setup automatic updates (optional) 
sudo apt install unattended-upgrades -y 
``` 
### Common Troubleshooting Commands 
```bash 
# Check system status 
systemctl status ssh 
systemctl status vncserver@1 

# View system logs 
journalctl -u 
ssh journalctl -u vncserver@1 

# Network diagnostics 
ip addr show ss -tulpn | grep :22 ss -tulpn | grep :5901 

# Process monitoring 
ps aux | grep vnc 
ps aux | grep ssh 
``` 
## Security Recommendations 
\. **Change default SSH port** from 22 to custom port 
2. **Disable password authentication** after setting up SSH keys 
3. **Use VPN** if accessing from outside your network 
4. **Regular security updates**: 
```bash 
sudo apt update && sudo apt upgrade -y 
``` 
**Monitor system logs** regularly for unauthorized access attempts 
## Performance Optimization Tips 
- **Limit VNC color depth** to 16-bit for better performance over network 
- **Use SSH tunneling** for VNC traffic: `ssh -L 5901:localhost:5901 macmini` 
- **Consider using tmux/screen** for persistent SSH sessions 
- **Monitor system resources** regularly with `htop` 
## Recovery Options 
If you lose remote access: 
1. **Physical access** 
- reconnect keyboard/monitor temporarily 
1. **Network boot** 
- if configured in BIOS 
1. **Recovery partition** 
- boot to recovery mode 
1. **Reinstallation** 
- worst case scenario 
--- **Note:** Always test each step thoroughly before proceeding to the next. Keep the keyboard and monitor connected until you've verified all remote access methods are working properly.
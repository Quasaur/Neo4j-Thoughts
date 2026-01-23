# Q:
that worked! Now how do i automate the correct startup of vncserver so that it works on reboot?
# A:
Great! Now let's set up VNC to start automatically on boot with the correct configuration. Here are a few methods:

## Method 1: Systemd Service (Recommended)

**1. Create a systemd service file:**

```bash
sudo nano /etc/systemd/system/vncserver@.service
```

**2. Add this content:**

```ini
[Unit]
Description=Start TigerVNC server at startup
After=syslog.target network.target

[Service]
Type=forking
User=calvin
Group=calvin
WorkingDirectory=/home/calvin

PIDFile=/home/calvin/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 -localhost no :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```

**3. Enable and start the service:**

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable the service for display :1
sudo systemctl enable vncserver@1.service

# Start it now to test
sudo systemctl start vncserver@1.service

# Check status
sudo systemctl status vncserver@1.service
```

## Method 2: User Cron Job

**1. Edit your user crontab:**

```bash
crontab -e
```

**2. Add this line:**

```bash
@reboot /usr/bin/vncserver :1 -localhost no -geometry 1920x1080 -depth 24
```

## Method 3: Add to Startup Applications (GUI)

**1. Open "Startup Applications" in Zorin OS** **2. Click "Add" and create a new entry:**

- **Name:** VNC Server
- **Command:** `/usr/bin/vncserver :1 -localhost no -geometry 1920x1080 -depth 24`
- **Comment:** Start VNC Server on boot

## Test the Automation

**1. Reboot your system:**

```bash
sudo reboot
```

**2. After reboot, check if VNC is running:**

```bash
sudo netstat -tlnp | grep 5901
```

**3. Verify it's listening on all interfaces:** You should see `0.0.0.0:5901` in the output.

## Additional Configuration Options

You can customize the VNC server startup by modifying the command with options like:

- `-geometry 1920x1080` - Set screen resolution
- `-depth 24` - Set color depth
- `-dpi 96` - Set DPI
- `-SecurityTypes VncAuth` - Require password authentication

The systemd method is most reliable and gives you better control and logging. Which method would you prefer to use?
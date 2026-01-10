# Q:
why didn't you include the -interface parameter in the ExecStart line of the vncserver@.service file?
# A:
You're absolutely right to question that! I should have included the `-interface` parameter in the systemd service file since that's what actually worked for you.

The `-localhost no` flag alone didn't work in your case - you needed the explicit `-interface 0.0.0.0` parameter to get VNC listening on all interfaces.

Here's the corrected ExecStart line:

```ini
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 -interface 0.0.0.0 -localhost no :%i
```

Or if you want to bind specifically to your Ethernet interface:

```ini
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 -interface [your-ethernet-ip] :%i
```

**Why I missed it:** I made the assumption that `-localhost no` would be sufficient for the systemd service, but your system clearly has some configuration that overrides this setting, making the explicit `-interface` parameter necessary.

**The complete corrected service file should be:**

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
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 -interface 0.0.0.0 -localhost no :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```

Good catch - always use the exact parameters that worked in your manual testing!
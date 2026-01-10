# Q:
ssh connection is working. However, i'm getting the following when issuing the command 'sudo netstat -tlnp | grep 5901': 
"tcp 0 0 127.0.0.1:5901 0.0.0.0:* LISTEN 708/Xtigervnc tcp6 0 0 ::1:5901 :::* "
My ExecStart command is 
"/usr/bin/vncserver -depth 24 -geometry 1920x1080 -interface 0.0.0.0 -localhost no :%i"
# A:
The systemd service isn't using your updated ExecStart command - it's still binding to localhost only. This suggests either:

1. The service file wasn't saved properly
2. systemd needs to be reloaded
3. There's a configuration override somewhere

## Let's troubleshoot:

**1. First, check what's actually in your service file:**

```bash
sudo cat /etc/systemd/system/vncserver@.service
```

**2. Check if systemd loaded the changes:**

```bash
sudo systemctl daemon-reload
sudo systemctl restart vncserver@1.service
```

**3. Check the service status for any errors:**

```bash
sudo systemctl status vncserver@1.service -l
```

**4. Check the service logs:**

```bash
journalctl -u vncserver@1.service -f
```

**5. Verify there's no conflicting config:**

```bash
# Check if there's a system-wide VNC config overriding your settings
cat ~/.vnc/config 2>/dev/null || echo "No user config file"
ls /etc/tigervnc/ 2>/dev/null || echo "No system config directory"
```

**6. If the service file looks correct, try killing any existing VNC and manually testing the systemd service:**

```bash
# Kill any running VNC
vncserver -kill :1

# Stop the service
sudo systemctl stop vncserver@1.service

# Start it again
sudo systemctl start vncserver@1.service

# Check what's listening
sudo netstat -tlnp | grep 5901
```

What do you see when you run these commands? The service file content will tell us if the `-interface 0.0.0.0` parameter is actually there.
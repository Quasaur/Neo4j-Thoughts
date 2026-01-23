# Q:
i did as you asked; when running 
'vncserver :1' 
i got the following reply: 
"New Xtigervnc server 'mcp:1 (calvin)' on port 5901 for display :1. 
Use xtigervncviewer -SecurityTypes VncAuth -passwd /home/calvin/.vnc/passwd :1 to connect to the VNC server. 
vncserver: Can't exec '/home/calvin/.vnc/xstartup': Permission denied 
=================== tail /home/calvin/.vnc/mcp:5901.log =================== 
Can't exec "/home/calvin/.vnc/xstartup": Permission denied at /usr/share/perl5/TigerVNC/Wrapper.pm line 1237. =========================================================================== 
Session startup via '/home/calvin/.vnc/xstartup' exited with status 1! 
Maybe try something simple first, e.g., tigervncserver -xstartup /usr/bin/xterm 
The X session exited with status 1! 
Killing Xtigervnc process ID 5991... success!"
# A:
The VNC server is starting but failing because the `xstartup` script doesn't have execute permissions. Here's how to fix it:

## Fix the Permission Issue

**1. Make the xstartup script executable:**

```bash
chmod +x ~/.vnc/xstartup
```

**2. If the xstartup file doesn't exist or is corrupted, create a new one:**

```bash
# Create a basic xstartup script for Zorin OS (which is Ubuntu-based)
cat > ~/.vnc/xstartup << 'EOF'
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec /etc/X11/xinit/xinitrc
EOF

# Make it executable
chmod +x ~/.vnc/xstartup
```

**3. For a more complete Zorin OS desktop environment, try this xstartup:**

```bash
cat > ~/.vnc/xstartup << 'EOF'
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
export XKL_XMODMAP_DISABLE=1

# Start the desktop environment
if [ -x /usr/bin/gnome-session ]; then
    exec /usr/bin/gnome-session
elif [ -x /usr/bin/startxfce4 ]; then
    exec /usr/bin/startxfce4
else
    exec /usr/bin/xterm
fi
EOF

# Make it executable
chmod +x ~/.vnc/xstartup
```

## Test the Fix

**1. Kill any existing VNC server:**

```bash
vncserver -kill :1
```

**2. Start VNC server again:**

```bash
vncserver :1 -localhost no
```

**3. Check if it's now listening properly:**

```bash
sudo netstat -tlnp | grep 5901
```

You should see it listening on `0.0.0.0:5901` instead of `127.0.0.1:5901`, and without the permission errors.

**4. Test the connection from your Mac:**

```bash
# From Mac terminal, test the connection
telnet [zorin-ip-address] 5901
```

If telnet connects successfully, try your VNC viewer. The desktop environment should now load properly when you connect.
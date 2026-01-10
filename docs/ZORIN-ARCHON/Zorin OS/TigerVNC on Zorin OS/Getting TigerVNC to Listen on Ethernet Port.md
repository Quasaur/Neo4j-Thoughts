# Q: 
TigerVNC is listening on localhost only; how do i get it to listen on the Ethernet port (enp1s0f0)? 
# A: 
You need to configure VNC to listen on all interfaces (or specifically your Ethernet interface) instead of just localhost. Here are the solutions:

## Method 1: Start VNC Server with -localhost no flag

Stop the current VNC server and restart it:

```bash
# Stop current VNC server
vncserver -kill :1

# Start with network access enabled
vncserver :1 -localhost no
```

## Method 2: Edit VNC Configuration File

Create or edit the VNC config file:

```bash
# Edit the VNC config file
nano ~/.vnc/config
```

Add this line to make it listen on all interfaces:

```
localhost=no
```

Or to bind specifically to your Ethernet interface:

```
interface=enp1s0f0
```

Then restart the VNC server:

```bash
vncserver -kill :1
vncserver :1
```

## Method 3: Systemd Service (if using systemd)

If you're using a systemd service, edit the service file:

```bash
sudo systemctl edit vncserver@:1.service
```

Add these lines:

```ini
[Service]
ExecStart=
ExecStart=/usr/bin/vncserver :1 -localhost no
```

Then:

```bash
sudo systemctl daemon-reload
sudo systemctl restart vncserver@:1.service
```

## Verify the Change

After making the change, verify it's now listening on all interfaces:

```bash
sudo netstat -tlnp | grep 5901
```

You should now see something like:

```
tcp  0  0  0.0.0.0:5901  0.0.0.0:*  LISTEN  [process-id]/Xvnc
```

Instead of:

```
tcp  0  0  127.0.0.1:5901  0.0.0.0:*  LISTEN  [process-id]/Xvnc
```

The `0.0.0.0:5901` means it's listening on all network interfaces, including your Ethernet port.
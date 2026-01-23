# Q:
Is there a list in Zorin OS of hosts that are allowed to remote in via TIGER NC (I'm running TigerVNC server on Zorin OS and TigerVNC viewer on MacOS yet I keep getting "Connection refused (61)")?
# A:
The "Connection refused (61)" error you're getting with TigerVNC typically indicates a network connectivity issue rather than a host allow/deny list problem. Let me help you troubleshoot this step by step.

## Common Causes and Solutions:

**1. VNC Server Not Running** First, verify the TigerVNC server is actually running on your Zorin OS machine:

```bash
# Check if VNC server is running
ps aux | grep vnc
# or
systemctl status vncserver@:1.service
```

**2. Firewall Blocking Connection** Zorin OS likely has a firewall blocking the VNC port (default 5901 for display :1):

```bash
# Check firewall status
sudo ufw status

# Allow VNC port (adjust port number if needed)
sudo ufw allow 5901/tcp
```

**3. VNC Server Configuration** Check your VNC server configuration. The main config files are typically:

- `~/.vnc/xstartup` - Desktop environment settings
- `~/.vnc/config` - Server configuration

**4. Network Configuration**

- Ensure both machines are on the same network
- Try connecting from the Zorin machine to itself first: `vncviewer localhost:1`
- Check the exact IP address: `ip addr show`

## Regarding Host Lists:

TigerVNC doesn't use a traditional "hosts allow" file like some services. However, you can configure access control through:

**1. VNC Password Protection**

```bash
# Set VNC password
vncpasswd
```

**2. TCP Wrappers** (if enabled) Check `/etc/hosts.allow` and `/etc/hosts.deny` for entries like:

```
vnc: 192.168.1.0/24
```

**3. VNC Server Startup Options** You can restrict connections when starting the server:

```bash
# Only allow connections from specific IPs
vncserver :1 -localhost no -SecurityTypes VncAuth
```

## Quick Debugging Steps:

1. **Start VNC server explicitly:**
    
    ```bash
    vncserver :1
    ```
    
2. **Test local connection:**
    
    ```bash
    vncviewer localhost:5901
    ```
    
3. **Check what's listening on the port:**
    
    ```bash
    netstat -tlnp | grep 5901
    ```
    
4. **From your Mac, test the connection:**
    
    ```bash
    telnet [zorin-ip-address] 5901
    ```
    

If telnet connects but VNC doesn't, it's a VNC-specific issue. If telnet fails, it's a network/firewall issue.

The most likely culprit is the firewall blocking port 5901. Try the `sudo ufw allow 5901/tcp` command first, then test the connection again.
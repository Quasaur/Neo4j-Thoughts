# Q:
i check support for Wake-on-LAN with the command 'sudo ethtool enp1s0f0 | grep -i wake' and received the following result: "Supports Wake-on: g Wake-on: g"
# A:
Perfect! Your network card already supports Wake-on-LAN and it's already enabled (`Wake-on: g`).

Since WoL is already working, you mainly need to:

## Step 1: Get your MAC address

```bash
ip link show enp1s0f0 | grep ether
```

Note down the MAC address (format like `aa:bb:cc:dd:ee:ff`)

## Step 2: Test Wake-on-LAN from your Mac

**Install wakeonlan on your Mac:**

```bash
# Using Homebrew (if you have it)
brew install wakeonlan

# Or use a built-in method
```

**Test the WoL functionality:**

1. **Shut down your Zorin machine:**
    
    ```bash
    sudo shutdown -h now
    ```
    
2. **From your Mac, send the magic packet:**
    
    ```bash
    # Replace aa:bb:cc:dd:ee:ff with your actual MAC address
    wakeonlan aa:bb:cc:dd:ee:ff
    ```
    
    **Alternative if you don't have wakeonlan installed:**
    
    ```bash
    # Use Python (built into macOS)
    python3 -c "
    import socket
    import binascii
    mac = 'aa:bb:cc:dd:ee:ff'  # Replace with your MAC
    data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(binascii.unhexlify(data), ('255.255.255.255', 9))
    print('WoL packet sent!')
    "
    ```
    

## Step 3: Make WoL persistent (just to be safe)

Even though it's already enabled, let's ensure it stays enabled after reboots:

```bash
sudo nano /etc/systemd/system/wol-enable.service
```

Add:

```ini
[Unit]
Description=Enable Wake On Lan
After=network.target

[Service]
Type=oneshot
ExecStart=/sbin/ethtool -s enp1s0f0 wol g
RemainAfterExit=true

[Install]
WantedBy=multi-user.target
```

Enable it:

```bash
sudo systemctl daemon-reload
sudo systemctl enable wol-enable.service
```

Your Zorin machine should now wake up when you send the magic packet from your Mac! What's the MAC address you got from the `ip link` command?
# Q:
My MAC address is "10:dd:b1:c3:c8:60"
# A:
Perfect! Your MAC address is `10:dd:b1:c3:c8:60`.

## Test Wake-on-LAN now:

**1. First, shut down your Zorin machine:**

```bash
sudo shutdown -h now
```

**2. From your Mac, send the WoL packet using one of these methods:**

**Method A - If you have Homebrew:**

```bash
brew install wakeonlan
wakeonlan 10:dd:b1:c3:c8:60
```

**Method B - Using Python (built into macOS):**

```bash
python3 -c "
import socket
import binascii
mac = '10:dd:b1:c3:c8:60'
data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(binascii.unhexlify(data), ('255.255.255.255', 9))
print('WoL packet sent to', mac)
"
```

**Method C - GUI option:** Download "Wake Me Up" from the Mac App Store and add your Zorin machine with MAC `10:dd:b1:c3:c8:60`.

Your Zorin machine should power on within a few seconds of sending the WoL packet. Once it boots up, you should be able to SSH in and then connect via VNC.

**For future reference, your complete headless workflow is now:**

1. **Wake the machine:** `wakeonlan 10:dd:b1:c3:c8:60` from Mac
2. **Wait 30-60 seconds for boot**
3. **SSH in:** `ssh calvin@[zorin-ip]`
4. **VNC connect:** Use your VNC viewer to connect to the IP

Try shutting down the Zorin machine and waking it up remotely!
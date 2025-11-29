# Q:
i can remote into Zorin from MacOS immediately after reboot; how do i setup wake-on-LAN in Zorin?
# A:
Great! Now let's set up Wake-on-LAN (WoL) so you can wake up your Zorin machine remotely when it's powered off or sleeping.

## Step 1: Check if your network card supports WoL

```bash
# Install ethtool if not already installed
sudo apt install ethtool

# Check WoL support for your ethernet interface
sudo ethtool enp1s0f0 | grep -i wake
```

You should see something like:

```
Supports Wake-on: pumbag
Wake-on: d
```

- **Supports Wake-on:** shows what WoL modes are supported
- **Wake-on:** shows current setting (`d` = disabled, `g` = enabled)

## Step 2: Enable WoL on the network interface

```bash
# Enable Wake-on-LAN
sudo ethtool -s enp1s0f0 wol g
```

**Verify it's enabled:**

```bash
sudo ethtool enp1s0f0 | grep -i wake
```

Should now show `Wake-on: g`

## Step 3: Make WoL persistent across reboots

**Method 1: Create a systemd service**

```bash
sudo nano /etc/systemd/system/wol-enable.service
```

Add this content:

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

Enable the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable wol-enable.service
```

**Method 2: Add to network configuration** Edit the network interface configuration:

```bash
sudo nano /etc/netplan/01-netcfg.yaml
```

Add the `wakeonlan: true` option:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp1s0f0:
      dhcp4: yes
      wakeonlan: true
```

Apply the changes:

```bash
sudo netplan apply
```

## Step 4: Check BIOS settings

Reboot and enter BIOS/UEFI settings, look for:

- **Wake-on-LAN** or **WoL** (enable it)
- **Power Management** settings
- **PME Event Wake Up** (enable it)
- **Deep Sleep** or **ErP** mode (may need to disable for WoL to work)

## Step 5: Get your MAC address for WoL

```bash
# Get MAC address of your ethernet interface
ip link show enp1s0f0 | grep ether
```

Note down the MAC address (format: `aa:bb:cc:dd:ee:ff`)

## Step 6: Test Wake-on-LAN from your Mac

**Install a WoL tool on your Mac:**

```bash
# Using Homebrew
brew install wakeonlan

# Or download a GUI app like "Wake Me Up" from Mac App Store
```

**Send WoL packet:**

```bash
# Replace with your Zorin machine's MAC address
wakeonlan aa:bb:cc:dd:ee:ff
```

## Test the setup:

1. **Put Zorin to sleep or shut it down**
2. **From your Mac, send the WoL packet**
3. **Zorin should wake up/power on**

Let me know what you see when you check the WoL support with ethtool!
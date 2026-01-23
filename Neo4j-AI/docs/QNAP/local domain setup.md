Thanks for the detailed setup, Calvin—this gives us a clear path. Since your **Asus AX6000 router** is handling **DNS, DHCP, and gateway duties**, and your local domain is `mallard.local`, the goal is to make sure your **QNAP TS-h686 NAS** can:

1. **Resolve `.local` hostnames**
2. **Advertise its own hostname within `mallard.local`**
3. **Integrate cleanly with your Linux systems and router’s DNS**

Here’s how to do it:

---

### 🧭 Step-by-Step: Integrate QNAP into `mallard.local`

#### 1. **Assign a Static IP via DHCP Reservation**

- On your Asus router:
    - Go to **LAN → DHCP Server**
    - Reserve a static IP (e.g., `192.168.50.10`) for your QNAP NAS using its MAC address
- This ensures consistent DNS mapping and avoids IP conflicts

#### 2. **Set Hostname on QNAP**

- Go to **Control Panel → System → General Settings**
- Set the **Device Name** to something like `nas` or `qnap`
- This will be used as `nas.mallard.local` or `qnap.mallard.local`

#### 3. **Enable Bonjour (mDNS) on QNAP**

- Go to **Control Panel → Network & File Services → Network Access**
- Enable **Bonjour Discovery Service**
- This allows `.local` resolution via mDNS (used by Linux systems with Avahi)

#### 4. **Configure DNS on QNAP**

- Go to **Control Panel → Network & Virtual Switch → Interfaces**
- Edit your active network adapter:
    - Set **Primary DNS** to `192.168.50.1` (your Asus router)
    - Disable automatic DNS from DHCP if needed
- This ensures QNAP uses your router for name resolution

#### 5. **Test from Linux**

From any Linux machine in `mallard.local`, run:

```bash
ping nas.mallard.local
ssh admin@nas.mallard.local
```

If it fails, check:

```bash
avahi-browse -a | grep nas
```

This confirms mDNS visibility.

---

### 🧠 Optional Enhancements

#### 🔧 Static DNS Mapping (if Asus supports it)

- Some Asus routers allow manual DNS entries:
    - Add `nas.mallard.local → 192.168.50.10` to the DNS table
    - This improves reliability over mDNS

#### 🧱 Firewall & ACLs

- On QNAP, ensure **SSH, SMB, and NFS** services are allowed for your subnet
- Use **Access Control → Shared Folder Permissions** to align with your Linux ACLs

---

Want help scripting a mount routine from Zorin OS to your QNAP using `nas.mallard.local`? I can help you build a modular fstab or systemd mount unit that survives reboots and respects ACLs.
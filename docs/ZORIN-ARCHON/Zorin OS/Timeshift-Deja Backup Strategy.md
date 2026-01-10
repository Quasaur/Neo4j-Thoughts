# Q:
Using both Timeshift and Deja Dup on my 2012 Int Mac Mini6 with 8GB RAM and 500GB SSD running Zorin OS 17.3 Pro, create for me a backup strategy with the following features: - Timeshift will create 7 daily snapshots per week and retain only two weeks of backups. - every Saturday a script you create will sync the local snapshots to an SMB3.0 files are on my QNAP TS-H686 named qtshift. The snapshots on qtshift will never be deleted. - Deja Dup will be used to backup automatically my entire /home folder (including my coding projects in /home/src to my QNAP TS-H686 SMB3.0 file share named qdeja; these backups will never be deleted.

# A:
Here’s a robust, modular backup strategy tailored to your Zorin OS 17.3 Pro setup on your 2012 Intel Mac Mini6, using **Timeshift** and **Déjà Dup**, with automated syncing to your QNAP TS-H686 NAS over SMB 3.0. This setup balances local resilience with off-device redundancy and long-term retention.

---

## 🧭 Overview of Strategy

|Tool|Purpose|Frequency|Destination|Retention Policy|
|---|---|---|---|---|
|**Timeshift**|System snapshots (OS state)|Daily (7/week)|Local SSD + QNAP `qtshift`|2 weeks locally, indefinite on NAS|
|**Déjà Dup**|Home folder backup|Automatic/scheduled|QNAP `qdeja` SMB share|Indefinite|

---

## ⚙️ Step 1: Configure Timeshift

### 🔧 Install & Set Up

```bash
sudo apt install timeshift
sudo timeshift --check
```

### 📅 Configure Snapshot Schedule

- Open Timeshift GUI or run:
    
    ```bash
    sudo timeshift --schedule daily
    sudo timeshift --scripted --create --comments "Auto daily snapshot"
    ```
    
- In GUI: Set retention to **14 snapshots** (2 weeks of daily backups)

---

## 🗃️ Step 2: Create Sync Script for Timeshift → QNAP

### 📁 Mount QNAP SMB Share

Create a mount point:

```bash
sudo mkdir -p /mnt/qtshift
```

Add credentials securely:

```bash
sudo nano /etc/smbcredentials_qtshift
```

```ini
username=your_qnap_user
password=your_qnap_password
```

Secure it:

```bash
sudo chmod 600 /etc/smbcredentials_qtshift
```

Mount via `/etc/fstab`:

```bash
//QNAP_IP/qtshift /mnt/qtshift cifs credentials=/etc/smbcredentials_qtshift,iocharset=utf8,vers=3.0,noperm 0 0
```

### 📝 Sync Script (`/usr/local/bin/sync_timeshift_to_qnap.sh`)

```bash
#!/bin/bash
TIMESHIFT_SRC="/timeshift/snapshots"
QNAP_DEST="/mnt/qtshift/timeshift-backups"

# Ensure mount is active
mountpoint -q /mnt/qtshift || sudo mount /mnt/qtshift

# Sync snapshots
rsync -aAXv --delete "$TIMESHIFT_SRC/" "$QNAP_DEST/"
```

Make it executable:

```bash
sudo chmod +x /usr/local/bin/sync_timeshift_to_qnap.sh
```

### 📆 Schedule with Cron

```bash
sudo crontab -e
```

Add:

```cron
0 3 * * 6 /usr/local/bin/sync_timeshift_to_qnap.sh
```

> Runs every Saturday at 3:00 AM

---

## 🗂️ Step 3: Configure Déjà Dup for /home → QNAP

### 📁 Mount QNAP SMB Share for Déjà Dup

```bash
sudo mkdir -p /mnt/qdeja
```

Create credentials:

```bash
sudo nano /etc/smbcredentials_qdeja
```

```ini
username=your_qnap_user
password=your_qnap_password
```

Secure it:

```bash
sudo chmod 600 /etc/smbcredentials_qdeja
```

Add to `/etc/fstab`:

```bash
//QNAP_IP/qdeja /mnt/qdeja cifs credentials=/etc/smbcredentials_qdeja,iocharset=utf8,vers=3.0,noperm 0 0
```

Mount it:

```bash
sudo mount /mnt/qdeja
```

### 🧭 Configure Déjà Dup

- Open **Backups** from Zorin menu
- Set:
    - **Folder to back up**: `/home`
    - **Exclude**: nothing (unless you want to skip cache/temp)
    - **Storage location**: `/mnt/qdeja`
    - **Schedule**: Daily or Weekly
    - **Retention**: Set to “Keep forever”

---

## 🧠 Optional Enhancements

- **NAS-side snapshots**: Enable ZFS snapshots on `qtshift` and `qdeja` shares for versioning
- **Email alerts**: Add logging + mail notification to your Timeshift sync script
- **Restore testing**: Periodically test restoring from both Timeshift and Déjà Dup to ensure integrity

---

Would you like me to help you wrap this into a modular dashboard or Obsidian.md note for tracking backups and restore points? I can also help you extend this strategy to Archon OS or Supabase environments.
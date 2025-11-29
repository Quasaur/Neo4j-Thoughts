# Q:
How do I Enable IOMMU in the QNAP BIOS on my TS-h686?
# A:
To enable IOMMU in the BIOS on your QNAP TS-h686, you’ll need to access the BIOS/UEFI settings and look for virtualization-related options. Here’s how to do it:

## Accessing BIOS on TS-h686

1. **Power on or restart** your TS-h686
2. **Press the Delete key** repeatedly during boot (some QNAP models use F2 or F12)
3. You should see the BIOS/UEFI setup screen

## Finding IOMMU Settings

The IOMMU setting is typically found under one of these menu locations:

- **Advanced** → **CPU Configuration** → **Intel VT-d** (enable this)
- **Chipset** → **North Bridge** → **Intel VT-d Technology**
- **Advanced** → **Integrated Peripherals** → **Intel VT-d**
- **Security** → **Virtualization Technology**

## What to Enable

Look for these specific settings and enable them:

- **Intel VT-d** (Intel Virtualization Technology for Directed I/O)
- **Intel VT-x** (if not already enabled)
- **IOMMU Support**

## Save and Exit

1. Once enabled, press **F10** to save and exit
2. Confirm the changes when prompted
3. The system will reboot

## Verification

After booting into your OS, you can verify IOMMU is working by checking:

- On Linux: `dmesg | grep -i iommu`
- The presence of `/sys/kernel/iommu_groups/` directory

If you can’t find these exact menu options, the BIOS interface may vary slightly. Look for any virtualization-related settings and enable them. The TS-h686 should support IOMMU since it’s designed for virtualization workloads.​​​​​​​​​​​​​​​​
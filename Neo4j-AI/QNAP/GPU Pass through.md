# Q:
Is my QNAP TS-h686 NAS’ GPU (nVidia GP108 GeForce GT 1030) available for GPU passthrough in the Container Station app that runs on it?
# A:
The NVIDIA GP108 GeForce GT 1030 in your QNAP TS-h686 is unlikely to be available for GPU passthrough in Container Station. Here’s why:

QNAP’s Container Station typically doesn’t support GPU passthrough for several reasons:

1. **Container Station limitations** - It’s designed as a lightweight containerization platform focused on basic Docker functionality, not advanced virtualization features like GPU passthrough.
2. **Hardware requirements** - GPU passthrough requires IOMMU support and proper isolation, which may not be fully implemented in QNAP’s container environment.
3. **Driver complexity** - The NAS would need specialized NVIDIA drivers and container runtime support (like nvidia-docker) which aren’t standard on QNAP systems.
4. **Resource allocation** - The GT 1030 is likely being used by the NAS system itself for hardware transcoding and other multimedia tasks.

**Alternatives to consider:**

- Use the GPU for its intended purpose (hardware transcoding in media applications)
- If you need GPU compute in containers, consider running a separate system with proper GPU passthrough support
- Check if specific QNAP apps can utilize the GPU directly (like Video Station for transcoding)

You could verify GPU availability by SSH’ing into your NAS and running `lspci | grep -i nvidia` or checking `/proc/driver/nvidia/version`, but Container Station’s architecture makes GPU passthrough highly unlikely to work even if the hardware is detected.​​​​​​​​​​​​​​​​
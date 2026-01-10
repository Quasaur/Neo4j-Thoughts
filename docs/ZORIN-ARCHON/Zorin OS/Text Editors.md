# Q:
when i edit the vncserver@.service from the command line, i want to load an xfce4-compatible text editor; how do i do this?
# A:
You can use a few different text editors that are XFCE4-compatible from the command line:

## Option 1: Use mousepad (XFCE4's default text editor)

```bash
sudo mousepad /etc/systemd/system/vncserver@.service
```

## Option 2: Use xed (if installed)

```bash
sudo xed /etc/systemd/system/vncserver@.service
```

## Option 3: Change your default EDITOR environment variable

```bash
# Set mousepad as default editor for this session
export EDITOR=mousepad

# Then use your original command
sudo systemctl edit vncserver@.service
```

Or make it permanent by adding to your `.bashrc`:

```bash
echo 'export EDITOR=mousepad' >> ~/.bashrc
source ~/.bashrc
```

## Option 4: Use the EDITOR variable inline

```bash
sudo EDITOR=mousepad systemctl edit vncserver@.service
```

## Check what text editors you have available:

```bash
# See what GUI text editors are installed
which mousepad xed gedit kate
```

**mousepad** is the most likely to be available since you're using an XFCE4-based environment. It's lightweight and designed specifically for XFCE4.

If none of these GUI editors work, you might need to install mousepad:

```bash
sudo apt update
sudo apt install mousepad
```

Which approach would you prefer?
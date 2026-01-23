# Q:
on the ExecStart command, should the -localhost parameter be "-localhost=no" instead of "localhost no"?
# A:
Good question! For TigerVNC, both formats should work, but let's try the equals sign format to be sure:

**Try this format:**

```ini
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 -interface 0.0.0.0 -localhost=no :%i
```

**However**, since we know that `-interface 0.0.0.0` was the key parameter that worked when you tested manually, you could also try removing the `-localhost` parameter entirely:

```ini
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 -interface 0.0.0.0 :%i
```

## Test which format works:

**1. Edit the service file:**

```bash
sudo mousepad /etc/systemd/system/vncserver@.service
```

**2. Try the equals format first:**

```ini
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 -interface 0.0.0.0 -localhost=no :%i
```

**3. Reload and restart:**

```bash
sudo systemctl daemon-reload
sudo systemctl restart vncserver@1.service
```

**4. Check the result:**

```bash
sudo netstat -tlnp | grep 5901
```

If you still see `127.0.0.1:5901`, then try the version without `-localhost` at all, since the `-interface 0.0.0.0` should be sufficient.

What worked when you tested manually was the exact combination of parameters, so let's make sure the systemd service uses exactly that same syntax.
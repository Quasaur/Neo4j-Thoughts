# Fix Supabase CLI Installation on Zorin OS

## Step 1: Clean Up Previous Installation Attempt

First, let's remove any partial installation:

```bash
# Remove any global npm supabase installation attempt
npm uninstall -g supabase 2>/dev/null || true

# Clean npm cache
npm cache clean --force
```

## Step 2: Install Supabase CLI Using Binary Method

Since npm global installation is no longer supported, we'll use the direct binary installation:

```bash
# Download the latest Supabase CLI binary for Linux
curl -L https://github.com/supabase/cli/releases/latest/download/supabase_linux_amd64.tar.gz -o /tmp/supabase.tar.gz

# Extract the binary
cd /tmp
tar -xzf supabase.tar.gz

# Move to a directory in your PATH (requires sudo for /usr/local/bin)
sudo mv supabase /usr/local/bin/supabase

# Make it executable
sudo chmod +x /usr/local/bin/supabase

# Clean up the downloaded file
rm /tmp/supabase.tar.gz
```

## Step 3: Verify Installation

```bash
# Check if Supabase CLI is installed correctly
supabase --version

# Test basic functionality
supabase help
```

## Alternative Method: Install to User Directory

If you prefer not to use sudo, you can install to your user directory:

```bash
# Create a local bin directory if it doesn't exist
mkdir -p ~/.local/bin

# Download and extract
curl -L https://github.com/supabase/cli/releases/latest/download/supabase_linux_amd64.tar.gz -o /tmp/supabase.tar.gz
cd /tmp
tar -xzf supabase.tar.gz

# Move to user bin directory
mv supabase ~/.local/bin/supabase
chmod +x ~/.local/bin/supabase

# Add to PATH if not already there
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Reload your shell configuration
source ~/.bashrc

# Clean up
rm /tmp/supabase.tar.gz
```

## Step 4: Test Installation

```bash
# Verify the installation works
supabase --version

# Should output something like: supabase version 1.x.x
```

## Step 5: Continue with Local Supabase Setup

Now you can proceed with setting up your local Supabase environment:

```bash
# Create project directory
mkdir ~/supabase-local
cd ~/supabase-local

# Initialize Supabase project
supabase init

# Start local Supabase services
supabase start
```

## Troubleshooting

### If you get "command not found" error:

1. **Check if the binary is in the right place:**
   ```bash
   ls -la /usr/local/bin/supabase
   # or if using user installation:
   ls -la ~/.local/bin/supabase
   ```

2. **Check your PATH:**
   ```bash
   echo $PATH
   ```

3. **Manually add to PATH if needed:**
   ```bash
   # For system installation:
   export PATH="/usr/local/bin:$PATH"
   
   # For user installation:
   export PATH="$HOME/.local/bin:$PATH"
   ```

### If you get permission errors with Docker:

```bash
# Ensure you're in the docker group
sudo usermod -aG docker $USER

# Log out and back in, or run:
newgrp docker
```

## Why This Happened

The Supabase team changed their distribution method and no longer supports global npm installation. The binary method is now the recommended approach for Linux systems like Zorin OS.

## Next Steps

Once Supabase CLI is installed successfully, you can:
1. Initialize your local Supabase project
2. Start the local development environment
3. Configure Archon to use your local Supabase instance
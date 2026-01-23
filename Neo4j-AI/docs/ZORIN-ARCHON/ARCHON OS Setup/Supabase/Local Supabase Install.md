# Installing Supabase Locally on Zorin OS

## Prerequisites

Before installing Supabase, ensure you have the following prerequisites installed:

### 1. Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install Docker and Docker Compose

```bash
# Install Docker
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce -y

# Add your user to docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify installations
docker --version
docker-compose --version
```

**Important**: Log out and log back in (or restart) for the docker group changes to take effect.

### 3. Install Git (if not already installed)

```bash
sudo apt install git -y
```

## Installing Supabase CLI

### Method 1: Using npm (Recommended)

```bash
# Install Node.js and npm if not already installed
sudo apt install nodejs npm -y

# Install Supabase CLI globally
npm install -g supabase
```

### Method 2: Using Direct Binary Download

```bash
# Download the latest Supabase CLI binary
curl -L https://github.com/supabase/cli/releases/latest/download/supabase_linux_amd64.tar.gz -o supabase.tar.gz

# Extract and install
tar -xzf supabase.tar.gz
sudo mv supabase /usr/local/bin/supabase
sudo chmod +x /usr/local/bin/supabase

# Clean up
rm supabase.tar.gz
```

### Verify Installation

```bash
supabase --version
```

## Setting Up Local Supabase Environment

### 1. Create Project Directory

```bash
mkdir ~/supabase-local
cd ~/supabase-local
```

### 2. Initialize Supabase Project

```bash
# Initialize a new Supabase project
supabase init

# This creates a supabase/ directory with configuration files
```

### 3. Start Local Supabase Services

```bash
# Start all Supabase services locally
supabase start

# This will download and start Docker containers for:
# - PostgreSQL database
# - PostgREST API server
# - Supabase Studio (web interface)
# - GoTrue (authentication)
# - Realtime server
# - Storage server
```

**Note**: The first run will take several minutes as it downloads all necessary Docker images.

### 4. Access Your Local Supabase

After successful startup, you'll see output similar to:

```
Started supabase local development setup.

         API URL: http://localhost:54321
          DB URL: postgresql://postgres:postgres@localhost:54322/postgres
      Studio URL: http://localhost:54323
    Inbucket URL: http://localhost:54324
        anon key: your-anon-key-here
service_role key: your-service-role-key-here
```

## Configuration for Archon

Based on your Archon setup, you'll need to configure the following in your Archon `.env` file:

```env
# For local Supabase (as mentioned in Archon docs)
SUPABASE_URL=http://host.docker.internal:8000
SUPABASE_SERVICE_KEY=your-service-role-key-from-supabase-start-output

# Alternative if the above doesn't work:
# SUPABASE_URL=http://localhost:54321
# SUPABASE_SERVICE_KEY=your-service-role-key-here
```

## Useful Commands

### Managing Local Supabase

```bash
# Stop all services
supabase stop

# Reset database (removes all data)
supabase db reset

# View service status
supabase status

# View logs
supabase logs

# Generate TypeScript types (optional)
supabase gen types typescript --local > types/supabase.ts
```

### Database Management

```bash
# Apply migrations
supabase db push

# Create a new migration
supabase migration new migration_name

# Run SQL directly
supabase db sql --file your_file.sql
```

## Troubleshooting

### Common Issues and Solutions

1. **Docker permission errors**:
    
    ```bash
    sudo usermod -aG docker $USER
    # Then logout and login again
    ```
    
2. **Port conflicts**:
    
    ```bash
    # Check what's using ports
    sudo netstat -tulpn | grep :54321
    
    # Stop conflicting services or change Supabase ports
    # Edit supabase/config.toml to change default ports
    ```
    
3. **Services not starting**:
    
    ```bash
    # Check Docker is running
    sudo systemctl status docker
    
    # Start Docker if needed
    sudo systemctl start docker
    ```
    
4. **Connection issues from Archon**:
    
    - Try using `http://localhost:54321` instead of `http://host.docker.internal:8000`
    - Ensure both Supabase and Archon are running
    - Check firewall settings if applicable

### Configuration Files

The main configuration file is located at `supabase/config.toml`. You can modify:

- Database settings
- API settings
- Port configurations
- Authentication settings

## Next Steps

1. **Access Supabase Studio**: Open http://localhost:54323 in your browser
2. **Set up your database schema**: Use the SQL editor or migrations
3. **Configure Archon**: Update your Archon `.env` file with the local Supabase credentials
4. **Run the Archon migration**: Execute the `migration/complete_setup.sql` in Supabase Studio's SQL editor

Your local Supabase installation is now ready to work with Archon!
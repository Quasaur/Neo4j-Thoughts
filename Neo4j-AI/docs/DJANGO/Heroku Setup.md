## Q:
Provide step-by-step instructions for setting up my existing Heroku account for receiving the deployment of wisdom-book, including installation of Heroku CLI on my MacBook7 Pro and which tier/price on Heroku to use for a Django web app connected to a Neo4j AuraDB database (1000+ records), replicating those records locally in a Postgres database which publishes those records to a ReactJS frontend which uses Tailwind CSS to manage global styles.

## A:
# Step-by-Step Heroku Deployment Guide for Wisdom Book

## Part 1: Install Heroku CLI on MacBook Pro

```bash
# Install Heroku CLI via Homebrew
brew tap heroku/brew && brew install heroku

# Verify installation
heroku --version

# Login to your Heroku account
heroku login
# This will open a browser window for authentication
```

## Part 2: Choose Heroku Tier/Pricing

For your Wisdom Book application with 1000+ records:

**Recommended Starting Configuration:**

**Dyno (App Server):**

- **Basic ($7/month)** - Recommended starting point
  - Always on (no sleeping)
  - 512 MB RAM
  - Custom domains with SSL
  - Suitable for low-to-moderate traffic
- **Eco ($5/month)** - Budget alternative
  - Apps sleep after 30 min inactivity
  - 512 MB RAM shared across apps
  - Fine for personal projects with light traffic

**Postgres Database:**

- **Mini ($5/month)** - Recommended for 1000+ records
  - 1 GB RAM
  - 10,000 row limit
  - 20 connections
  - Perfect for your current needs with room to grow
- **Essential-0 ($0/month)** - Testing only
  - 10,000 row limit
  - Very limited performance
  - Not recommended for production


```shell
// heroku app must be created first.
heroku addons:create heroku-postgresql:essential-0
```
**Total Monthly Cost:**

- Production: $12/month (Basic + Mini Postgres)
- Budget: $10/month (Eco + Mini Postgres)

## Part 3: Prepare Your Django Project

### 3.1: Install Required Dependencies

```bash
# Activate your virtual environment first
source venv/bin/activate  # or your venv path

# Install production dependencies
pip install gunicorn dj-database-url psycopg2-binary whitenoise django-cors-headers

# Update requirements.txt
pip freeze > requirements.txt
```

### 3.2: Create Heroku Configuration Files

**Create `Procfile` in project root:**

```
web: gunicorn wisdom_book.wsgi --log-file -
```

**Create `runtime.txt` in project root:**

```
python-3.11.7
```

(Check your Python version with `python --version` and adjust accordingly)

### 3.3: Update Django Settings

**Create or modify `settings.py` for Heroku compatibility:**

```python
import os
import dj_database_url
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-dev-secret-key-change-this')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.herokuapp.com',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # Add if using CORS
    # Your apps here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Add if using CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database configuration
if 'DATABASE_URL' in os.environ:
    # Production - Heroku Postgres
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        )
    }
else:
    # Development - Local Postgres
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'wisdom_book'),
            'USER': os.environ.get('DB_USER', 'postgres'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }

# Neo4j Configuration (for AuraDB)
NEO4J_URI = os.environ.get('NEO4J_URI')
NEO4J_USERNAME = os.environ.get('NEO4J_USERNAME')
NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Whitenoise configuration for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS settings (if React is on different domain during dev)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# In production, you might want:
# CORS_ALLOW_ALL_ORIGINS = True  # Only if needed
```

### 3.4: Create `.gitignore` (if not exists)

```bash
# Create/update .gitignore
cat << 'EOF' > .gitignore
# Python
*.py[cod]
__pycache__/
venv/
env/
*.so
*.egg
*.egg-info/
dist/
build/

# Django
*.log
db.sqlite3
/staticfiles/
/media/

# Environment variables
.env
.env.local

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# React
node_modules/
/build
.env.local
.env.development.local
.env.test.local
.env.production.local
npm-debug.log*
yarn-debug.log*
yarn-error.log*
EOF
```

## Part 4: Prepare React Frontend

### 4.1: Build React for Production

```bash
# Navigate to your React frontend directory
cd frontend  # or wherever your React app is

# Install dependencies (if not already)
npm install

# Create production build
npm run build

# This creates an optimized build in the 'build' directory
```

### 4.2: Configure Django to Serve React

**Option A: Serve React from Django (Recommended for simplicity)**

```bash
# Create static directory in Django project root
mkdir -p backend/static/react  # Adjust path to your structure

# Copy React build to Django static
cp -r frontend/build/* backend/static/react/
```

**Update Django `urls.py` to serve React:**

```python
# In your main urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_api_app.urls')),  # Your API endpoints
    
    # Serve React app - must be last
    re_path(r'^.*$', TemplateView.as_view(template_name='react/index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

## Part 5: Create Heroku App

```bash
# Navigate to your Django project root
cd /path/to/wisdom-book

# Create Heroku app
heroku create wisdom-book-clmjournal
# Or let Heroku generate a name: heroku create

# Verify app was created
heroku apps:info
```

## Part 6: Add Heroku Postgres

```bash
# Add Postgres addon (Mini tier - $5/month)
heroku addons:create heroku-postgresql:mini -a wisdom-book-clmjournal

# Or for free testing tier (not recommended for production):
# heroku addons:create heroku-postgresql:essential-0

# Verify addon was created
heroku addons -a wisdom-book-clmjournal

# Check database info (automatically sets DATABASE_URL)
heroku config:get DATABASE_URL -a wisdom-book-clmjournal
```

## Part 7: Set Environment Variables

```bash
# Generate a new Django secret key
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Set Django configuration
heroku config:set DJANGO_SECRET_KEY='paste-generated-secret-key-here' -a wisdom-book-clmjournal
heroku config:set DEBUG=False -a wisdom-book-clmjournal

# Set Neo4j AuraDB credentials (get these from your Neo4j AuraDB console)
heroku config:set NEO4J_URI='neo4j+s://your-instance.databases.neo4j.io' -a wisdom-book-clmjournal
heroku config:set NEO4J_USERNAME='neo4j' -a wisdom-book-clmjournal
heroku config:set NEO4J_PASSWORD='your-auradb-password' -a wisdom-book-clmjournal

# Verify all config variables
heroku config -a wisdom-book-clmjournal
```

## Part 8: Deploy to Heroku

```bash
# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial Heroku deployment setup"

# Add Heroku remote
heroku git:remote -a wisdom-book-clmjournal

# Deploy to Heroku
git push heroku main
# If your default branch is 'master': git push heroku master:main

# Monitor deployment logs
heroku logs --tail -a wisdom-book-clmjournal
```

## Part 9: Run Database Setup

```bash
# Run Django migrations on Heroku Postgres
heroku run python manage.py migrate -a wisdom-book-clmjournal

# Create superuser for Django admin
heroku run python manage.py createsuperuser -a wisdom-book-clmjournal

# Collect static files
heroku run python manage.py collectstatic --noinput -a wisdom-book-clmjournal

# If you have a custom management command to sync Neo4j → Postgres:
heroku run python manage.py sync_neo4j_to_postgres -a wisdom-book-clmjoural
```

## Part 10: Verify Deployment

```bash
# Open your app in browser
heroku open -a wisdom-book-clmjournal

# Check app status
heroku ps -a wisdom-book-clmjournal

# View logs in real-time
heroku logs --tail -a wisdom-book-cljournal

# Test Django admin
# Navigate to: https://your-app.herokuapp.com/admin

# Run Django shell for debugging
heroku run python manage.py shell -a wisdom-book-cljournal
```

## Part 11: Set Up Automated Neo4j Sync (Optional)

If you need to periodically sync data from Neo4j AuraDB to Postgres:

```bash
# Add Heroku Scheduler addon (free)
heroku addons:create scheduler:standard -a wisdom-book-clmjournal

# Open scheduler dashboard
heroku addons:open scheduler -a wisdom-book-clmjournal
```

**In the Scheduler web interface:**

- Click “Create job”
- Command: `python manage.py sync_neo4j_to_postgres`
- Frequency: Choose based on your needs (Every hour, Every day at…, etc.)
- Click “Save job”

## Part 12: Configure Custom Domain (Optional)

```bash
# Add custom domain
heroku domains:add www.wisdombook.com -a wisdom-book-clmjournal

# Get DNS target
heroku domains -a wisdom-book-clmjournal

# Add CNAME record in your DNS provider:
# CNAME: www -> [dns-target-from-heroku]
```

## Troubleshooting Common Issues

### Issue: Static files not loading

```bash
# Disable collectstatic during build
heroku config:set DISABLE_COLLECTSTATIC=1 -a wisdom-book-clmjournal

# Manually collect static files after deployment
heroku run python manage.py collectstatic --noinput -a wisdom-book-clmjournal
```

### Issue: Database connection errors

```bash
# Check DATABASE_URL is set
heroku config:get DATABASE_URL -a wisdom-book-clmjournal

# Verify database exists
heroku pg:info -a wisdom-book-clmjournal

# Check database credentials
heroku pg:credentials:url DATABASE -a wisdom-book-clmjournal
```

### Issue: Neo4j connection fails

```bash
# Verify Neo4j credentials
heroku config:get NEO4J_URI -a wisdom-book-clmjournal
heroku config:get NEO4J_USERNAME -a wisdom-book-clmjournal
heroku config:get NEO4J_PASSWORD -a wisdom-book-clmjournal

# Test connection in Django shell
heroku run python manage.py shell -a wisdom-book-clmjournal
>>> from neomodel import db
>>> db.cypher_query("RETURN 1")
```

### Issue: React routes return 404

Add this to your Django `urls.py`:

```python
from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    # ... your API routes ...
    
    # Catch-all for React Router
    re_path(r'^(?!admin|api).*$', TemplateView.as_view(template_name='react/index.html')),
]
```

### Issue: CORS errors from React

```python
# In settings.py
CORS_ALLOWED_ORIGINS = [
    "https://your-app.herokuapp.com",
]

# Or for development
CORS_ALLOW_ALL_ORIGINS = True  # Remove in production
```

## Ongoing Maintenance

### View logs

```bash
heroku logs --tail -a wisdom-book-clmjournal
```

### Scale dynos

```bash
# Scale up
heroku ps:scale web=2 -a wisdom-book-clmjournal

# Scale down
heroku ps:scale web=1 -a wisdom-book-clmjournal
```

### Update app after code changes

```bash
git add .
git commit -m "Your update message"
git push heroku main
```

### Backup database

```bash
# Create manual backup
heroku pg:backups:capture -a wisdom-book-clmjournal

# Download backup
heroku pg:backups:download -a wisdom-book-clmjournal
```

### Monitor database usage

```bash
heroku pg:info -a wisdom-book-clmjournal
```

## Cost Summary

**Recommended Production Setup:**

- **Basic Dyno**: $7/month (always on, 512MB RAM)
- **Mini Postgres**: $5/month (1GB RAM, 10K rows, 20 connections)
- **Heroku Scheduler**: Free
- **SSL Certificate**: Free (auto-provisioned)
- **Total: $12/month**

**Budget Setup:**

- **Eco Dyno**: $5/month (sleeps after 30 min, 512MB RAM)
- **Mini Postgres**: $5/month
- **Total: $10/month**

Both tiers include:

- Automatic SSL certificates
- Custom domain support
- Git-based deployment
- Logging and monitoring

-----

Would you like help with any specific step, or do you have questions about your particular project structure?​​​​​​​​​​​​​​​​

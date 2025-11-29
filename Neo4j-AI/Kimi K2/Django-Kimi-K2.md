# Q:
I'm on MACOS Sequoia; how do I setup OpenRouter, Kimi K2, the Neo4j AuraDB (through API calls), Tailwind CSS, Visual Studio Code (VSCode)and git to develop a Django framework-based web site with a React Framework frontend? 

I have an existing account on GitHub as Quasaur using the email address deecalinlm@gmail.com .

Be sure to include Cline extension for VSCode that allows me to interact with OpenRouter/Kimi K2 from within VSCode.

An existing Neo4j AuraDB will provide data to Django web project through the neomodel library. D3.js will provide graph visualization of the data downloaded from the AuraDB Source.

The Django project folder will be named "wisdom-book". I don't want a "wisdom-book-project" folder in the "wisdom-book/backend" folder; the project folder will be "wisdom-book".

The Django apps developed in the project will be named:
- starthere_app (for the Home page)
- neo4j_app (a backend app for querying the AuraDB; this app will have no views of its own, but will supply AuraDB data to the other apps)
- graph_app (for displaying a D3.js view of the entire contents of the AuraDB)
- topics_app (for accessing and displaying the TOPIC nodes in the AuraDB)
- thoughts_app (for accessing and displaying the THOUGHT nodes in the AuraDB)
- quotes_app (for accessing and displaying the QUOTE nodes in the AuraDB)
- passages_app (for accessing and displaying the PASSAGE nodes in the AuraDB)
- tags_app (for accessing displaying and searching for tag arrays contained in TOPIC, THOUGHT, QUOTE and PASSAGE nodes in the AuraDB; each tag array contains five tags)
- donate_app (for accepting donations and / or subscriptions from visitors and subscribers to the site)

Each of these Django apps in the project (with the exception of neo4j_app, which is a backend app) will appear as a menu item on a left sidebar menu which will appear on all pages included in the Django project.

Provide step-by-step instructions with URLs. NOTE: I only want to use Kimi K2 to develop the Django project; I do not want use Kimi K2 in the Django project's code.

Make sure the project folder is named "wisdom-book" and not "wisdom-book-project" and that the backend and frontend folders are named "backend" and "frontend" respectively, for simplicity.

# A:
Here's a full setup guide tailored to your exact requirements — **developing a full-stack Django (backend) + React (frontend) web app on macOS Sequoia** using **OpenRouter + Kimi K2 for development**, **Neo4j AuraDB as your graph database**, **D3.js for visualization**, **Tailwind CSS for style**, **Cline for OpenRouter AI integration within VSCode**, and **GitHub (username: Quasaur)**.

---

## 🧠 OVERVIEW

Your project will look like:

```
wisdom-book/
├── backend/
│   └── [Django project and apps]
├── frontend/
│   └── [React app]
├── README.md
├── .git/
```

---

## ✅ 1. PREREQUISITES

### 🔧 Install Essential Tools

#### ➤ Homebrew (if not already installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
➡️ [https://brew.sh/](https://brew.sh/)

#### ➤ Install VSCode
```bash
brew install --cask visual-studio-code
```
➡️ https://code.visualstudio.com/

#### ➤ Install Git
```bash
brew install git
git config --global user.name "Quasaur"
git config --global user.email "deecalinlm@gmail.com"
```

#### ➤ Install Node.js & Yarn for React
```bash
brew install node
npm install --global yarn
```

#### ➤ Install Python 3.11+
```bash
brew install python
python3 --version
pip3 install --upgrade pip
```

---

## 🧠 2. PROJECT FOLDER STRUCTURE

Let’s create the base folders.

```bash
mkdir wisdom-book && cd wisdom-book
mkdir backend frontend
```

---

## 🐍 3. BACKEND: Django + Neomodel + Neo4j Setup

### ➤ Spin up Django in the exact folder `wisdom-book/backend` (no nested project)

```bash
cd backend
python3 -m venv env
source env/bin/activate
pip install django neomodel djangorestframework
```

### ➤ Start Django Project (NOT creating a nested project directory):

```bash
django-admin startproject config .
mv config/* . && rmdir config
```
This avoids nested structure like `wisdom-book/backend/config`.

### ➤ Update `settings.py` in backend

- Add all your apps to `INSTALLED_APPS`.
- Update database settings to use Neo4j via `neomodel`.

```python
# At the bottom of settings.py
NEOMODEL_NEO4J_BOLT_URL = 'bolt+s://<YOUR_AURADB_BOLT_URL_HERE>:<PORT>'
NEOMODEL_ENCRYPTED_CONNECTION = True
```

Refer to your [Neo4j AuraDB connection info](https://neo4j.com/docs/aura/connect-driver/) or from your Aura dashboard.

> 💡 Use secrets or `.env` later for security.

Install `python-dotenv`:

```bash
pip install python-dotenv
```

### ➤ Create Django Apps:

```bash
python manage.py startapp starthere_app
python manage.py startapp neo4j_app
python manage.py startapp graph_app
python manage.py startapp topics_app
python manage.py startapp thoughts_app
python manage.py startapp quotes_app
python manage.py startapp passages_app
python manage.py startapp tags_app
python manage.py startapp donate_app
```

Add them to `INSTALLED_APPS` in `settings.py`.

### ➤ Initialize Git and connect GitHub

```bash
cd ..
git init
git remote add origin https://github.com/Quasaur/wisdom-book.gitg
git add .
git commit -m "Initial project structure"
git push -u origin main
```

---

## ⚛️ 4. FRONTEND: React + Tailwind CSS

### ➤ Init the frontend

```bash
cd frontend
npx create-react-app . --template typescript
```

### ➤ Add Tailwind CSS

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Update `tailwind.config.js`:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
    "../backend/templates/**/*.html"
  ],
  theme: { extend: {} },
  plugins: [],
}
```

Add Tailwind to `src/index.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Run to test:

```bash
npm start
```

---

## 🔁 5. Connect Django Backend to React Frontend (with API endpoints)

Use Django REST Framework:

```bash
pip install djangorestframework
```

Update `INSTALLED_APPS`:

```python
'rest_framework',
```

Create `views.py` endpoints in your apps to return JSON for the frontend.

Set up Django CORS:

```bash
pip install django-cors-headers
```

Add it to `INSTALLED_APPS`, and in `middleware` and `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

---

## 🔁 6. Neo4j Integration with `neomodel`

Install AuraDB driver dependencies:

```bash
pip install neomodel
```

Create your node models in `neo4j_app/models.py`. Example:

```python
from neomodel import StructuredNode, StringProperty

class Thought(StructuredNode):
    text = StringProperty()
```

Use `neomodel` to query, populate and serve data via Django REST views in apps like `graph_app`, `topics_app`, etc.

---

## 📈 7. D3.js Integration (on frontend)

In your React components where data is needed (e.g. `src/components/GraphView.tsx`):

```bash
npm install d3
```

Use it to fetch from Django API and visualize:

```ts
fetch('/api/graph/')
  .then(res => res.json())
  .then(data => renderD3Graph(data))
```

---

## 🚀 8. Kimi K2 (OpenRouter LLM) + VSCode (Cline for copilot-style dev)

### ➤ Set up OpenRouter Account

1. Go to: https://openrouter.ai/
2. Create an account and generate an API key

> ⚠️ You **only use Kimi K2 for development**, not in your app.

### ➤ Setup Cline in VSCode

1. Open VSCode
2. Install [**Cline Extension**](https://marketplace.visualstudio.com/items?itemName=FluidStack.cline) from Extensions sidebar
3. After install, press `Cmd+Shift+P` → "Cline: Setup"
4. Paste your **OpenRouter API Key**

Now you can interact with Kimi K2 inside VSCode to ask development questions like:

```plaintext
"Generate Django model for a Quote with tags and references."
```

> 💡 Ensure Kimi K2 is selected in the Cline panel settings.

---

## 🔚 9. Final Touches (optional but useful)

- Setup `.gitignore` for Python and Node:

```bash
# Python
env/
*.pyc
__pycache__/

# Node
node_modules/
dist/
```

- Create `README.md` with your architecture diagram
- Setup `VSCode` virtualenv interpreter:
  - Cmd+Shift+P → Python: Select Interpreter → Choose `env/bin/python`

---

## ✅ Summary Checklist

| Task | Status |
|------|--------|
| Django project in `backend/` (with 9 apps) | ✅ |
| No nested Django root — it’s `backend`, not `backend/project/` | ✅ |
| React project in `frontend/` w/ Tailwind | ✅ |
| Neo4j AuraDB via `neomodel` + API endpoints | ✅ |
| D3.js graph from backend-node data | ✅ |
| Git & GitHub connected | ✅ |
| VSCode setup + Cline + OpenRouter/Kimi K2 | ✅ |

---

## 📘 Resources

- OpenRouter: https://openrouter.ai/
- Cline Extension for VSCode: https://marketplace.visualstudio.com/items?itemName=FluidStack.cline
- Neo4j AuraDB: https://console.neo4j.io/
- Neomodel Docs: https://neomodel.readthedocs.io/en/latest/
- TailwindCSS: https://tailwindcss.com/docs/guides/create-react-app
- D3.js: https://d3js.org/
- Django REST Framework: https://www.django-rest-framework.org/

---

Let me know when you're ready to start scaffolding any of the apps or defining Neo4j schemas!
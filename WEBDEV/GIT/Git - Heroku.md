## Q:
I’m creating a new branch of wisdom-book for the live production version of the project on Heroku; I will call it “prod”. 

The purpose for creating the prod branch is to ensure that Neo4j AuraDB authentication secrets aren’t exposed to public visitors to the wisdom-book web app.

To accomplish this objective, is the creation of the prod branch necessary?

If the creation of the prod branch is necessary for protecting Neo4j secrets from the public, how do I propagate sebsequent changes in the main branch to the prod branch?

## A:
## Is a separate `prod` branch necessary?

**No, a separate branch is NOT necessary to protect Neo4j secrets.** This is a configuration/deployment issue, not a branching issue.

## The Right Solution: Environment Variables

You should handle secrets the same way in both development and production using environment variables:

**In your Django settings:**

```python
# settings.py
NEO4J_URI = os.environ.get('NEO4J_URI')
NEO4J_USERNAME = os.environ.get('NEO4J_USERNAME')
NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD')
```

**Locally (development):**

```bash
# .env file (in .gitignore)
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-local-password
```

**On Heroku (production):**

```bash
# Set via Heroku config vars
heroku config:set NEO4J_URI=bolt://your-auradb-url:7687
heroku config:set NEO4J_USERNAME=neo4j
heroku config:set NEO4J_PASSWORD=your-auradb-password
```

## Why This Works

- Your code never contains secrets - they’re always in environment variables
- The same codebase runs in both environments
- `.env` file is in `.gitignore` so local secrets aren’t committed
- Heroku config vars are never exposed to web app visitors
- You can deploy directly from `main` branch

## If You Still Need a Prod Branch

If there’s a different reason you need separate branches (not just secrets), then to propagate changes:

```bash
git checkout prod
git merge main
git push origin prod
```

But again - **for protecting secrets, you don’t need a separate branch at all.** Just use environment variables everywhere and keep secrets out of your repository entirely.

Does your current setup already use environment variables, or are secrets currently hardcoded somewhere in the code?​​​​​​​​​​​​​​​​

# Neo4j AuraDB Backups

This directory contains database backups exported from Neo4j AuraDB.

## ⚠️ Important Security Notice

**Backup files are NOT committed to Git** (they may contain sensitive data).

## Creating a Backup

1. Set environment variables:
   ```bash
   export NEO4J_URI="neo4j+s://cf81ef03.databases.neo4j.io"
   export NEO4J_USERNAME="neo4j"
   export NEO4J_PASSWORD="your-password-here"
   ```

2. Run the export script:
   ```bash
   python3 ANALYSIS/complete_auradb_export.py
   ```

3. The backup will be saved to this folder with timestamp:
   ```
   BACKUPS/auradb_complete_export_YYYYMMDD_HHMMSS.json
   ```

## Alternative: Using a .env File

Create a `.env` file in the project root (this file is gitignored):

```
NEO4J_URI=neo4j+s://cf81ef03.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-password-here
```

Install python-dotenv:
```bash
pip install python-dotenv
```

The script will automatically load credentials from `.env`.

## Backup Contents

Each backup JSON file contains:
- **Metadata**: Export timestamp, source URI
- **Schema**: All indexes and constraints
- **Nodes**: All 774 nodes (TOPIC, DESCRIPTION, THOUGHT, CONTENT, QUOTE, PASSAGE)
- **Relationships**: All 752 relationships

## Storage Recommendations

- Keep backups in this directory (they won't be committed)
- For important backups, copy to secure external storage
- Consider encrypting backups containing production data
- Rotate old backups to save disk space

## Restoring from Backup

To restore data from a backup file, use APOC's import functionality or write a custom Cypher script that processes the JSON and recreates nodes/relationships.

## Security Checklist

- [ ] Never commit passwords or credentials to Git
- [ ] Keep `.env` files in `.gitignore`
- [ ] Rotate Neo4j passwords regularly
- [ ] Store important backups in encrypted locations
- [ ] Review GitHub Security tab for any exposed secrets

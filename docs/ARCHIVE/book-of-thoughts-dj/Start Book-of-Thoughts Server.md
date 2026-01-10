 1. Activate the virtual environment:
  cd /Users/quasaur/Developer/DJANGO/book-of-thoughts/backend
  source vbot/bin/activate
  2. Set up environment variables (create a .env file with Neo4j credentials):
  NEO4J_URI=bolt://localhost:7687
  NEO4J_USERNAME=neo4j
  NEO4J_PASSWORD=your-password
  NEO4J_DATABASE=neo4j
  SECRET_KEY=your-secret-key
  DEBUG=True
  3. Run the Django server:
  python manage.py runserver
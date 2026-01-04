import re
import os

BOOK_PATH = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/Book6E-FINAL.md"
CYPHER_DIR = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher"

def get_book_tweets():
    with open(BOOK_PATH, "r", encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')
    tweets = []
    for line in lines:
        line = line.strip()
        if not line: continue
        # Match date pattern: DD-Mon-YYYY[a-z]?:
        match = re.search(r'^(\d{2}-[A-Za-z]{3}-\d{4}[a-z]?): (.+)', line)
        if match:
            tweets.append({"id": match.group(1), "content": match.group(2)})
    return tweets

def get_cypher_files():
    files = []
    for filename in os.listdir(CYPHER_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(CYPHER_DIR, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                # Try to extract ID from "ID: ..."
                id_match = re.search(r'ID: ([0-9]{2}-[A-Za-z]{3}-[0-9]{4}[a-z]?)', content)
                files.append({
                    "filename": filename,
                    "id": id_match.group(1) if id_match else None,
                    "content": content
                })
    return files

book_tweets = get_book_tweets()
cypher_files = get_cypher_files()

missing = []
for tweet in book_tweets:
    found = False
    # First search by ID
    for f in cypher_files:
        if f['id'] == tweet['id']:
            found = True
            break
    
    # If not found by ID, search by content (first 30 chars)
    if not found:
        snippet = tweet['content'][:30]
        for f in cypher_files:
            if snippet in f['content']:
                found = True
                break
    
    if not found:
        missing.append(tweet)

print(f"Total book tweets: {len(book_tweets)}")
print(f"Total cypher files: {len(cypher_files)}")
print(f"Missing tweets from book: {len(missing)}")
for m in missing:
    print(f"- {m['id']}: {m['content'][:50]}...")

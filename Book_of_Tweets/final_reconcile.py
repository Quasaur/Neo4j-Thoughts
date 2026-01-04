import re
import os

BOOK_PATH = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/Book6E-FINAL.md"
CYPHER_DIR = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher"

def clean_content(text):
    text = text.replace('\\', '').replace('...', '').replace('..', '')
    text = re.sub(r'\s+', ' ', text).strip().lower()
    return text

def get_book_tweets():
    with open(BOOK_PATH, "r", encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')
    tweets = []
    for line in lines:
        line = line.strip()
        if not line: continue
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
                # Extract search terms: ID and cleaned content
                id_match = re.search(r'ID: ([0-9]{2}-[A-Za-z]{3}-[0-9]{4}[a-z]?)', content)
                files.append({
                    "filename": filename,
                    "id": id_match.group(1) if id_match else None,
                    "clean_content": clean_content(content)
                })
    return files

book_tweets = get_book_tweets()
cypher_files = get_cypher_files()

missing = []
for tweet in book_tweets:
    found = False
    
    # Check by ID in ID field
    for f in cypher_files:
        if f['id'] == tweet['id']:
            found = True
            break
    
    # Check if ID exists anywhere in the file (sometimes it's just in a comment)
    # Actually, let's check content directly
    if not found:
        ct = clean_content(tweet['content'][:50])
        for f in cypher_files:
            if ct in f['clean_content']:
                found = True
                break
    
    if not found:
        missing.append(tweet)

print(f"Book Tweets: {len(book_tweets)}")
print(f"Cypher Files: {len(cypher_files)}")
print(f"Missing from Cypher: {len(missing)}")
for m in missing:
    print(f"{m['id']}: {m['content'][:100]}")

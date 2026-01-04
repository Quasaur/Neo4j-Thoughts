import re
import os

BOOK_PATH = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/Book6E-FINAL.md"
CYPHER_DIR = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher"

def clean_content(text):
    # Remove backslashes, ellipses, spaces, and lowercase it
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
                files.append({
                    "filename": filename,
                    "content": content
                })
    return files

book_tweets = get_book_tweets()
cypher_files = get_cypher_files()

missing = []
for tweet in book_tweets:
    found = False
    clean_book = clean_content(tweet['content'][:50])
    for f in cypher_files:
        clean_file = clean_content(f['content'])
        if clean_book in clean_file:
            found = True
            break
    
    if not found:
        # Fallback: check if ID is in filename (slugified)
        slug = tweet['id'].upper()
        for f in cypher_files:
            if slug in f['filename']:
                found = True
                break

    if not found:
        missing.append(tweet)

print(f"Total book tweets: {len(book_tweets)}")
print(f"Total cypher files: {len(cypher_files)}")
print(f"Missing tweets: {len(missing)}")
for m in missing:
    print(f"- {m['id']}: {m['content'][:100]}")

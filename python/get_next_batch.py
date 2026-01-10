import os
import re

# Standards
PROJECT_STANDARDS = "project_standards.md"
BOOK_PATH = "Book_of_Tweets/Book6E-FINAL.md"
START_FROM = "25-Jul-2010" # ID of the 31st tweet

def extract_tweets(limit=20):
    with open(BOOK_PATH, "r") as f:
        content = f.read()
    
    lines = content.split('\n')
    tweets = []
    start_collecting = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        match = re.search(r'^(\d{2}-[A-Za-z]{3}-\d{4}[a-z]?): (.+)', line)
        if match:
            date_id = match.group(1)
            text = match.group(2)
            
            if date_id == START_FROM:
                start_collecting = True
            
            if start_collecting:
                tweets.append({
                    "id": date_id,
                    "content": text
                })
                if len(tweets) >= limit:
                    break
    return tweets

def generate_md(tweet):
    # This is a placeholder for the logic that usually involves the AI model
    # Since I'm an agent, I will generate the fields here
    # and then write the files.
    # Note: For production, I'd normally call a helper but here I'll simulate it.
    pass

# I will actually do a loop in the next step using the AI's internal generation.
if __name__ == "__main__":
    tweets = extract_tweets(20)
    for i, t in enumerate(tweets):
        print(f"{i+1}. {t['id']}: {t['content']}")

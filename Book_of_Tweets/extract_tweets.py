import re
import os

BOOK_PATH = "Book_of_Tweets/Book6E-FINAL.md"
START_FROM = "12-Nov-2010"

def extract_tweets():
    with open(BOOK_PATH, "r") as f:
        content = f.read()
    
    # Lines starting with date format like 08-Apr-2010a:
    # but excluding those starting with X or xxx
    lines = content.split('\n')
    tweets = []
    start_collecting = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Match date pattern: DD-Mon-YYYY[a-z]?:
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
        elif start_collecting and not re.match(r'^(#|X|xxx)', line) and len(line) > 10:
             # This handles cases where a date might be missing or different format but it's part of the flow
             # However, the user said all entries marked with X are inserted.
             # The rest from 08-Apr-2010a have yet to be imported.
             pass

    return tweets

if __name__ == "__main__":
    tweets = extract_tweets()
    print(f"Extracted {len(tweets)} tweets starting from {START_FROM}.")

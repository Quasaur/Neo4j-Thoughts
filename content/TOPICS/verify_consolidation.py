import os

ROOT = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/TOPICS"

total = 0
converted = 0
missing = []

for filename in os.listdir(ROOT):
    if filename.startswith("topic-") and filename.endswith(".md"):
        total += 1
        path = os.path.join(ROOT, filename)
        with open(path, 'r') as f:
            if "```Cypher" in f.read():
                converted += 1
            else:
                missing.append(filename)

print(f"Total Files: {total}")
print(f"Converted: {converted}")
if missing:
    print(f"Missing Cypher in: {missing}")
else:
    print("All files converted successfully.")

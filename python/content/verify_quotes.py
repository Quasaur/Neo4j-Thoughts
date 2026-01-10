import os

ROOT = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/QUOTES"

total = 0
converted = 0
missing = []

for root, _, files in os.walk(ROOT):
    for filename in files:
        if filename.endswith(".md") and not filename.startswith("verify_") and not filename.startswith("consolidate_") and not filename.startswith("standardize_"):
            total += 1
            path = os.path.join(root, filename)
            with open(path, 'r') as f:
                content = f.read()
                if "```Cypher" in content:
                    converted += 1
                else:
                    missing.append(filename)

print(f"Total Quote Files: {total}")
print(f"Converted: {converted}")
if missing:
    print(f"Missing Cypher in ({len(missing)}): {missing}")
else:
    print("All quotes converted successfully.")

import os
import re
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

files = [
    "ANGER-AS-CONTAGION.md",
    "ATTENTIONS-DESIRE.md",
    "BORED-VS-BORING.md",
    "CHANGE-OTHERS-NOT-SELF.md",
    "DEFINE-APATHY.md",
    "DEFINE-HOPE.md",
    "ESSENCE-OF-JOY.md",
    "FEAR-AS-BAD-MOTIVE.md",
    "GETTING-VS-BEING.md",
    "HAPPY-IF-GOD-PLEASED.md",
    "HOLLYWOOD-VIOLENCE-PREMISE.md",
    "HONESTY-THROUGH-LOVE.md",
    "NO-ANGER-SELFLESSNESS.md",
    "NOT-LOOKING-IDIOT.md",
    "OPPORTUNITY-FOR-ANGER.md",
    "ORDERS-GIVING-TAKING.md",
    "OVERCOMING-FEAR-BLAME.md",
    "PERFECT-PEOPLE-CRITICISM.md",
    "PRIDE-IS-PRISON.md",
    "REJOICING-IN-OTHERS.md",
    "REMEMBERING-VS-LIVING-PAST.md",
    "RESPECTING-OUR-BODIES.md",
    "TERRIBLE-SECRETS.md",
    "UNREASONABLE-PEOPLE-PROBLEM.md",
    "UNREASONABLE-PRIDE.md",
    "WANTING-FORGIVENESS-ONLY.md",
    "WANTING-LOVE-ONLY.md",
    "WHISPER-OF-HOPE.md"
]

base_path = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher/"

def extract_cypher(content):
    match = re.search(r'```Cypher\s*(.*?)\s*```', content, re.DOTALL)
    if match:
        cypher = match.group(1).strip()
        # Fix quoted property keys in relationships
        cypher = re.sub(r'\{\s*"name":\s*', '{ name: ', cypher)
        # Escape double quotes in string literals
        # Find strings between : " and " ,
        cypher = re.sub(r': "([^"]*)"', lambda m: ': "' + m.group(1).replace('"', '\\"') + '"', cypher)
        return cypher
    return None

def update_neo4j_property(file_path, value):
    with open(file_path, 'r') as f:
        content = f.read()
    # Replace neo4j: false with neo4j: true
    updated = re.sub(r'neo4j: false', f'neo4j: {value}', content)
    with open(file_path, 'w') as f:
        f.write(updated)

def execute_cypher(cypher):
    statements = [s.strip() for s in cypher.split('\n\n') if s.strip() and not s.strip().startswith('//')]
    driver = GraphDatabase.driver(URI, auth=AUTH)
    try:
        with driver.session() as session:
            for stmt in statements:
                if stmt:
                    session.run(stmt)
        return True
    except Exception as e:
        print(f"Error executing Cypher: {e}")
        return False
    finally:
        driver.close()

successful = []
failed = []

for file in files:
    file_path = os.path.join(base_path, file)
    with open(file_path, 'r') as f:
        content = f.read()
    cypher = extract_cypher(content)
    if cypher:
        if execute_cypher(cypher):
            update_neo4j_property(file_path, "true")
            successful.append(file)
        else:
            failed.append(file)
    else:
        failed.append(file + " (no Cypher block)")

print("Successful files:")
for f in successful:
    print(f)

print("\nFailed files:")
for f in failed:
    print(f)
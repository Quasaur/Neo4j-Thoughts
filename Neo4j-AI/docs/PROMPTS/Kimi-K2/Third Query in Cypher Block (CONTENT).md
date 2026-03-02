# PROMPT
For both content and Book_of_Tweets folders: Examine the third query (which makes the CONTENT node the child of the primary node contained in the first CREATE query) in the Cypher block of every THOUGHT, QUOTE and PASSAGE markdown file and make corrections according to the following rules:
## Third Query: First Relationship 
### DESCRIPTION Relationship
Rule 19: The third Cypher query makes the DESCRIPTION node the child of the Cypher block's primary TOPIC node using the HAS_DESCRIPTION relationship type.

Rule 19a: The value of the "name" property of the relationship has two parts:
- the prefix "edge."
- the second part of the TOPIC node's name (.i.e., "ANTHROPOLOGY" of "topic.ANTHROPOLOGY").

Rule 19b: Following is an example of the part of the third Cypher query that contains the replationship's "name" field:
```cypher
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ANTHROPOLOGY"}]->(d);
```

### CONTENT Relationship
Rule 20: The third Cypher query makes the CONTENT node the child of the Cypher block's primary THOUGHT, QUOTE or PASSAGE node using the HAS_CONTENT relationship type.

#### THOUGHT to CONTENT
Rule 20a: The value of the "name" property of the THOUGHT to CONTENT relationship has two parts:
- the prefix "t.edge."
- the second part of the THOUGHT node's name (.i.e., "ADDICTION" of "thought.AADDICTION").

Rule 20b: Following is an example of the part of the third Cypher query that contains the replationship's "name" field:
```cypher
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ANTHROPOLOGY"}]->(d);
```

#### QUOTE to CONTENT
Rule 21a: The value of the "name" property of the QUOTE to CONTENT relationship has two parts:
- the prefix "q.edge."
- the second part of the QUOTE node's name (.i.e., "BEGOTTEN" of "quote.ANTHROPOLOGY").

Rule 21b: Following is an example of the part of the third Cypher query that contains the replationship's "name" field:
```cypher
MERGE (t)-[:HAS_DESCRIPTION {name: "q.edge.BEGOTTEN"}]->(d);
```

#### PASSAGE to CONTENT
Rule 22a: The value of the "name" property of the PASSAGE to CONTENT relationship has two parts:
- the prefix "p.edge."
- the second part of the PASSAGE node's name (.i.e., "FAITHLESSNESS" of "passage.FAITHLESSNESS").

Rule 22b: Following is an example of the part of the third Cypher query that contains the replationship's "name" field:
```cypher
MERGE (t)-[:HAS_DESCRIPTION {name: "p.edge.FAITHLESSNESS"}]->(d);
```

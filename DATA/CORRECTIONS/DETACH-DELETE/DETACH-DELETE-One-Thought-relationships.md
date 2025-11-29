```Cypher
MATCH (t:THOUGHT) WHERE t:name = 'thought.EMPTINESS' DETACH DELETE t;
```
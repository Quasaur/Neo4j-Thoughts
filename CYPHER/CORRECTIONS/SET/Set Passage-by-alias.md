```Cypher
MATCH (p:PASSAGE) WHERE p.alias = 'Passage: HONOR AND DISGRACE' 
SET p.alias = "Passage: Honor and Disgrace";
```
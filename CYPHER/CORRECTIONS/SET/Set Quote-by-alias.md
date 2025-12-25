```Cypher
MATCH (q:QUOTE) WHERE q.alias = 'Quote: Diine Miracles' 
SET q.alias = "Quote: Divine Miracles";
```
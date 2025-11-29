```Cypher
MATCH (n:TOPIC) WHERE 'cosmos' IN n.tags RETURN n;
```

OR

```Cypher
MATCH (n:TOPIC) WHERE 'cosmos' IN n.tags RETURN n.tags;
```
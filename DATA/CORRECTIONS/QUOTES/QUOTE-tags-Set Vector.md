```Cypher
MATCH (q {name: 'quote.BEGOTTEN'})
SET q.tags = ['adam'] + ['first'] + ['last'] + ['jesus_christ'] + ['begotten']
RETURN q;
```


```CYPER
MATCH (n {name: "topic.HUMANITY"})-[r]-(m)
RETURN n, r, m
```
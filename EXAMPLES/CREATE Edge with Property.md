```Cypher
MATCH (person1:Person {name: 'Alice'}), (person2:Person {name: 'Bob'})
CREATE (person1)-[:FRIENDS_WITH {since: 2020}]->(person2)
RETURN person1, person2
```
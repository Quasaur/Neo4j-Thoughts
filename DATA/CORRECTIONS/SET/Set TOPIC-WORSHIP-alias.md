```Cypher
MATCH (t:TOPIC {name: 'topic.WORSHIP'}) SET t.alias = "Topic: Obeisance" RETURN t;
```
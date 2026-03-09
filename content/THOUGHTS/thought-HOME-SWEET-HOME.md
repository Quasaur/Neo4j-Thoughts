---
type: THOUGHT
name: "thought.HOME SWEET HOME"
alias: "Thought: Home, Sweet Home"
parent: "topic.THE-GOSPEL"
en_content: "GOD is my Home...and I am His!"
tags: ["home", "sweet", "safety", "fellowship", "godhead"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HOME SWEET HOME",
    alias: "Thought: Home, Sweet Home",
    parent: "topic.THE-GOSPEL",
    tags: ["home", "sweet", "safety", "fellowship", "godhead"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HOME SWEET HOME",
    ctype: "THOUGHT",
    en_title: "Home, Sweet Home",
    en_content: "GOD is my Home...and I am His!",
    es_title: "HOGAR DULCE HOGAR",
    es_content: "DIOS es mi Hogar...y yo soy Suyo!",
    fr_title: "HOME SWEET HOME",
    fr_content: "DIEU est ma Maison... et je suis la Sienne !",
    hi_title: "मेरा प्यारा घर",
    hi_content: "ईश्वर मेरा घर है...और मैं उसका हूँ!",
    zh_title: "jiā ， tián mì de jiā",
    zh_content: "shàng dì shì wǒ de jiā …… wǒ shì tā de ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HOME SWEET HOME" AND c.name = "content.HOME SWEET HOME"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.HOME SWEET HOME"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.HOME SWEET HOME"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GOSPEL->HOME SWEET HOME"}]->(child);
```

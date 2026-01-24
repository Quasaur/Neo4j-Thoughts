---
name: "thought.HOME_SWEET_HOME"
alias: "Thought: HOME, SWEET HOME"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- home
- sweet
- safety
- fellowship
- godhead
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HOME_SWEET_HOME",
    alias: "Thought: HOME, SWEET HOME",
    parent: "topic.THE-GOSPEL",
    tags: ["home", "sweet", "safety", "fellowship", "godhead"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HOME_SWEET_HOME",
    en_title: "HOME, SWEET HOME",
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
WHERE t.name = "thought.HOME_SWEET_HOME" AND c.name = "content.HOME_SWEET_HOME"
MERGE (t)-[:HAS_CONTENT {name: "edge.HOME_SWEET_HOME"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.HOME_SWEET_HOME"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GOSPEL->HOME_SWEET_HOME"}]->(child);
```

---
type: THOUGHT
name: "thought.HAPPY SABBATH"
alias: "Thought: Happy Sabbath"
parent: "topic.CREATION"
en_content: "Happy Sabbath, Earth!"
tags: ["happy", "sabbath", "earth", "creation", "rest"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HAPPY SABBATH",
    alias: "Thought: Happy Sabbath",
    parent: "topic.CREATION",
    tags: ["happy", "sabbath", "earth", "creation", "rest"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HAPPY SABBATH",
    ctype: "THOUGHT",
    en_title: "Happy Sabbath",
    en_content: "Happy Sabbath, Earth!",
    es_title: "FELIZ SÁBADO",
    es_content: "¡Feliz sábado, Tierra!",
    fr_title: "JOYEUX SABBAT",
    fr_content: "Joyeux sabbat, Terre !",
    hi_title: "शुभ सब्बाथ",
    hi_content: "शुभ सब्बाथ, पृथ्वी!",
    zh_title: "ān xī rì kuài lè",
    zh_content: "ān xī rì kuài lè ， dì qiú ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HAPPY SABBATH" AND c.name = "content.HAPPY SABBATH"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.HAPPY SABBATH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.HAPPY SABBATH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.CREATION->HAPPY SABBATH"}]->(child);
```

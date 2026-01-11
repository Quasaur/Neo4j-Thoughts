---
name: "thought.HAPPY_SABBATH"
alias: "Thought: HAPPY SABBATH"
type: THOUGHT
parent: topic.CREATION
tags:
- happy
- sabbath
- earth
- creation
- rest
neo4j: true
ptopic: "[[topic-CREATION]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HAPPY_SABBATH",
    alias: "Thought: HAPPY SABBATH",
    parent: "topic.CREATION",
    tags: ["happy", "sabbath", "earth", "creation", "rest"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HAPPY_SABBATH",
    en_title: "HAPPY SABBATH",
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
WHERE t.name = "thought.HAPPY_SABBATH" AND c.name = "content.HAPPY_SABBATH"
MERGE (t)-[:HAS_CONTENT {name: "edge.HAPPY_SABBATH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.HAPPY_SABBATH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->HAPPY_SABBATH"}]->(child);
```

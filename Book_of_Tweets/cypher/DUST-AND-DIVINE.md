---
name: "thought.DUST AND DIVINE"
alias: "Thought: Image of God"
type: THOUGHT
en_content: "We are dust...that look like God."
parent: "topic.HUMANITY"
tags:
- humanity
- creation
- dust
- divine_image
- paradox
level: 3
neo4j: true
insert: true
---
# Dust and Divine

> [!Thought-en]
> We are dust...that look like God.

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DUST AND DIVINE",
    alias: "Thought: Image of God",
    parent: "topic.HUMANITY",
    tags: ["humanity", "creation", "dust", "divine_image", "paradox"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DUST AND DIVINE",
    en_title: "Dust and Divine",
    en_content: "We are dust...that look like God.",
    es_title: "Polvo y divino",
    es_content: "Somos polvo... que se parece a Dios.",
    fr_title: "Poussière et divin",
    fr_content: "Nous sommes de la poussière... qui ressemble à Dieu.",
    hi_title: "dhuool aur divy",
    hi_content: "हम धूल हैं... जो भगवान की तरह दिखते हैं।",
    zh_title: "chén āi yǔ shén shèng",
    zh_content: "wǒ men shì chén āi... què xiàng shàng dì."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DUST AND DIVINE" AND c.name = "content.DUST AND DIVINE"
MERGE (t)-[:HAS_CONTENT {name: "edge.DUST AND DIVINE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.DUST AND DIVINE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMANITY >DUST AND DIVINE"}]->(child);
```

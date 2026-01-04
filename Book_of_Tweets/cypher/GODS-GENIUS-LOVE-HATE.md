---
name: "thought.GODS GENIUS LOVE HATE"
alias: "Thought: Gods Genius Love Hate"
type: THOUGHT
en_content: "What identifies God's Genius is the ability to hate evil while simultaneously loving evil people."
parent: "topic.THE GODHEAD"
tags:
- genius
- love
- hate
- evil
- divinity
level: 1
neo4j: true
insert: true
---
# Gods Genius Love Hate

> [!Thought-en]
> What identifies God's Genius is the ability to hate evil while simultaneously loving evil people.

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013c)
CREATE (t:THOUGHT {
    name: "thought.GODS GENIUS LOVE HATE",
    alias: "Thought: Gods Genius Love Hate",
    parent: "topic.THE GODHEAD",
    tags: ['genius', 'love', 'hate', 'evil', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS GENIUS LOVE HATE",
    en_title: "Gods Genius Love Hate",
    en_content: "What identifies God's Genius is the ability to hate evil while simultaneously loving evil people.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GODS GENIUS LOVE HATE" AND c.name = "content.GODS GENIUS LOVE HATE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS GENIUS LOVE HATE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS GENIUS LOVE HATE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS GENIUS LOVE HATE" }]->(child);
```
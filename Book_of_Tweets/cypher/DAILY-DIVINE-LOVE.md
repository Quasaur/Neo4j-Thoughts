---
name: "thought.DAILY DIVINE LOVE"
alias: "Thought: Daily Divine Love"
type: THOUGHT
en_content: "Though I may deserve Wrath I still need Love...and God gives me His Love every morning!"
parent: "topic.GRACE"
tags:
- love
- grace
- wrath
- morning
- god
level: 3
neo4j: true
insert: true
---
# Daily Divine Love

> [!Thought-en]
> Though I may deserve Wrath I still need Love...and God gives me His Love every morning!

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jun-2012b)
CREATE (t:THOUGHT {
    name: "thought.DAILY DIVINE LOVE",
    alias: "Thought: Daily Divine Love",
    parent: "topic.GRACE",
    tags: ['love', 'grace', 'wrath', 'morning', 'god'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DAILY DIVINE LOVE",
    en_title: "Daily Divine Love",
    en_content: "Though I may deserve Wrath I still need Love...and God gives me His Love every morning!",
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
WHERE t.name = "thought.DAILY DIVINE LOVE" AND c.name = "content.DAILY DIVINE LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DAILY DIVINE LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.DAILY DIVINE LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >DAILY DIVINE LOVE" }]->(child);
```
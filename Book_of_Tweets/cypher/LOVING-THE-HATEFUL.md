---
name: "thought.LOVING THE HATEFUL"
alias: "Thought: Loving The Hateful"
type: THOUGHT
en_content: "Loving the hateful... how does God do it? How can I do it?"
parent: "topic.THE GODHEAD"
tags:
- love
- hate
- character
- god
- divinity
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2013b)
CREATE (t:THOUGHT {
    name: "thought.LOVING THE HATEFUL",
    alias: "Thought: Loving The Hateful",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'hate', 'character', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.LOVING THE HATEFUL",
    en_title: "Loving The Hateful",
    en_content: "Loving the hateful... how does God do it? How can I do it?",
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
WHERE t.name = "thought.LOVING THE HATEFUL" AND c.name = "content.LOVING THE HATEFUL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVING THE HATEFUL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.LOVING THE HATEFUL"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >LOVING THE HATEFUL" }]->(child);
```

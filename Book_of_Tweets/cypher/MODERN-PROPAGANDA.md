---
name: "thought.MODERN PROPAGANDA"
alias: "Thought: Modern Propaganda"
type: THOUGHT
en_content: "Modern Propaganda (good vampires, pious werewolves, virtuous mediums) has perpetuated humanity's slide into Satan's occult domain."
parent: "topic.EVIL"
tags:
- evil
- propaganda
- occult
- deception
- discernment
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2010a)
CREATE (t:THOUGHT {
    name: "thought.MODERN PROPAGANDA",
    alias: "Thought: Modern Propaganda",
    parent: "topic.EVIL",
    tags: ['evil', 'propaganda', 'occult', 'deception', 'discernment'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.MODERN PROPAGANDA",
    en_title: "Modern Propaganda",
    en_content: "Modern Propaganda (good vampires, pious werewolves, virtuous mediums) has perpetuated humanity's slide into Satan's occult domain.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MODERN PROPAGANDA" AND c.name = "content.MODERN PROPAGANDA"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MODERN PROPAGANDA" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.MODERN PROPAGANDA"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >MODERN PROPAGANDA" }]->(child);
```

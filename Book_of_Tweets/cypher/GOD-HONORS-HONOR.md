---
name: "thought.GOD HONORS HONOR"
alias: "Thought: God Honors Honor"
type: THOUGHT
en_content: "God is not stupid; He honors those who honor Him...those who ignore Him are lightly esteemed."
parent: "topic.THE GODHEAD"
tags:
- god
- honor
- justice
- truth
- reverence
level: 1
neo4j: true
insert: true
---
# God Honors Honor

> [!Thought-en]
> God is not stupid; He honors those who honor Him...those who ignore Him are lightly esteemed.

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.GOD HONORS HONOR",
    alias: "Thought: God Honors Honor",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'honor', 'justice', 'truth', 'reverence'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD HONORS HONOR",
    en_title: "God Honors Honor",
    en_content: "God is not stupid; He honors those who honor Him...those who ignore Him are lightly esteemed.",
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
WHERE t.name = "thought.GOD HONORS HONOR" AND c.name = "content.GOD HONORS HONOR"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD HONORS HONOR" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD HONORS HONOR"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD HONORS HONOR" }]->(child);
```
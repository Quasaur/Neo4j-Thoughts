---
name: "thought.PROVING CREATION"
alias: "Thought: Proving Creation"
type: THOUGHT
en_content: "\"In The Beginning God created the heavens and the Earth.\" -- Genesis 1:1 There's not a soul on the planet that can prove otherwise."
parent: "topic.CREATION"
tags:
- creation
- truth
- bible
- science
- origin
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jan-2012b)
CREATE (t:THOUGHT {
    name: "thought.PROVING CREATION",
    alias: "Thought: Proving Creation",
    parent: "topic.CREATION",
    tags: ['creation', 'truth', 'bible', 'science', 'origin'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PROVING CREATION",
    en_title: "Proving Creation",
    en_content: "\"In The Beginning God created the heavens and the Earth.\" -- Genesis 1:1 There's not a soul on the planet that can prove otherwise.",
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
WHERE t.name = "thought.PROVING CREATION" AND c.name = "content.PROVING CREATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PROVING CREATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.PROVING CREATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >PROVING CREATION" }]->(child);
```

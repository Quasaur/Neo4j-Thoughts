---
name: "thought.HORDES OF THE ABYSS"
alias: "Thought: Hordes Of The Abyss"
type: THOUGHT
en_content: "Humanity will be visited by the hordes of the Abyss because that is what it, by its deeds, asked for."
parent: "topic.EVIL"
tags:
- abyss
- hordes
- deeds
- judgment
- evil
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013d)
CREATE (t:THOUGHT {
    name: "thought.HORDES OF THE ABYSS",
    alias: "Thought: Hordes Of The Abyss",
    parent: "topic.EVIL",
    tags: ['abyss', 'hordes', 'deeds', 'judgment', 'evil'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HORDES OF THE ABYSS",
    en_title: "Hordes Of The Abyss",
    en_content: "Humanity will be visited by the hordes of the Abyss because that is what it, by its deeds, asked for.",
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
WHERE t.name = "thought.HORDES OF THE ABYSS" AND c.name = "content.HORDES OF THE ABYSS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HORDES OF THE ABYSS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.HORDES OF THE ABYSS"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >HORDES OF THE ABYSS" }]->(child);
```

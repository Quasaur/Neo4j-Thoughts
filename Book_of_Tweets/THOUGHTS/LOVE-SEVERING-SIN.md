---
name: "thought.LOVE SEVERING SIN"
alias: "Thought: Love Severing Sin"
type: THOUGHT
en_content: "Only Love can separate sinners from their sins."
parent: "topic.GRACE"
tags:
- love
- sin
- separation
- grace
- transformation
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Jan-2012b)
CREATE (t:THOUGHT {
    name: "thought.LOVE SEVERING SIN",
    alias: "Thought: Love Severing Sin",
    parent: "topic.GRACE",
    tags: ['love', 'sin', 'separation', 'grace', 'transformation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LOVE SEVERING SIN",
    en_title: "Love Severing Sin",
    en_content: "Only Love can separate sinners from their sins.",
    es_title: "El Amor Separando el Pecado",
    es_content: "Sólo el Amor puede separar a los pecadores de sus pecados.",
    fr_title: "L'Amour Séparant le Péché",
    fr_content: "Seul l'Amour peut séparer les pécheurs de leurs péchés.",
    hi_title: "प्रेम पाप को अलग करता है",
    hi_content: "केवल प्रेम ही पापियों को उनके पापों से अलग कर सकता है।",
    zh_title: "Ài Gēduàn Zuì'è",
    zh_content: "Wéiyǒu Ài néng jiāng zuìrén cóng tāmen de zuì'è zhōng fēnlí."
});

MATCH (t:THOUGHT {name: "thought.LOVE SEVERING SIN"})
MATCH (c:CONTENT {name: "content.LOVE SEVERING SIN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVE SEVERING SIN" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.LOVE SEVERING SIN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LOVE SEVERING SIN" }]->(child);
```

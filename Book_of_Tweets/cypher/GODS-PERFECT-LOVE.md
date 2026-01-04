---
name: "thought.GODS PERFECT LOVE"
alias: "Thought: Gods Perfect Love"
type: THOUGHT
en_content: "God loves us with ALL His Heart, Soul, Mind and Strength!"
parent: "topic.THE GODHEAD"
tags:
- love
- god
- devotion
- majesty
- heart
level: 1
neo4j: true
insert: true
---
# Gods Perfect Love

> [!Thought-en]
> God loves us with ALL His Heart, Soul, Mind and Strength!

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jan-2012c)
CREATE (t:THOUGHT {
    name: "thought.GODS PERFECT LOVE",
    alias: "Thought: Gods Perfect Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'god', 'devotion', 'majesty', 'heart'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS PERFECT LOVE",
    en_title: "Gods Perfect Love",
    en_content: "God loves us with ALL His Heart, Soul, Mind and Strength!",
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
WHERE t.name = "thought.GODS PERFECT LOVE" AND c.name = "content.GODS PERFECT LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS PERFECT LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS PERFECT LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS PERFECT LOVE" }]->(child);
```
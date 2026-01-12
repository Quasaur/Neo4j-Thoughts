---
name: "thought.BOUNTIFUL EYE"
alias: "Thought: Bountiful Eye"
type: THOUGHT
en_content: "Whoever has a bountiful eye will be blessed, for he shares his bread with the poor. Proverbs 22:9, ESV"
parent: "topic.MORALITY"
tags:
- blessing
- generosity
- poor
- morality
- character
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.BOUNTIFUL EYE",
    alias: "Thought: Bountiful Eye",
    parent: "topic.MORALITY",
    tags: ['blessing', 'generosity', 'poor', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BOUNTIFUL EYE",
    en_title: "Bountiful Eye",
    en_content: "Whoever has a bountiful eye will be blessed, for he shares his bread with the poor. Proverbs 22:9, ESV",
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
WHERE t.name = "thought.BOUNTIFUL EYE" AND c.name = "content.BOUNTIFUL EYE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BOUNTIFUL EYE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.BOUNTIFUL EYE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >BOUNTIFUL EYE" }]->(child);
```

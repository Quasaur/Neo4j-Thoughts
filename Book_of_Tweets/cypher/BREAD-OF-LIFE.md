---
name: "thought.BREAD OF LIFE"
alias: "Thought: Bread Of Life"
type: THOUGHT
en_content: "We overeat in our attempt to feed our starving spirit with natural food instead of The BREAD of LIFE which is Christ."
parent: "topic.THE GODHEAD"
tags:
- christ
- bread
- life
- overeat
- spirit
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Apr-2012a)
CREATE (t:THOUGHT {
    name: "thought.BREAD OF LIFE",
    alias: "Thought: Bread Of Life",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'bread', 'life', 'overeat', 'spirit'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.BREAD OF LIFE",
    en_title: "Bread Of Life",
    en_content: "We overeat in our attempt to feed our starving spirit with natural food instead of The BREAD of LIFE which is Christ.",
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
WHERE t.name = "thought.BREAD OF LIFE" AND c.name = "content.BREAD OF LIFE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BREAD OF LIFE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.BREAD OF LIFE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >BREAD OF LIFE" }]->(child);
```

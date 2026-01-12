---
name: "thought.GOD HAS SENSE"
alias: "Thought: God Has Sense"
type: THOUGHT
en_content: "God has sense: if you talk to Him He'll talk to you; if you listen to Him He'll listen to you; if you'll honor Him He'll honor you."
parent: "topic.SPIRITUALITY"
tags:
- relationship
- communication
- honor
- spirituality
- god
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Nov-2011a)
CREATE (t:THOUGHT {
    name: "thought.GOD HAS SENSE",
    alias: "Thought: God Has Sense",
    parent: "topic.SPIRITUALITY",
    tags: ['relationship', 'communication', 'honor', 'spirituality', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD HAS SENSE",
    en_title: "God Has Sense",
    en_content: "God has sense: if you talk to Him He'll talk to you; if you listen to Him He'll listen to you; if you'll honor Him He'll honor you.",
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
WHERE t.name = "thought.GOD HAS SENSE" AND c.name = "content.GOD HAS SENSE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD HAS SENSE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.GOD HAS SENSE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >GOD HAS SENSE" }]->(child);
```

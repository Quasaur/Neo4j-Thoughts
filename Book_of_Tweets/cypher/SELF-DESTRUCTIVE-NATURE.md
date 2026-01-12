---
name: "thought.SELF DESTRUCTIVE NATURE"
alias: "Thought: Self Destructive Nature"
type: THOUGHT
en_content: "We are self-destructive by nature and teach our children to be self-destructive."
parent: "topic.HUMANITY"
tags:
- humanity
- children
- destruction
- nature
- character
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013c)
CREATE (t:THOUGHT {
    name: "thought.SELF DESTRUCTIVE NATURE",
    alias: "Thought: Self Destructive Nature",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'children', 'destruction', 'nature', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SELF DESTRUCTIVE NATURE",
    en_title: "Self Destructive Nature",
    en_content: "We are self-destructive by nature and teach our children to be self-destructive.",
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
WHERE t.name = "thought.SELF DESTRUCTIVE NATURE" AND c.name = "content.SELF DESTRUCTIVE NATURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SELF DESTRUCTIVE NATURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.SELF DESTRUCTIVE NATURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >SELF DESTRUCTIVE NATURE" }]->(child);
```

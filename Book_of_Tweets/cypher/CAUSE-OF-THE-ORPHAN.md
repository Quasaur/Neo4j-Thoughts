---
name: "thought.CAUSE OF THE ORPHAN"
alias: "Thought: Cause Of The Orphan"
type: THOUGHT
en_content: "\"They do not plead the cause, (The cause of the orphan), THAT THEY MAY PROSPER; And they do not defend the rights of the poor.\" -- Jeremiah"
parent: "topic.MORALITY"
tags:
- justice
- orphan
- poor
- morality
- prophet
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.CAUSE OF THE ORPHAN",
    alias: "Thought: Cause Of The Orphan",
    parent: "topic.MORALITY",
    tags: ['justice', 'orphan', 'poor', 'morality', 'prophet'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CAUSE OF THE ORPHAN",
    en_title: "Cause Of The Orphan",
    en_content: "\"They do not plead the cause, (The cause of the orphan), THAT THEY MAY PROSPER; And they do not defend the rights of the poor.\" -- Jeremiah",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CAUSE OF THE ORPHAN" AND c.name = "content.CAUSE OF THE ORPHAN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CAUSE OF THE ORPHAN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CAUSE OF THE ORPHAN"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CAUSE OF THE ORPHAN" }]->(child);
```

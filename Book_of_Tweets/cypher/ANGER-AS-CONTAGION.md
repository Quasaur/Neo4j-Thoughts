---
name: "thought.ANGER AS CONTAGION"
alias: "Thought: Anger As Contagion"
type: THOUGHT
en_content: "Anger is a contagion that easily leaps from soul to soul where there is an absence of reason."
parent: "topic.ATTITUDE"
tags:
- anger
- reason
- soul
- attitude
- character
level: 2
neo4j: true
insert: true
---
# Anger As Contagion

> [!Thought-en]
> Anger is a contagion that easily leaps from soul to soul where there is an absence of reason.

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2012a)
CREATE (t:THOUGHT {
    name: "thought.ANGER AS CONTAGION",
    alias: "Thought: Anger As Contagion",
    parent: "topic.ATTITUDE",
    tags: ['anger', 'reason', 'soul', 'attitude', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ANGER AS CONTAGION",
    en_title: "Anger As Contagion",
    en_content: "Anger is a contagion that easily leaps from soul to soul where there is an absence of reason.",
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
WHERE t.name = "thought.ANGER AS CONTAGION" AND c.name = "content.ANGER AS CONTAGION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ANGER AS CONTAGION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ANGER AS CONTAGION"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >ANGER AS CONTAGION" }]->(child);
```
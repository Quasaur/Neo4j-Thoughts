---
name: "thought.PRAYER BEFORE SPEECH"
alias: "Thought: Prayer Before Speech"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- prayer
- speech
- spirituality
- integrity
- character
level: 2
neo4j: true
insert: true
---
# Prayer Before Speech

> [!Thought-en]
> It is inappropriate to speak out on what we don't pray out.

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Aug-2012a)
CREATE (t:THOUGHT {
    name: "thought.PRAYER BEFORE SPEECH",
    alias: "Thought: Prayer Before Speech",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'speech', 'spirituality', 'integrity', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER BEFORE SPEECH",
    en_title: "Prayer Before Speech",
    en_content: "It is inappropriate to speak out on what we don't pray out.",
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
WHERE t.name = "thought.PRAYER BEFORE SPEECH" AND c.name = "content.PRAYER BEFORE SPEECH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER BEFORE SPEECH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER BEFORE SPEECH"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER BEFORE SPEECH" }]->(child);
```
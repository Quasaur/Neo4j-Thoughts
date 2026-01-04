---
name: "thought.FEAR AS BAD MOTIVE"
alias: "Thought: Fear As Bad Motive"
type: THOUGHT
en_content: "Fear is rarely a good motive for any action."
parent: "topic.ATTITUDE"
tags:
- fear
- motive
- action
- attitude
- character
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.FEAR AS BAD MOTIVE",
    alias: "Thought: Fear As Bad Motive",
    parent: "topic.ATTITUDE",
    tags: ['fear', 'motive', 'action', 'attitude', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FEAR AS BAD MOTIVE",
    en_title: "Fear As Bad Motive",
    en_content: "Fear is rarely a good motive for any action.",
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
WHERE t.name = "thought.FEAR AS BAD MOTIVE" AND c.name = "content.FEAR AS BAD MOTIVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FEAR AS BAD MOTIVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.FEAR AS BAD MOTIVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >FEAR AS BAD MOTIVE" }]->(child);
```

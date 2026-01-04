---
name: "thought.NOT LOOKING IDIOT"
alias: "Thought: Not Looking Idiot"
type: THOUGHT
en_content: "I don't mind being an idiot, just looking like one."
parent: "topic.ATTITUDE"
tags:
- idiot
- appearance
- attitude
- character
level: 2
neo4j: true
insert: true
---
# Not Looking Idiot

> [!Thought-en]
> I don't mind being an idiot, just looking like one.

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.NOT LOOKING IDIOT",
    alias: "Thought: Not Looking Idiot",
    parent: "topic.ATTITUDE",
    tags: ['idiot', 'appearance', 'attitude', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NOT LOOKING IDIOT",
    en_title: "Not Looking Idiot",
    en_content: "I don't mind being an idiot, just looking like one.",
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
WHERE t.name = "thought.NOT LOOKING IDIOT" AND c.name = "content.NOT LOOKING IDIOT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOT LOOKING IDIOT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.NOT LOOKING IDIOT"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >NOT LOOKING IDIOT" }]->(child);
```
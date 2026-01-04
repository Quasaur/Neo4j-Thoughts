---
name: "thought.AMERICA CHEATS ITSELF"
alias: "Thought: America Cheats Itself"
type: THOUGHT
en_content: "America is a nation that CHEATS ITSELF out of its own money."
parent: "topic.MORALITY"
tags:
- america
- economy
- greed
- morality
- society
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.AMERICA CHEATS ITSELF",
    alias: "Thought: America Cheats Itself",
    parent: "topic.MORALITY",
    tags: ['america', 'economy', 'greed', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AMERICA CHEATS ITSELF",
    en_title: "America Cheats Itself",
    en_content: "America is a nation that CHEATS ITSELF out of its own money.",
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
WHERE t.name = "thought.AMERICA CHEATS ITSELF" AND c.name = "content.AMERICA CHEATS ITSELF"
MERGE (t)-[:HAS_CONTENT { "name": "edge.AMERICA CHEATS ITSELF" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.AMERICA CHEATS ITSELF"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >AMERICA CHEATS ITSELF" }]->(child);
```

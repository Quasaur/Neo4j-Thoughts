---
name: "thought.FAMILIAR SPIRITS WARNING"
alias: "Thought: Familiar Spirits Warning"
type: THOUGHT
en_content: "\"You do not turn nor seek to those having familiar spirits nor necromancers to be unclean by them; I am YHWH your God.\" -- Leviticus 19:31"
parent: "topic.EVIL"
tags:
- occult
- spirits
- evil
- law
- bible
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.FAMILIAR SPIRITS WARNING",
    alias: "Thought: Familiar Spirits Warning",
    parent: "topic.EVIL",
    tags: ['occult', 'spirits', 'evil', 'law', 'bible'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FAMILIAR SPIRITS WARNING",
    en_title: "Familiar Spirits Warning",
    en_content: "\"You do not turn nor seek to those having familiar spirits nor necromancers to be unclean by them; I am YHWH your God.\" -- Leviticus 19:31",
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
WHERE t.name = "thought.FAMILIAR SPIRITS WARNING" AND c.name = "content.FAMILIAR SPIRITS WARNING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAMILIAR SPIRITS WARNING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.FAMILIAR SPIRITS WARNING"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >FAMILIAR SPIRITS WARNING" }]->(child);
```

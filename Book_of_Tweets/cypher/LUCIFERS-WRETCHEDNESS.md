---
name: "thought.LUCIFERS WRETCHEDNESS"
alias: "Thought: Lucifers Wretchedness"
type: THOUGHT
en_content: "What a wretch Lucifer must be, to despise his most ardent Supporter!"
parent: "topic.EVIL"
tags:
- lucifer
- pride
- evil
- supporter
- character
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.LUCIFERS WRETCHEDNESS",
    alias: "Thought: Lucifers Wretchedness",
    parent: "topic.EVIL",
    tags: ['lucifer', 'pride', 'evil', 'supporter', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LUCIFERS WRETCHEDNESS",
    en_title: "Lucifers Wretchedness",
    en_content: "What a wretch Lucifer must be, to despise his most ardent Supporter!",
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
WHERE t.name = "thought.LUCIFERS WRETCHEDNESS" AND c.name = "content.LUCIFERS WRETCHEDNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LUCIFERS WRETCHEDNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.LUCIFERS WRETCHEDNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >LUCIFERS WRETCHEDNESS" }]->(child);
```

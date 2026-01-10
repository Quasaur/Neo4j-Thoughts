---
name: "thought.CONGRESS NOT OURS"
alias: "Thought: Congress Not Ours"
type: THOUGHT
en_content: "The United States Congress no longer belongs to the American People."
parent: "topic.MORALITY"
tags:
- congress
- america
- people
- morality
- ownership
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.CONGRESS NOT OURS",
    alias: "Thought: Congress Not Ours",
    parent: "topic.MORALITY",
    tags: ['congress', 'america', 'people', 'morality', 'ownership'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONGRESS NOT OURS",
    en_title: "Congress Not Ours",
    en_content: "The United States Congress no longer belongs to the American People.",
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
WHERE t.name = "thought.CONGRESS NOT OURS" AND c.name = "content.CONGRESS NOT OURS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CONGRESS NOT OURS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CONGRESS NOT OURS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CONGRESS NOT OURS" }]->(child);
```

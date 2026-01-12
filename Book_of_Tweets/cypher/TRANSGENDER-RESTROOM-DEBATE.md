---
name: "thought.TRANSGENDER RESTROOM DEBATE"
alias: "Thought: Transgender Restroom Debate"
type: THOUGHT
en_content: "A bill that lets a transgendered male into a girls' restroom is one thing; getting that male past the girl's father is another."
parent: "topic.MORALITY"
tags:
- morality
- gender
- society
- father
- safety
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.TRANSGENDER RESTROOM DEBATE",
    alias: "Thought: Transgender Restroom Debate",
    parent: "topic.MORALITY",
    tags: ['morality', 'gender', 'society', 'father', 'safety'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TRANSGENDER RESTROOM DEBATE",
    en_title: "Transgender Restroom Debate",
    en_content: "A bill that lets a transgendered male into a girls' restroom is one thing; getting that male past the girl's father is another.",
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
WHERE t.name = "thought.TRANSGENDER RESTROOM DEBATE" AND c.name = "content.TRANSGENDER RESTROOM DEBATE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRANSGENDER RESTROOM DEBATE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.TRANSGENDER RESTROOM DEBATE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >TRANSGENDER RESTROOM DEBATE" }]->(child);
```

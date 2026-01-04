---
name: "thought.TALKING TO PEOPLE"
alias: "Thought: Talking To People"
type: THOUGHT
en_content: "If you don't know how to talk to people, you probably shouldn't talk to people."
parent: "topic.WISDOM"
tags:
- communication
- wisdom
- social_skills
- discernment
- relationships
level: 3
neo4j: true
insert: true
---
# Talking To People

> [!Thought-en]
> If you don't know how to talk to people, you probably shouldn't talk to people.

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.TALKING TO PEOPLE",
    alias: "Thought: Talking To People",
    parent: "topic.WISDOM",
    tags: ["communication", "wisdom", "social_skills", "discernment", "relationships"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TALKING TO PEOPLE",
    en_title: "Talking To People",
    en_content: "If you don't know how to talk to people, you probably shouldn't talk to people.",
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
WHERE t.name = "thought.TALKING TO PEOPLE" AND c.name = "content.TALKING TO PEOPLE"
MERGE (t)-[:HAS_CONTENT {name: "edge.TALKING TO PEOPLE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.TALKING TO PEOPLE"
MERGE (parent)-[:HAS_THOUGHT {name: "WISDOM >TALKING TO PEOPLE"}]->(child);
```

---
name: "thought.HOLLYWOOD VIOLENCE PREMISE"
alias: "Thought: Hollywood Violence Premise"
type: THOUGHT
en_content: "The original premise of Hollywood violence was \"If they're watching violence they're not committing it.\"...Oops!"
parent: "topic.ATTITUDE"
tags:
- violence
- society
- media
- attitude
- failure
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jan-2013)
CREATE (t:THOUGHT {
    name: "thought.HOLLYWOOD VIOLENCE PREMISE",
    alias: "Thought: Hollywood Violence Premise",
    parent: "topic.ATTITUDE",
    tags: ['violence', 'society', 'media', 'attitude', 'failure'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HOLLYWOOD VIOLENCE PREMISE",
    en_title: "Hollywood Violence Premise",
    en_content: "The original premise of Hollywood violence was \"If they're watching violence they're not committing it.\"...Oops!",
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
WHERE t.name = "thought.HOLLYWOOD VIOLENCE PREMISE" AND c.name = "content.HOLLYWOOD VIOLENCE PREMISE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HOLLYWOOD VIOLENCE PREMISE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HOLLYWOOD VIOLENCE PREMISE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >HOLLYWOOD VIOLENCE PREMISE" }]->(child);
```

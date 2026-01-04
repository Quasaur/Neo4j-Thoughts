---
name: "thought.HELL AND HYPOCRISY"
alias: "Thought: Hell And Hypocrisy"
type: THOUGHT
en_content: "If I send you to Hell, it's guaranteed that I will be following you shortly."
parent: "topic.MORALITY"
tags:
- judgment
- hypocrisy
- hell
- morality
- character
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Dec-2011b)
CREATE (t:THOUGHT {
    name: "thought.HELL AND HYPOCRISY",
    alias: "Thought: Hell And Hypocrisy",
    parent: "topic.MORALITY",
    tags: ['judgment', 'hypocrisy', 'hell', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HELL AND HYPOCRISY",
    en_title: "Hell And Hypocrisy",
    en_content: "If I send you to Hell, it's guaranteed that I will be following you shortly.",
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
WHERE t.name = "thought.HELL AND HYPOCRISY" AND c.name = "content.HELL AND HYPOCRISY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HELL AND HYPOCRISY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.HELL AND HYPOCRISY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >HELL AND HYPOCRISY" }]->(child);
```

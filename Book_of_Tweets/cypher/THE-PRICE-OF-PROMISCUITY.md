---
name: "thought.THE PRICE OF PROMISCUITY"
alias: "Thought: The Price Of Promiscuity"
type: THOUGHT
en_content: "People who are promiscuous wind up paying a terrible price."
parent: "topic.MORALITY"
tags:
- morality
- purity
- consequences
- society
- character
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Nov-2011c)
CREATE (t:THOUGHT {
    name: "thought.THE PRICE OF PROMISCUITY",
    alias: "Thought: The Price Of Promiscuity",
    parent: "topic.MORALITY",
    tags: ['morality', 'purity', 'consequences', 'society', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.THE PRICE OF PROMISCUITY",
    en_title: "The Price Of Promiscuity",
    en_content: "People who are promiscuous wind up paying a terrible price.",
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
WHERE t.name = "thought.THE PRICE OF PROMISCUITY" AND c.name = "content.THE PRICE OF PROMISCUITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE PRICE OF PROMISCUITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.THE PRICE OF PROMISCUITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >THE PRICE OF PROMISCUITY" }]->(child);
```

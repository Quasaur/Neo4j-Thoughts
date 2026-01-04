---
name: "thought.WAY OF EMPIRES"
alias: "Thought: Way Of Empires"
type: THOUGHT
en_content: "We are going the way of the Roman Empire and the Soviet Union."
parent: "topic.HUMANITY"
tags:
- history
- humanity
- fall
- society
- judgment
level: 3
neo4j: true
insert: true
---
# Way Of Empires

> [!Thought-en]
> We are going the way of the Roman Empire and the Soviet Union.

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.WAY OF EMPIRES",
    alias: "Thought: Way Of Empires",
    parent: "topic.HUMANITY",
    tags: ['history', 'humanity', 'fall', 'society', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WAY OF EMPIRES",
    en_title: "Way Of Empires",
    en_content: "We are going the way of the Roman Empire and the Soviet Union.",
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
WHERE t.name = "thought.WAY OF EMPIRES" AND c.name = "content.WAY OF EMPIRES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WAY OF EMPIRES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.WAY OF EMPIRES"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >WAY OF EMPIRES" }]->(child);
```
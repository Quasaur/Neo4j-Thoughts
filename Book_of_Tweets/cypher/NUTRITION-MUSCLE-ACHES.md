---
name: "thought.NUTRITION MUSCLE ACHES"
alias: "Thought: Nutrition Muscle Aches"
type: THOUGHT
en_content: "Nutrition: Muscle aches may benefit from the following: Astaxanthin, Calcium, Magnesium, Bromelain, Creatine."
parent: "topic.CREATION"
tags:
- creation
- health
- nutrition
- biology
- body
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.NUTRITION MUSCLE ACHES",
    alias: "Thought: Nutrition Muscle Aches",
    parent: "topic.CREATION",
    tags: ['creation', 'health', 'nutrition', 'biology', 'body'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NUTRITION MUSCLE ACHES",
    en_title: "Nutrition Muscle Aches",
    en_content: "Nutrition: Muscle aches may benefit from the following: Astaxanthin, Calcium, Magnesium, Bromelain, Creatine.",
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
WHERE t.name = "thought.NUTRITION MUSCLE ACHES" AND c.name = "content.NUTRITION MUSCLE ACHES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NUTRITION MUSCLE ACHES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.NUTRITION MUSCLE ACHES"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >NUTRITION MUSCLE ACHES" }]->(child);
```

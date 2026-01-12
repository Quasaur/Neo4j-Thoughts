---
name: "thought.QUESTIONING GODS EXISTENCE"
alias: "Thought: Questioning Gods Existence"
type: THOUGHT
en_content: "In a perverse generation they question God's Existence, when it's their existence and survival that has a question mark behind them."
parent: "topic.PHILOSOPHY"
tags:
- existence
- god
- survival
- skepticism
- philosophy
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Aug-2012b)
CREATE (t:THOUGHT {
    name: "thought.QUESTIONING GODS EXISTENCE",
    alias: "Thought: Questioning Gods Existence",
    parent: "topic.PHILOSOPHY",
    tags: ['existence', 'god', 'survival', 'skepticism', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.QUESTIONING GODS EXISTENCE",
    en_title: "Questioning Gods Existence",
    en_content: "In a perverse generation they question God's Existence, when it's their existence and survival that has a question mark behind them.",
    es_title: "Cuestionando la Existencia de Dios",
    es_content: "En una generación perversa cuestionan la Existencia de Dios, cuando es su existencia y supervivencia la que tiene un signo de interrogación detrás de ellas.",
    fr_title: "Questionner l'Existence de Dieu",
    fr_content: "Dans une génération perverse, ils questionnent l'Existence de Dieu, alors que c'est leur existence et leur survie qui ont un point d'interrogation derrière elles.",
    hi_title: "ईश्वर के अस्तित्व पर प्रश्न उठाना",
    hi_content: "एक भ्रष्ट पीढ़ी में वे ईश्वर के अस्तित्व पर प्रश्न उठाते हैं, जबकि उनके अस्तित्व और जीवित रहने के पीछे ही प्रश्नचिह्न लगा है।",
    zh_title: "Zhiyi Shangdi de Cunzai",
    zh_content: "Zai yige duoluo de shidai li, tamen zhiyi Shangdi de cunzai, dan shishi shang tamen ziji de cunzai he shengcun cai shi you wenhao de."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.QUESTIONING GODS EXISTENCE" AND c.name = "content.QUESTIONING GODS EXISTENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.QUESTIONING GODS EXISTENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.QUESTIONING GODS EXISTENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >QUESTIONING GODS EXISTENCE" }]->(child);
```

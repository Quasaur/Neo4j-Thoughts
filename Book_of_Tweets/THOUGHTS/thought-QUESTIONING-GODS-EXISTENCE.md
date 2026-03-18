---
type: THOUGHT
name: "thought.QUESTIONING GODS EXISTENCE"
alias: "Thought: Questioning Gods Existence"
parent: "topic.PHILOSOPHY"
en_content: "In a perverse generation they question God's Existence, when it's their existence and survival that has a question mark behind them."
tags: ["existence", "god", "survival", "skepticism", "philosophy"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Aug-2012b)
CREATE (t:THOUGHT {    name: "thought.QUESTIONING GODS EXISTENCE",
    alias: "Thought: Questioning Gods Existence",
    parent: "topic.PHILOSOPHY",
    tags: ['existence', 'god', 'survival', 'skepticism', 'philosophy'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.QUESTIONING GODS EXISTENCE",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.QUESTIONING GODS EXISTENCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->QUESTIONING GODS EXISTENCE"
RETURN t, parent;
```

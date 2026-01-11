---
name: "thought.IN_HIM_WE_LIVE"
alias: "Thought: IN HIM WE LIVE"
type: THOUGHT
parent: topic.CREATION
tags:
- creation
- divine
- fulness
- indwelling
- holyspirit
neo4j: true
ptopic: "[[topic-CREATION]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.IN_HIM_WE_LIVE",
    alias: "Thought: IN HIM WE LIVE",
    parent: "topic.CREATION",
    tags: ["creation", "divine", "fulness", "indwelling", "holyspirit"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IN_HIM_WE_LIVE",
    en_title: "IN HIM WE LIVE",
    en_content: "We are all inside of God...is God inside of us?",
    es_title: "EN ÉL VIVIMOS",
    es_content: "Todos estamos dentro de Dios... ¿está Dios dentro de nosotros?",
    fr_title: "EN LUI NOUS VIVONS",
    fr_content: "Nous sommes tous à l’intérieur de Dieu… Dieu est-il à l’intérieur de nous ?",
    hi_title: "हम उसी में रहते हैं",
    hi_content: "हम सब भगवान के अंदर हैं...क्या भगवान हमारे अंदर हैं?",
    zh_title: "wǒ men zhù zài tā lǐ miàn",
    zh_content: "wǒ men dōu zài shàng dì zhī nèi …… shàng dì zài wǒ men zhī nèi ma ？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IN_HIM_WE_LIVE" AND c.name = "content.IN_HIM_WE_LIVE"
MERGE (t)-[:HAS_CONTENT {name: "edge.IN_HIM_WE_LIVE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.IN_HIM_WE_LIVE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->IN_HIM_WE_LIVE"}]->(child);
```

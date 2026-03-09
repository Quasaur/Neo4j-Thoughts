---
type: THOUGHT
name: "thought.IN HIM WE LIVE"
alias: "Thought: In Him We Live"
parent: "topic.CREATION"
en_content: "We are all inside of God...is God inside of us?"
tags: ["creation", "divine", "fulness", "indwelling", "holy_spirit"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.IN HIM WE LIVE",
    alias: "Thought: In Him We Live",
    parent: "topic.CREATION",
    tags: ["creation", "divine", "fulness", "indwelling", "holy_spirit"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IN HIM WE LIVE",
    ctype: "THOUGHT",
    en_title: "In Him We Live",
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
WHERE t.name = "thought.IN HIM WE LIVE" AND c.name = "content.IN HIM WE LIVE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.IN HIM WE LIVE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.IN HIM WE LIVE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.CREATION->IN HIM WE LIVE"}]->(child);
```

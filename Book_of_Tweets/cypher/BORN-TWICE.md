---
name: "thought.BORN TWICE"
alias: "Thought: Born Twice"
type: THOUGHT
en_content: "Born once, die twice; born twice, die once--Happy Resurrection Day!"
parent: "topic.RELIGION"
tags:
- resurrection
- life
- death
- rebirth
- salvation
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.BORN TWICE",
    alias: "Thought: Born Twice",
    parent: "topic.RELIGION",
    tags: ['resurrection', 'life', 'death', 'rebirth', 'salvation'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.BORN TWICE",
    en_title: "Born Twice",
    en_content: "Born once, die twice; born twice, die once--Happy Resurrection Day!",
    es_title: "Nacido Dos Veces",
    es_content: "Nacido una vez, muere dos veces; nacido dos veces, muere una vez--¡Feliz Día de la Resurrección!",
    fr_title: "Né Deux Fois",
    fr_content: "Né une fois, meurt deux fois ; né deux fois, meurt une fois--Joyeuse jour de la Résurrection !",
    hi_title: "दो बार जन्म",
    hi_content: "एक बार जन्मे, दो बार मरो; दो बार जन्मे, एक बार मरो--पुनरुत्थान दिवस की शुभकामनाएं!",
    zh_title: "Shēng liǎng cì 生两次",
    zh_content: "Shēng yī cì, sǐ liǎng cì; shēng liǎng cì, sǐ yī cì--Fùhuójié kuàilè! 生一次，死两次；生两次，死一次--复活节快乐！"
});

MATCH (t:THOUGHT {name: "thought.BORN TWICE"})
MATCH (c:CONTENT {name: "content.BORN TWICE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.BORN TWICE" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.BORN TWICE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >BORN TWICE" }]->(child);
```

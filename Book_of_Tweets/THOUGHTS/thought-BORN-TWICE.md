---
type: THOUGHT
name: "thought.BORN TWICE"
alias: "Thought: Born Twice"
parent: "topic.RELIGION"
en_content: "Born once, die twice; born twice, die once--Happy Resurrection Day!"
tags: ["resurrection", "life", "death", "rebirth", "salvation"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Apr-2011)
CREATE (t:THOUGHT {    name: "thought.BORN TWICE",
    alias: "Thought: Born Twice",
    parent: "topic.RELIGION",
    tags: ['resurrection', 'life', 'death', 'rebirth', 'salvation'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.BORN TWICE",
    ctype: "THOUGHT",
    en_title: "Born Twice",
    en_content: "Born once, die twice; born twice, die once--Happy Resurrection Day!",
    es_title: "Nacido Dos Veces",
    es_content: "Nacido una vez, muere dos veces; nacido dos veces, muere una vez--¡Feliz Día de la Resurrección!",
    fr_title: "Né Deux Fois",
    fr_content: "Né une fois, meurt deux fois ; né deux fois, meurt une fois--Joyeuse jour de la Résurrection !",
    hi_title: "दो बार जन्म",
    hi_content: "एक बार जन्मे, दो बार मरो; दो बार जन्मे, एक बार मरो--पुनरुत्थान दिवस की शुभकामनाएं!",
    zh_title: "Shēng liǎng cì  shēng liǎng cì",
    zh_content: "Shēng yī cì, sǐ liǎng cì; shēng liǎng cì, sǐ yī cì--Fùhuójié kuàilè!  shēng yī cì ， sǐ liǎng cì ； shēng liǎng cì ， sǐ yī cì -- fù huó jié kuài lè ！"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BORN TWICE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->BORN TWICE"
RETURN t, parent;
```

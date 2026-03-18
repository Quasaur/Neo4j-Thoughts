---
type: THOUGHT
name: "thought.CHEATING THE ECONOMY"
alias: "Thought: Cheating The Economy"
parent: "topic.MORALITY"
en_content: "As long as we feel it necessary to cheat, lie and steal to survive, our economy will never truly prosper."
tags: ["cheat", "lie", "steal", "economy", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012g)
CREATE (t:THOUGHT {    name: "thought.CHEATING THE ECONOMY",
    alias: "Thought: Cheating The Economy",
    parent: "topic.MORALITY",
    tags: ['cheat', 'lie', 'steal', 'economy', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CHEATING THE ECONOMY",
    ctype: "THOUGHT",
    en_title: "Cheating The Economy",
    en_content: "As long as we feel it necessary to cheat, lie and steal to survive, our economy will never truly prosper.",
    es_title: "Engañar a la Economía",
    es_content: "Mientras sintamos que es necesario engañar, mentir y robar para sobrevivir, nuestra economía nunca prosperará verdaderamente.",
    fr_title: "Tromper l'Économie",
    fr_content: "Tant que nous estimons nécessaire de tricher, de mentir et de voler pour survivre, notre économie ne prospérera jamais vraiment.",
    hi_title: "अर्थव्यवस्था को धोखा देना",
    hi_content: "जब तक हम जीवित रहने के लिए धोखा देना, झूठ बोलना और चोरी करना आवश्यक समझते हैं, हमारी अर्थव्यवस्था कभी भी सच में समृद्ध नहीं होगी।",
    zh_title: "Qīpiàn Jīngjì",
    zh_content: "Zhǐyào wǒmen juédé wèile shēngcún bìxū qīpiàn, sāhuǎng hé tōuqiè, Wǒmen de jīngjì jiāng yǒngyuǎn bùhuì zhēnzhèng fánróng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CHEATING THE ECONOMY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->CHEATING THE ECONOMY"
RETURN t, parent;
```

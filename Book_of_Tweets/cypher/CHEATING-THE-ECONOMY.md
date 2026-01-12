---
name: "thought.CHEATING THE ECONOMY"
alias: "Thought: Cheating The Economy"
type: THOUGHT
en_content: "As long as we feel it necessary to cheat, lie and steal to survive, our economy will never truly prosper."
parent: "topic.MORALITY"
tags:
- cheat
- lie
- steal
- economy
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012g)
CREATE (t:THOUGHT {
    name: "thought.CHEATING THE ECONOMY",
    alias: "Thought: Cheating The Economy",
    parent: "topic.MORALITY",
    tags: ['cheat', 'lie', 'steal', 'economy', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHEATING THE ECONOMY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CHEATING THE ECONOMY" AND c.name = "content.CHEATING THE ECONOMY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHEATING THE ECONOMY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CHEATING THE ECONOMY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CHEATING THE ECONOMY" }]->(child);
```

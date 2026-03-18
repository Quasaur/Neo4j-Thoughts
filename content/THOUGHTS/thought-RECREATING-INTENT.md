---
type: THOUGHT
name: "thought.RECREATING INTENT"
alias: "Thought: Recreating Intent"
parent: "topic.LOVE"
en_content: "Fear of judgment will change our behavior...but not our hearts. Only the Love of Christ can recreate my intent."
tags: ["love", "transformation", "heart", "grace", "salvation"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.RECREATING INTENT",
    alias: "Thought: Recreating Intent",
    parent: "topic.LOVE",
    tags: ['love', 'transformation', 'heart', 'grace', 'salvation'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.RECREATING INTENT",
    ctype: "THOUGHT",
    en_title: "Recreating Intent",
    en_content: "Fear of judgment will change our behavior...but not our hearts. Only the Love of Christ can recreate my intent.",
    es_title: "Recreando la Intención",
    es_content: "El temor al juicio cambiará nuestro comportamiento...pero no nuestros corazones. Solo el Amor de Cristo puede recrear mi intención.",
    fr_title: "Recréer l'Intention",
    fr_content: "La peur du jugement changera notre comportement...mais pas nos cœurs. Seul l'Amour du Christ peut recréer mon intention.",
    hi_title: "आशय का पुनर्निर्माण",
    hi_content: "न्याय का भय हमारे व्यवहार को बदल देगा...लेकिन हमारे हृदय को नहीं। केवल मसीह का प्रेम ही मेरे आशय का पुनर्निर्माण कर सकता है।",
    zh_title: "Chóngjiàn Yìtú",
    zh_content: "Duì shěnpàn de kǒngjù huì gǎibiàn wǒmen de xíngwéi...dàn bù huì gǎibiàn wǒmen de xīn. Zhǐyǒu Jīdū de ài cáinéng chóngjiàn wǒ de yìtú."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.RECREATING INTENT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->RECREATING INTENT"
RETURN t, parent;
```

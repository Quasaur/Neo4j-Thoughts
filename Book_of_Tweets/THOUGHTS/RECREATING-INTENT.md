---
name: "thought.RECREATING INTENT"
alias: "Thought: Recreating Intent"
type: THOUGHT
en_content: "Fear of judgment will change our behavior...but not our hearts. Only the Love of Christ can recreate my intent."
parent: "topic.GRACE"
tags:
- love
- transformation
- heart
- grace
- salvation
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jul-2011a)
CREATE (t:THOUGHT {
    name: "thought.RECREATING INTENT",
    alias: "Thought: Recreating Intent",
    parent: "topic.GRACE",
    tags: ['love', 'transformation', 'heart', 'grace', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RECREATING INTENT",
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

MATCH (t:THOUGHT {name: "thought.RECREATING INTENT"})
MATCH (c:CONTENT {name: "content.RECREATING INTENT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.RECREATING INTENT" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.RECREATING INTENT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE->RECREATING INTENT" }]->(child);
```

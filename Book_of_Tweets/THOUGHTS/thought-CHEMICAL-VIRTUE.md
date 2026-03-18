---
type: THOUGHT
name: "thought.CHEMICAL VIRTUE"
alias: "Thought: Chemical Virtue"
parent: "topic.PHILOSOPHY"
en_content: "You yourself are a supernatural being! Explain LOVE, or COURAGE or VIRTUE chemically."
tags: ["supernatural", "love", "courage", "chemistry", "philosophy"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011f)
CREATE (t:THOUGHT {    name: "thought.CHEMICAL VIRTUE",
    alias: "Thought: Chemical Virtue",
    parent: "topic.PHILOSOPHY",
    tags: ['supernatural', 'love', 'courage', 'chemistry', 'philosophy'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.CHEMICAL VIRTUE",
    ctype: "THOUGHT",
    en_title: "Chemical Virtue",
    en_content: "You yourself are a supernatural being! Explain LOVE, or COURAGE or VIRTUE chemically.",
    es_title: "Virtud Química",
    es_content: "¡Tú mismo eres un ser sobrenatural! Explica el AMOR, o el VALOR o la VIRTUD químicamente.",
    fr_title: "Vertu Chimique",
    fr_content: "Vous êtes vous-même un être surnaturel ! Expliquez l'AMOUR, ou le COURAGE ou la VERTU chimiquement.",
    hi_title: "रासायनिक गुण",
    hi_content: "आप स्वयं एक अलौकिक प्राणी हैं! प्रेम, या साहस या गुण को रासायनिक रूप से समझाइए।",
    zh_title: "Huàxué Měidé",
    zh_content: "Nǐ zìjǐ jiù shì yīgè chāozìrán de shēngwù! Yòng huàxué jiěshì RÀNG, YǑNGQÌ huò MĚIDÉ."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CHEMICAL VIRTUE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->CHEMICAL VIRTUE"
RETURN t, parent;
```

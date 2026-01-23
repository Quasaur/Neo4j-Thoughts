---
name: "thought.CHEMICAL VIRTUE"
alias: "Thought: Chemical Virtue"
type: THOUGHT
en_content: "You yourself are a supernatural being! Explain LOVE, or COURAGE or VIRTUE chemically."
parent: "topic.PHILOSOPHY"
tags:
- supernatural
- love
- courage
- chemistry
- philosophy
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011f)
CREATE (t:THOUGHT {
    name: "thought.CHEMICAL VIRTUE",
    alias: "Thought: Chemical Virtue",
    parent: "topic.PHILOSOPHY",
    tags: ['supernatural', 'love', 'courage', 'chemistry', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHEMICAL VIRTUE",
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

MATCH (t:THOUGHT {name: "thought.CHEMICAL VIRTUE"})
MATCH (c:CONTENT {name: "content.CHEMICAL VIRTUE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHEMICAL VIRTUE" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.CHEMICAL VIRTUE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >CHEMICAL VIRTUE" }]->(child);
```

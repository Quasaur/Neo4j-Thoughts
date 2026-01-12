---
name: "thought.OMNIPOTENCE VS FREEWILL"
alias: "Thought: Omnipotence Vs Freewill"
type: THOUGHT
en_content: "Free Will exists only due to human ignorance of The Divine Omnipotence."
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- freewill
- omnipotence
- ignorance
- divinity
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jun-2012a)
CREATE (t:THOUGHT {
    name: "thought.OMNIPOTENCE VS FREEWILL",
    alias: "Thought: Omnipotence Vs Freewill",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'freewill', 'omnipotence', 'ignorance', 'divinity'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.OMNIPOTENCE VS FREEWILL",
    en_title: "Omnipotence Vs Freewill",
    en_content: "Free Will exists only due to human ignorance of The Divine Omnipotence.",
    es_title: "Omnipotencia Vs Libre Albedrío",
    es_content: "El Libre Albedrío existe únicamente debido a la ignorancia humana de La Omnipotencia Divina.",
    fr_title: "Omnipotence Vs Libre Arbitre",
    fr_content: "Le Libre Arbitre n'existe qu'en raison de l'ignorance humaine de L'Omnipotence Divine.",
    hi_title: "सर्वशक्तिमत्ता बनाम स्वतंत्र इच्छा",
    hi_content: "स्वतंत्र इच्छा केवल दिव्य सर्वशक्तिमत्ता के मानवीय अज्ञान के कारण ही अस्तित्व में है।",
    zh_title: "Quánnéng Vs Zìyóu Yìzhì",
    zh_content: "Zìyóu Yìzhì jǐnjǐn yīnwèi rénlèi duì Shénshèng Quánnéng de wúzhī ér cúnzài."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.OMNIPOTENCE VS FREEWILL" AND c.name = "content.OMNIPOTENCE VS FREEWILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OMNIPOTENCE VS FREEWILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.OMNIPOTENCE VS FREEWILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >OMNIPOTENCE VS FREEWILL" }]->(child);
```

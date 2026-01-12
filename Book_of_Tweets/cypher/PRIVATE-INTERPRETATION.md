---
name: "thought.PRIVATE INTERPRETATION"
alias: "Thought: Private Interpretation"
type: THOUGHT
en_content: "Where Satan can't stop Bible reading he distracts with private interpretation."
parent: "topic.TRUTH"
tags:
- bible
- satan
- truth
- deception
- interpretation
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.PRIVATE INTERPRETATION",
    alias: "Thought: Private Interpretation",
    parent: "topic.TRUTH",
    tags: ['bible', 'satan', 'truth', 'deception', 'interpretation'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRIVATE INTERPRETATION",
    en_title: "Private Interpretation",
    en_content: "Where Satan can't stop Bible reading he distracts with private interpretation.",
    es_title: "Interpretación Privada",
    es_content: "Donde Satanás no puede detener la lectura de la Biblia, distrae con interpretación privada.",
    fr_title: "Interprétation Privée",
    fr_content: "Là où Satan ne peut pas arrêter la lecture de la Bible, il distrait par l'interprétation privée.",
    hi_title: "निजी व्याख्या",
    hi_content: "जहाँ शैतान बाइबल पढ़ने को रोक नहीं सकता, वहाँ वह निजी व्याख्या से भटकाता है।",
    zh_title: "Si Ren Jie Shi",
    zh_content: "Dang Sa Dan Wu Fa Zu Zhi Du Sheng Jing Shi, Ta Jiu Yong Si Ren Jie Shi Lai Fen San Zhu Yi Li."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRIVATE INTERPRETATION" AND c.name = "content.PRIVATE INTERPRETATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRIVATE INTERPRETATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.PRIVATE INTERPRETATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >PRIVATE INTERPRETATION" }]->(child);
```

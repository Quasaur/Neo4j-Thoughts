---
name: "thought.TRULY HUMAN ENGAGEMENT"
alias: "Thought: Truly Human Engagement"
type: THOUGHT
en_content: "One is not truly human until they have engaged their Creator."
parent: "topic.HUMANITY"
tags:
- humanity
- creator
- engagement
- identity
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Jan-2014)
CREATE (t:THOUGHT {
    name: "thought.TRULY HUMAN ENGAGEMENT",
    alias: "Thought: Truly Human Engagement",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'creator', 'engagement', 'identity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TRULY HUMAN ENGAGEMENT",
    en_title: "Truly Human Engagement",
    en_content: "One is not truly human until they have engaged their Creator.",
    es_title: "Compromiso Verdaderamente Humano",
    es_content: "Uno no es verdaderamente humano hasta que ha entrado en relación con su Creador.",
    fr_title: "Engagement Véritablement Humain",
    fr_content: "On n'est pas véritablement humain tant qu'on n'a pas engagé son Créateur.",
    hi_title: "सच्ची मानवीय संलग्नता",
    hi_content: "कोई व्यक्ति तब तक वास्तव में मानव नहीं है जब तक वह अपने सृष्टिकर्ता से जुड़ाव नहीं करता।",
    zh_title: "Zhen Zheng De Ren Lei Can Yu",
    zh_content: "Yi Ge Ren Zhi You Yu Ta De Zao Wu Zhu Jian Li Guan Xi Hou, Cai Zhen Zheng Cheng Wei Ren Lei."
});

MATCH (t:THOUGHT {name: "thought.TRULY HUMAN ENGAGEMENT"})
MATCH (c:CONTENT {name: "content.TRULY HUMAN ENGAGEMENT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRULY HUMAN ENGAGEMENT" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.TRULY HUMAN ENGAGEMENT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->TRULY HUMAN ENGAGEMENT" }]->(child);
```

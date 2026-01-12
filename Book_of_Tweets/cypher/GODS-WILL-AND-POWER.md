---
name: "thought.GODS WILL AND POWER"
alias: "Thought: Gods Will And Power"
type: THOUGHT
en_content: "God has His Own Will and Desire and more than enough Power to execute Them."
parent: "topic.THE GODHEAD"
tags:
- will
- desire
- power
- god
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2014)
CREATE (t:THOUGHT {
    name: "thought.GODS WILL AND POWER",
    alias: "Thought: Gods Will And Power",
    parent: "topic.THE GODHEAD",
    tags: ['will', 'desire', 'power', 'god'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS WILL AND POWER",
    en_title: "Gods Will And Power",
    en_content: "God has His Own Will and Desire and more than enough Power to execute Them.",
    es_title: "La Voluntad y el Poder de Dios",
    es_content: "Dios tiene Su propia Voluntad y Deseo y más que suficiente Poder para ejecutarlos.",
    fr_title: "La Volonté et la Puissance de Dieu",
    fr_content: "Dieu a Sa propre Volonté et Son Désir et plus qu'assez de Puissance pour les exécuter.",
    hi_title: "परमेश्वर की इच्छा और शक्ति",
    hi_content: "परमेश्वर की अपनी इच्छा और चाह है और उन्हें पूरा करने के लिए पर्याप्त से भी अधिक शक्ति है।",
    zh_title: "Shàngdì de Yìzhì hé Nénglì",
    zh_content: "Shàngdì yǒu Tā zìjǐ de Yìzhì hé Yuànwàng, bìngqiě yǒu zúgòu de Nénglì qù zhíxíng Tāmen."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GODS WILL AND POWER" AND c.name = "content.GODS WILL AND POWER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS WILL AND POWER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS WILL AND POWER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS WILL AND POWER" }]->(child);
```

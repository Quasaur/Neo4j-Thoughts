---
name: "thought.TEN TRILLION CELLS"
alias: "Thought: Ten Trillion Cells"
type: THOUGHT
en_content: "The human body is made up of at least 10 trillion cells...God is great!"
parent: "topic.CREATION"
tags:
- creation
- biology
- cells
- life
- power
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.TEN TRILLION CELLS",
    alias: "Thought: Ten Trillion Cells",
    parent: "topic.CREATION",
    tags: ['creation', 'biology', 'cells', 'life', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TEN TRILLION CELLS",
    en_title: "Ten Trillion Cells",
    en_content: "The human body is made up of at least 10 trillion cells...God is great!",
    es_title: "Diez Billones de Células",
    es_content: "El cuerpo humano está compuesto de al menos 10 billones de células... ¡Dios es grande!",
    fr_title: "Dix Billions de Cellules",
    fr_content: "Le corps humain est composé d'au moins 10 billions de cellules... Dieu est grand !",
    hi_title: "दस ट्रिलियन कोशिकाएं",
    hi_content: "मानव शरीर कम से कम 10 ट्रिलियन कोशिकाओं से बना है... परमेश्वर महान है!",
    zh_title: "Shí wàn yì xìbāo 十万亿细胞",
    zh_content: "Réntǐ yóu zhìshǎo 10 wàn yì gè xìbāo... Shàngdì zhēn wěidà! 人体由至少 10 万亿个细胞...上帝真伟大！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TEN TRILLION CELLS" AND c.name = "content.TEN TRILLION CELLS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TEN TRILLION CELLS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.TEN TRILLION CELLS"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >TEN TRILLION CELLS" }]->(child);
```

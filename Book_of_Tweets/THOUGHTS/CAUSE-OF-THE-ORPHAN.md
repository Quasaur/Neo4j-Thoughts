---
name: "thought.CAUSE OF THE ORPHAN"
alias: "Thought: Cause Of The Orphan"
type: THOUGHT
en_content: "\"They do not plead the cause, (The cause of the orphan), THAT THEY MAY PROSPER; And they do not defend the rights of the poor.\" -- Jeremiah"
parent: "topic.MORALITY"
tags:
- justice
- orphan
- poor
- morality
- prophet
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.CAUSE OF THE ORPHAN",
    alias: "Thought: Cause Of The Orphan",
    parent: "topic.MORALITY",
    tags: ['justice', 'orphan', 'poor', 'morality', 'prophet'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CAUSE OF THE ORPHAN",
    en_title: "Cause Of The Orphan",
    en_content: "\"They do not plead the cause, (The cause of the orphan), THAT THEY MAY PROSPER; And they do not defend the rights of the poor.\" -- Jeremiah",
    es_title: "La Causa del Huérfano",
    es_content: "\"Ellos no defienden la causa, (La causa del huérfano), PARA QUE PROSPEREN; Y no defienden los derechos de los pobres.\" -- Jeremías",
    fr_title: "La Cause de l'Orphelin",
    fr_content: "\"Ils ne plaident pas la cause, (La cause de l'orphelin), AFIN QU'ILS PROSPÈRENT ; Et ils ne défendent pas les droits des pauvres.\" -- Jérémie",
    hi_title: "अनाथ का कारण",
    hi_content: "\"वे इस कारण की वकालत नहीं करते, (अनाथ का कारण), ताकि वे समृद्ध हों; और वे गरीबों के अधिकारों की रक्षा नहीं करते।\" -- यिर्मयाह",
    zh_title: "Gūér de Shìyè",
    zh_content: "\"Tāmen bù wèi cǐ shì biànhù, (Gūér de shìyè), Shǐ tāmen fánróng; Yě bù bǎohù qióngrén de quánlì.\" -- Yēlìmǐshū"
});

MATCH (t:THOUGHT {name: "thought.CAUSE OF THE ORPHAN"})
MATCH (c:CONTENT {name: "content.CAUSE OF THE ORPHAN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CAUSE OF THE ORPHAN" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.CAUSE OF THE ORPHAN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->CAUSE OF THE ORPHAN" }]->(child);
```

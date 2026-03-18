---
type: THOUGHT
name: "thought.LIMITLESS DIVINE POWER"
alias: "Thought: Limitless Divine Power"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "ABSOLUTE POWER: Besides His Own Limitless Power, everyone else's power is also at God's Disposal...even Satan's."
tags: ["power", "sovereignty", "god", "disposal", "control"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LIMITLESS DIVINE POWER",
    alias: "Thought: Limitless Divine Power",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['power', 'sovereignty', 'god', 'disposal', 'control'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIMITLESS DIVINE POWER",
    ctype: "THOUGHT",
    en_title: "Limitless Divine Power",
    en_content: "ABSOLUTE POWER: Besides His Own Limitless Power, everyone else's power is also at God's Disposal...even Satan's.",
    es_title: "Poder Divino Ilimitado",
    es_content: "PODER ABSOLUTO: Además de Su Propio Poder Ilimitado, el poder de todos los demás también está a Disposición de Dios...incluso el de Satanás.",
    fr_title: "Puissance Divine Illimitée",
    fr_content: "PUISSANCE ABSOLUE : Outre Sa Propre Puissance Illimitée, le pouvoir de tous les autres est aussi à la Disposition de Dieu...même celui de Satan.",
    hi_title: "असीम दिव्य शक्ति",
    hi_content: "परम शक्ति: अपनी स्वयं की असीम शक्ति के अतिरिक्त, बाकी सभी की शक्ति भी परमेश्वर के अधिकार में है...यहाँ तक कि शैतान की भी।",
    zh_title: "Wú Xiàn Shén Lì",
    zh_content: "JUÉ DUÌ QUÁN LÌ: Chú le Tā Zì Jǐ de Wú Xiàn Quán Lì zhī wài, qí tā suǒ yǒu rén de quán lì yě dōu zài Shàng Dì de Zhī Pèi xià...shèn zhì Sā Dàn de yě shì。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIMITLESS DIVINE POWER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->LIMITLESS DIVINE POWER"
RETURN t, parent;
```

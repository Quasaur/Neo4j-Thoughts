---
type: THOUGHT
name: "thought.DIVINE VISITATION EFFECT"
alias: "Thought: Divine Visitation Effect"
parent: "topic.SPIRITUALITY"
en_content: "A Divine Visitation will ruin you for this life. You may look and act like everyone, but you're not like them...you're of another World."
tags: ["visitation", "life", "transformation", "world", "spirituality"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Sep-2013)
CREATE (t:THOUGHT {    name: "thought.DIVINE VISITATION EFFECT",
    alias: "Thought: Divine Visitation Effect",
    parent: "topic.SPIRITUALITY",
    tags: ['visitation', 'life', 'transformation', 'world', 'spirituality'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.DIVINE VISITATION EFFECT",
    ctype: "THOUGHT",
    en_title: "Divine Visitation Effect",
    en_content: "A Divine Visitation will ruin you for this life. You may look and act like everyone, but you're not like them...you're of another World.",
    es_title: "Efecto de la Visitación Divina",
    es_content: "Una Visitación Divina te arruinará para esta vida. Puedes verte y actuar como todos los demás, pero no eres como ellos...eres de otro Mundo.",
    fr_title: "Effet de la Visitation Divine",
    fr_content: "Une Visitation Divine vous ruinera pour cette vie. Vous pouvez paraître et agir comme tout le monde, mais vous n'êtes pas comme eux...vous êtes d'un autre Monde.",
    hi_title: "दिव्य दर्शन प्रभाव",
    hi_content: "एक दिव्य दर्शन आपको इस जीवन के लिए बर्बाद कर देगा। आप सबकी तरह दिख और व्यवहार कर सकते हैं, लेकिन आप उनके जैसे नहीं हैं...आप दूसरे संसार के हैं।",
    zh_title: "Shén Lín Xiào Yìng",
    zh_content: "Shén de Lái Lín huì ràng nǐ duì zhè shēng huó shī qù xìng qù. Nǐ kě néng kàn qǐ lái hé xíng wéi dōu xiàng qí tā rén, dàn nǐ bù xiàng tā men...nǐ shǔ yú lìng yī gè Shì Jiè."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DIVINE VISITATION EFFECT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->DIVINE VISITATION EFFECT"
RETURN t, parent;
```

---
name: "thought.DIVINE VISITATION EFFECT"
alias: "Thought: Divine Visitation Effect"
type: THOUGHT
en_content: "A Divine Visitation will ruin you for this life. You may look and act like everyone, but you're not like them...you're of another World."
parent: "topic.SPIRITUALITY"
tags:
- visitation
- life
- transformation
- world
- spirituality
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Sep-2013)
CREATE (t:THOUGHT {
    name: "thought.DIVINE VISITATION EFFECT",
    alias: "Thought: Divine Visitation Effect",
    parent: "topic.SPIRITUALITY",
    tags: ['visitation', 'life', 'transformation', 'world', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DIVINE VISITATION EFFECT",
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

MATCH (t:THOUGHT {name: "thought.DIVINE VISITATION EFFECT"})
MATCH (c:CONTENT {name: "content.DIVINE VISITATION EFFECT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DIVINE VISITATION EFFECT" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.DIVINE VISITATION EFFECT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >DIVINE VISITATION EFFECT" }]->(child);
```

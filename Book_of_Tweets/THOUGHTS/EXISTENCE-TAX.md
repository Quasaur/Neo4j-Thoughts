---
name: "thought.EXISTENCE TAX"
alias: "Thought: Existence Tax"
type: THOUGHT
en_content: "Cost of Living: Men can't CREATE Life...so they're gonna charge it an existence tax...are you kidding me?!?"
parent: "topic.MORALITY"
tags:
- life
- morality
- society
- tax
- creation
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.EXISTENCE TAX",
    alias: "Thought: Existence Tax",
    parent: "topic.MORALITY",
    tags: ['life', 'morality', 'society', 'tax', 'creation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.EXISTENCE TAX",
    en_title: "Existence Tax",
    en_content: "Cost of Living: Men can't CREATE Life...so they're gonna charge it an existence tax...are you kidding me?!?",
    es_title: "Impuesto de Existencia",
    es_content: "Costo de Vida: Los hombres no pueden CREAR Vida...así que le van a cobrar un impuesto de existencia...¿¡en serio!?",
    fr_title: "Taxe d'Existence",
    fr_content: "Coût de la Vie: Les hommes ne peuvent pas CRÉER la Vie...alors ils vont lui imposer une taxe d'existence...vous plaisantez ?!",
    hi_title: "अस्तित्व कर",
    hi_content: "जीवन यापन की लागत: पुरुष जीवन का सृजन नहीं कर सकते...इसलिए वे इस पर अस्तित्व कर लगाने जा रहे हैं...क्या आप मजाक कर रहे हैं?!",
    zh_title: "Cúnzài Shuì",
    zh_content: "Shēnghuó Chéngběn: Nánrén bùnéng CHUÀNGZÀO Shēngmìng...suǒyǐ tāmen yào duì tā shōu cúnzài shuì...nǐ zài kāi wánxiào ma?!"
});

MATCH (t:THOUGHT {name: "thought.EXISTENCE TAX"})
MATCH (c:CONTENT {name: "content.EXISTENCE TAX"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.EXISTENCE TAX" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.EXISTENCE TAX"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->EXISTENCE TAX" }]->(child);
```

---
name: "thought.WITHHOLDING POWERS"
alias: "Thought: Withholding Powers"
type: THOUGHT
en_content: "God withholds powers from us because we do not give Him glory for powers already bestowed."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- power
- glory
- sovereignty
- character
- responsibility
level: 2
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.WITHHOLDING POWERS",
    alias: "Thought: Withholding Powers",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['power', 'glory', 'sovereignty', 'character', 'responsibility'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WITHHOLDING POWERS",
    en_title: "Withholding Powers",
    en_content: "God withholds powers from us because we do not give Him glory for powers already bestowed.",
    es_title: "Retención de Poderes",
    es_content: "Dios nos retiene poderes porque no le damos gloria por los poderes ya concedidos.",
    fr_title: "Rétention des Pouvoirs",
    fr_content: "Dieu nous retient des pouvoirs parce que nous ne lui rendons pas gloire pour les pouvoirs déjà accordés.",
    hi_title: "शक्तियों का रोकना",
    hi_content: "परमेश्वर हमसे शक्तियों को रोकता है क्योंकि हम उन शक्तियों के लिए उसकी महिमा नहीं करते जो पहले से दी गई हैं।",
    zh_title: "Kòu Liú Néng Lì",
    zh_content: "Shàng Dì kòu liú wǒ men de néng lì, yīn wèi wǒ men méi yǒu wèi Tā yǐ jīng cì yǔ de néng lì ér guī róng yú Tā."
});

MATCH (t:THOUGHT {name: "thought.WITHHOLDING POWERS"})
MATCH (c:CONTENT {name: "content.WITHHOLDING POWERS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.WITHHOLDING POWERS" }]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.WITHHOLDING POWERS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY->WITHHOLDING POWERS" }]->(child);
```

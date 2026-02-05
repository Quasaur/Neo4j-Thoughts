---
name: "thought.CHOKING THE WORD"
alias: "Thought: Choking The Word"
type: THOUGHT
en_content: "Like weeds choke a flower, the cares of this life and the deceitfulness of riches choke the Word of God in my heart, and make it unfruitful."
parent: "topic.FAITH"
tags:
- faith
- word
- riches
- distraction
- growth
level: 4
neo4j: false
ptopic: "[[topic-FAITH]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.CHOKING THE WORD",
    alias: "Thought: Choking The Word",
    parent: "topic.FAITH",
    tags: ['faith', 'word', 'riches', 'temptation', 'growth'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHOKING THE WORD",
    en_title: "Choking The Word",
    en_content: "Like weeds choke a flower, the cares of this life and the deceitfulness of riches choke the Word of God in my heart, and make it unfruitful.",
    es_title: "Ahogando la Palabra",
    es_content: "Como las malas hierbas ahogan una flor, los afanes de esta vida y el engaño de las riquezas ahogan la Palabra de Dios en mi corazón, y la hacen infructuosa.",
    fr_title: "Étouffer la Parole",
    fr_content: "Comme les mauvaises herbes étouffent une fleur, les soucis de cette vie et la séduction des richesses étouffent la Parole de Dieu dans mon cœur, et la rendent infructueuse.",
    hi_title: "वचन को दबाना",
    hi_content: "जैसे खरपतवार एक फूल को दबा देती है, इस जीवन की चिंताएं और धन का धोखा मेरे हृदय में परमेश्वर के वचन को दबा देते हैं, और इसे निष्फल बना देते हैं।",
    zh_title: "Yānmò Zhēn Dào",
    zh_content: "Xiàng yěcǎo yānmò huāduǒ yīyàng, Jīnshì de sīlǜ hé cáif\u00f9 de míhuò yānmòle wǒ xīnzhōng de Shén Dào, Shǐ tā bùnéng jiéguǒ."
});

MATCH (t:THOUGHT {name: "thought.CHOKING THE WORD"})
MATCH (c:CONTENT {name: "content.CHOKING THE WORD"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.CHOKING THE WORD" }]->(c);

MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:THOUGHT {name: "thought.CHOKING THE WORD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.FAITH->CHOKING THE WORD" }]->(child);
```

---
name: "thought.FLESH VS SPIRIT"
alias: "Thought: Flesh Vs Spirit"
type: THOUGHT
en_content: "The flesh is too stupid to be spiritual; it must be crucified with Christ and brought in subjection by the Love of God to the Spirit of God."
parent: "topic.SPIRITUALITY"
tags:
- flesh
- spirit
- crucifixion
- subjection
- sanctification
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.FLESH VS SPIRIT",
    alias: "Thought: Flesh Vs Spirit",
    parent: "topic.SPIRITUALITY",
    tags: ['flesh', 'spirit', 'crucifixion', 'subjection', 'sanctification'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FLESH VS SPIRIT",
    en_title: "Flesh Vs Spirit",
    en_content: "The flesh is too stupid to be spiritual; it must be crucified with Christ and brought in subjection by the Love of God to the Spirit of God.",
    es_title: "Carne versus Espíritu",
    es_content: "La carne es demasiado tonta para ser espiritual; debe ser crucificada con Cristo y sometida por el Amor de Dios al Espíritu de Dios.",
    fr_title: "Chair contre Esprit",
    fr_content: "La chair est trop stupide pour être spirituelle ; elle doit être crucifiée avec Christ et soumise par l'Amour de Dieu à l'Esprit de Dieu.",
    hi_title: "शरीर बनाम आत्मा",
    hi_content: "शरीर आध्यात्मिक होने के लिए बहुत मूर्ख है; इसे मसीह के साथ क्रूस पर चढ़ाया जाना चाहिए और परमेश्वर के प्रेम द्वारा परमेश्वर के आत्मा के अधीन लाया जाना चाहिए।",
    zh_title: "Ròutǐ yǔ Líng 肉体与灵",
    zh_content: "Ròutǐ tài yúchǔn, wúfǎ língxìng; tā bìxū yǔ Jīdū tóng dìng shízi jià, bìng tòngguò Shàngdì de ài bèi Shàngdì de Líng suǒ zhìfú. 肉体太愚蠢，无法灵性；它必须与基督同钉十字架，并通过上帝的爱被上帝的灵所制服。"
});

MATCH (t:THOUGHT {name: "thought.FLESH VS SPIRIT"})
MATCH (c:CONTENT {name: "content.FLESH VS SPIRIT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FLESH VS SPIRIT" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.FLESH VS SPIRIT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >FLESH VS SPIRIT" }]->(child);
```

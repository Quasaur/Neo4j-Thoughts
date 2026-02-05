---
name: "thought.MAJORITY OF THREE"
alias: "Thought: Majority Of Three"
type: THOUGHT
en_content: "The Godhead is a Majority of Three: Their LIFE far outweighs all Death in the Cosmos...and their GOODNESS overwhelms all Evil!"
parent: "topic.THE GODHEAD"
tags:
- godhead
- life
- death
- goodness
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jun-2014)
CREATE (t:THOUGHT {
    name: "thought.MAJORITY OF THREE",
    alias: "Thought: Majority Of Three",
    parent: "topic.THE GODHEAD",
    tags: ['godhead', 'life', 'death', 'goodness'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MAJORITY OF THREE",
    en_title: "Majority Of Three",
    en_content: "The Godhead is a Majority of Three: Their LIFE far outweighs all Death in the Cosmos...and their GOODNESS overwhelms all Evil!",
    es_title: "Mayoría de tres",
    es_content: "La Divinidad es una Mayoría de Tres: Su VIDA supera con creces toda Muerte en el Cosmos... ¡y su BONDAD supera todo Mal!",
    fr_title: "Majorité de trois",
    fr_content: "La Divinité est une majorité de trois : leur VIE dépasse de loin toute mort dans le cosmos... et leur BONTÉ submerge tout le mal !",
    hi_title: "तीन का बहुमत",
    hi_content: "ईश्वरत्व तीन का बहुमत है: उनका जीवन ब्रह्मांड में सभी मृत्यु से कहीं अधिक है... और उनकी अच्छाई सभी बुराईयों पर हावी हो जाती है!",
    zh_title: "sān rén duō shù",
    zh_content: "shén xìng shì sān wèi duō shù ： tā men de shēng mìng yuǎn yuǎn chāo guò yǔ zhòu zhōng suǒ yǒu de sǐ wáng …… tā men de shàn liáng yā dǎo le suǒ yǒu xié è ！"
});

MATCH (t:THOUGHT {name: "thought.MAJORITY OF THREE"})
MATCH (c:CONTENT {name: "content.MAJORITY OF THREE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.MAJORITY OF THREE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.MAJORITY OF THREE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->MAJORITY OF THREE" }]->(child);
```

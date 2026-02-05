---
name: "thought.BOUNTIFUL EYE"
alias: "Thought: Bountiful Eye"
type: THOUGHT
en_content: "Whoever has a bountiful eye will be blessed, for he shares his bread with the poor. Proverbs 22:9, ESV"
parent: "topic.MORALITY"
tags:
- blessing
- generosity
- poor
- morality
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.BOUNTIFUL EYE",
    alias: "Thought: Bountiful Eye",
    parent: "topic.MORALITY",
    tags: ['blessing', 'generosity', 'poor', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BOUNTIFUL EYE",
    en_title: "Bountiful Eye",
    en_content: "Whoever has a bountiful eye will be blessed, for he shares his bread with the poor. Proverbs 22:9, ESV",
    es_title: "Ojo Generoso",
    es_content: "Quien tiene un ojo generoso será bendecido, porque comparte su pan con los pobres. Proverbios 22:9, RV",
    fr_title: "Œil Généreux",
    fr_content: "Celui qui a un œil généreux sera béni, car il partage son pain avec les pauvres. Proverbes 22:9, LSG",
    hi_title: "उदार दृष्टि",
    hi_content: "जो उदार दृष्टि रखता है वह आशीष पाएगा, क्योंकि वह गरीबों के साथ अपनी रोटी बांटता है। नीतिवचन 22:9",
    zh_title: "Kāngkǎi de yǎnjuāng  kāng kǎi de yǎn jīng",
    zh_content: "Yǒngyǒu kāngkǎi de yǎnjuāng zhī rén bì yùfú, yīnwèi tā yǔ qióngrén fēnxǎng miànbao. Zhíyán 22:9  yǒu kāng kǎi de yǎn jīng zhī rén bì méng fú ， yīn wèi tā yǔ qióng rén fēn xiǎng miàn bāo 。 zhēn yán  22:9"
});

MATCH (t:THOUGHT {name: "thought.BOUNTIFUL EYE"})
MATCH (c:CONTENT {name: "content.BOUNTIFUL EYE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.BOUNTIFUL EYE" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.BOUNTIFUL EYE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->BOUNTIFUL EYE" }]->(child);
```

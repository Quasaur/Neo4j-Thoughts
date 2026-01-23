---
name: "thought.GLORY THROUGH LOSERS"
alias: "Thought: Glory Through Losers"
type: THOUGHT
en_content: "God prefers losers so that when we win God gets the glory!"
parent: "topic.GRACE"
tags:
- grace
- glory
- humility
- weakness
- blessing
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.GLORY THROUGH LOSERS",
    alias: "Thought: Glory Through Losers",
    parent: "topic.GRACE",
    tags: ['grace', 'glory', 'humility', 'weakness', 'blessing'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GLORY THROUGH LOSERS",
    en_title: "Glory Through Losers",
    en_content: "God prefers losers so that when we win God gets the glory!",
    es_title: "Gloria a Través de los Perdedores",
    es_content: "¡Dios prefiere a los perdedores para que cuando ganemos Dios reciba la gloria!",
    fr_title: "Gloire à Travers les Perdants",
    fr_content: "Dieu préfère les perdants pour que lorsque nous gagnons, Dieu reçoive la gloire !",
    hi_title: "हारने वालों के द्वारा महिमा",
    hi_content: "परमेश्वर हारने वालों को पसंद करता है ताकि जब हम जीतें तो परमेश्वर को महिमा मिले!",
    zh_title: "tōng guò shī bài zhě de róng yào",
    zh_content: "shàng dì xǐ huān shī bài zhě, zhè yàng dāng wǒ men dé shèng shí shàng dì jiù dé dào róng yào!"
});

MATCH (t:THOUGHT {name: "thought.GLORY THROUGH LOSERS"})
MATCH (c:CONTENT {name: "content.GLORY THROUGH LOSERS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GLORY THROUGH LOSERS" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.GLORY THROUGH LOSERS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >GLORY THROUGH LOSERS" }]->(child);
```

---
name: "thought.FREEDOM TO RUIN"
alias: "Thought: Freedom To Ruin"
type: THOUGHT
en_content: "It appears that God has given us the freedom to ruin our lives as we see fit...so much for Freedom."
parent: "topic.HUMANITY"
tags:
- freedom
- responsibility
- choice
- humanity
- ruin
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Jan-2011)
CREATE (t:THOUGHT {
    name: "thought.FREEDOM TO RUIN",
    alias: "Thought: Freedom To Ruin",
    parent: "topic.HUMANITY",
    tags: ['freedom', 'responsibility', 'choice', 'humanity', 'ruin'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FREEDOM TO RUIN",
    en_title: "Freedom To Ruin",
    en_content: "It appears that God has given us the freedom to ruin our lives as we see fit...so much for Freedom.",
    es_title: "Libertad para Arruinarse",
    es_content: "Parece que Dios nos ha dado la libertad de arruinar nuestras vidas como mejor nos parezca... eso es lo que hay de la Libertad.",
    fr_title: "Liberté de se Ruiner",
    fr_content: "Il semble que Dieu nous ait donné la liberté de ruiner nos vies comme bon nous semble... voilà pour la Liberté.",
    hi_title: "बर्बादी की स्वतंत्रता",
    hi_content: "ऐसा लगता है कि परमेश्वर ने हमें अपने जीवन को बर्बाद करने की स्वतंत्रता दी है जैसा हम उचित समझें... तो यह रही स्वतंत्रता।",
    zh_title: "Huǐmiè de zìyuóu  huǐ miè de zì yóu",
    zh_content: "Kànqǐlái Shàngdì gěi le wǒmen àn zìjǐ yìyuàn huǐmiè shēnghuó de zìyuóu... zhè jiùshì zìyuóu de jiéguǒ.  kàn qǐ lái shàng dì gěi le wǒ men àn zì jǐ yì yuàn huǐ miè shēng huó de zì yóu ... zhè jiù shì zì yóu de jié guǒ 。"
});

MATCH (t:THOUGHT {name: "thought.FREEDOM TO RUIN"})
MATCH (c:CONTENT {name: "content.FREEDOM TO RUIN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FREEDOM TO RUIN" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.FREEDOM TO RUIN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->FREEDOM TO RUIN" }]->(child);
```

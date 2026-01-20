---
name: "thought.THE LORD GIVES"
alias: "Thought: Divine Sovereignty"
type: THOUGHT
en_content: "\"The Lord gives. The Lord takes away. Blessed be The Name of the Lord!\" -- The Prophet 'Iyowb (Job)"
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- blessing
- jodb
- lords_name
- trust
level: 2
neo4j: false
ptopic: 
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE LORD GIVES",
    alias: "Thought: Divine Sovereignty",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ["sovereignty", "blessing", "job", "lords_name", "trust"],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE LORD GIVES",
    en_title: "The Lord Gives",
    en_content: "\"The Lord gives. The Lord takes away. Blessed be The Name of the Lord!\" -- The Prophet 'Iyowb (Job)",
    es_title: "El Señor da",
    es_content: "\"El Señor dio y el Señor quitó; ¡bendito sea el nombre del Señor!\" -- El Profeta Iyowb (Job)",
    fr_title: "Le Seigneur donne",
    fr_content: "\"El Eterno ha dado, y el Eterno ha quitado; ¡bendito sea el nombre del Eterno!\" -- El Profeta Iyowb (Job)",
    hi_title: "bhagavaan deta hai",
    hi_content: "\"प्रभु ने दिया, प्रभु ने ले लिया। प्रभु का नाम धन्य हो!\" -- भविष्यद्वक्ता इय्याब (अय्यूब)",
    zh_title: "Yēhéhuá shǎngcì",
    zh_content: "“shǎng cì de shì yē hé huá, shǒu huí de yě shì yē hé huá ; yē hé huá de míng shì yīng dāng chéng sòng de!” -- xiān zhī yóu bó"
});

MATCH (t:THOUGHT {name: "thought.THE LORD GIVES"})
MATCH (c:CONTENT {name: "content.THE LORD GIVES"})
MERGE (t)-[:HAS_CONTENT {name: "edge.THE LORD GIVES"}]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.THE LORD GIVES"})
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE SOVEREIGNTY >THE LORD GIVES"}]->(child);
```

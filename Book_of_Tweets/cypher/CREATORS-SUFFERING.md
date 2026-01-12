---
name: "thought.CREATORS SUFFERING"
alias: "Thought: Creators Suffering"
type: THOUGHT
en_content: "Better for all of us to have gone to Hell than for Our Precious Creator to have suffered the way He did."
parent: "topic.THE GODHEAD"
tags:
- suffering
- atonement
- love
- sacrifice
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011c)
CREATE (t:THOUGHT {
    name: "thought.CREATORS SUFFERING",
    alias: "Thought: Creators Suffering",
    parent: "topic.THE GODHEAD",
    tags: ['suffering', 'atonement', 'love', 'sacrifice', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CREATORS SUFFERING",
    en_title: "Creators Suffering",
    en_content: "Better for all of us to have gone to Hell than for Our Precious Creator to have suffered the way He did.",
    es_title: "Sufrimiento del Creador",
    es_content: "Mejor que todos nosotros hubiéramos ido al infierno que nuestro Precioso Creador hubiera sufrido como lo hizo.",
    fr_title: "Souffrance du Créateur",
    fr_content: "Mieux vaut que nous allions tous en enfer plutôt que notre Précieux Créateur ait souffert comme Il l'a fait.",
    hi_title: "स्रष्टा का दुख",
    hi_content: "हम सभी के लिए नरक जाना बेहतर था कि हमारे कीमती स्रष्टा ने जैसा दुख उठाया।",
    zh_title: "Chuàngzào Zhě de Tòngkǔ",
    zh_content: "Wǒmen suǒyǒu rén dōu qù dìyù bǐ wǒmen bǎoguì de Chuàngzào Zhě shòu nàme duō tòngkǔ gèng hǎo."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CREATORS SUFFERING" AND c.name = "content.CREATORS SUFFERING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CREATORS SUFFERING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.CREATORS SUFFERING"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CREATORS SUFFERING" }]->(child);
```

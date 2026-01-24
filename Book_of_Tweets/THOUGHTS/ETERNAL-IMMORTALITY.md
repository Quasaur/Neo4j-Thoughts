---
name: "thought.ETERNAL IMMORTALITY"
alias: "Thought: Eternal Immortality"
type: THOUGHT
en_content: "If you die eternally, you're already dead; if you live eternally, you were always immortal!"
parent: "topic.THE GODHEAD"
tags:
- eternity
- immortality
- life
- death
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-May-2012b)
CREATE (t:THOUGHT {
    name: "thought.ETERNAL IMMORTALITY",
    alias: "Thought: Eternal Immortality",
    parent: "topic.THE GODHEAD",
    tags: ['eternity', 'immortality', 'life', 'death', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ETERNAL IMMORTALITY",
    en_title: "Eternal Immortality",
    en_content: "If you die eternally, you're already dead; if you live eternally, you were always immortal!",
    es_title: "Inmortalidad Eterna",
    es_content: "¡Si mueres eternamente, ya estás muerto; si vives eternamente, siempre fuiste inmortal!",
    fr_title: "Immortalité Éternelle",
    fr_content: "Si tu meurs éternellement, tu es déjà mort ; si tu vis éternellement, tu as toujours été immortel !",
    hi_title: "शाश्वत अमरता",
    hi_content: "यदि आप शाश्वत रूप से मरते हैं, तो आप पहले से ही मृत हैं; यदि आप शाश्वत रूप से जीते हैं, तो आप हमेशा अमर थे!",
    zh_title: "Yǒnghéng Bùsǐ",
    zh_content: "Rúguǒ nǐ yǒnghéng de sǐqù, nǐ yǐjīng sǐle; rúguǒ nǐ yǒnghéng de huózhe, nǐ yīzhí dōu shì bùsǐ de!"
});

MATCH (t:THOUGHT {name: "thought.ETERNAL IMMORTALITY"})
MATCH (c:CONTENT {name: "content.ETERNAL IMMORTALITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ETERNAL IMMORTALITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.ETERNAL IMMORTALITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->ETERNAL IMMORTALITY" }]->(child);
```

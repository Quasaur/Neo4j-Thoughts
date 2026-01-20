---
name: "thought.CHANGING EVIL TO RIGHTEOUS"
alias: "Thought: Changing Evil To Righteous"
type: THOUGHT
en_content: "God's Other Genius is changing evil people into righteous people!"
parent: "topic.THE GODHEAD"
tags:
- transformation
- grace
- genius
- god
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013d)
CREATE (t:THOUGHT {
    name: "thought.CHANGING EVIL TO RIGHTEOUS",
    alias: "Thought: Changing Evil To Righteous",
    parent: "topic.THE GODHEAD",
    tags: ['transformation', 'grace', 'genius', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CHANGING EVIL TO RIGHTEOUS",
    en_title: "Changing Evil To Righteous",
    en_content: "God's Other Genius is changing evil people into righteous people!",
    es_title: "Transformar al Malvado en Justo",
    es_content: "¡Otro Genio de Dios es transformar a las personas malvadas en personas justas!",
    fr_title: "Transformer le Méchant en Juste",
    fr_content: "L'autre génie de Dieu est de transformer les méchants en justes !",
    hi_title: "बुरे को धर्मी में बदलना",
    hi_content: "परमेश्वर की दूसरी प्रतिभा बुरे लोगों को धर्मी लोगों में बदलना है!",
    zh_title: "Jiāng Xié'è Biàn Wéi Zhèngyì",
    zh_content: "Shàngdì de lìng yī tiāncái shì jiāng xié'è de rén biàn wéi zhèngyì de rén!"
});

MATCH (t:THOUGHT {name: "thought.CHANGING EVIL TO RIGHTEOUS"})
MATCH (c:CONTENT {name: "content.CHANGING EVIL TO RIGHTEOUS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHANGING EVIL TO RIGHTEOUS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.CHANGING EVIL TO RIGHTEOUS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CHANGING EVIL TO RIGHTEOUS" }]->(child);
```

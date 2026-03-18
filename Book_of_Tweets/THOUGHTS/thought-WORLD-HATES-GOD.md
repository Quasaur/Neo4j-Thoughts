---
type: THOUGHT
name: "thought.WORLD HATES GOD"
alias: "Thought: World Hates God"
parent: "topic.HUMANITY"
en_content: "God loves the world. The world hates God. This is not going to end well for the world."
tags: ["world", "hate", "god", "judgment", "humanity"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Feb-2012b)
CREATE (t:THOUGHT {    name: "thought.WORLD HATES GOD",
    alias: "Thought: World Hates God",
    parent: "topic.HUMANITY",
    tags: ['world', 'hate', 'god', 'judgment', 'humanity'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.WORLD HATES GOD",
    ctype: "THOUGHT",
    en_title: "World Hates God",
    en_content: "God loves the world. The world hates God. This is not going to end well for the world.",
    es_title: "El Mundo Odia a Dios",
    es_content: "Dios ama al mundo. El mundo odia a Dios. Esto no va a terminar bien para el mundo.",
    fr_title: "Le Monde Déteste Dieu",
    fr_content: "Dieu aime le monde. Le monde déteste Dieu. Cela ne va pas bien finir pour le monde.",
    hi_title: "संसार परमेश्वर से घृणा करता है",
    hi_content: "परमेश्वर संसार से प्रेम करता है। संसार परमेश्वर से घृणा करता है। यह संसार के लिए अच्छा अंत नहीं होगा।",
    zh_title: "Shìjiè Hèn Shàngdì",
    zh_content: "Shàngdì ài shìjiè. Shìjiè hèn Shàngdì. Zhè duì shìjiè lái shuō bù huì yǒu hǎo jiéguǒ."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WORLD HATES GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->WORLD HATES GOD"
RETURN t, parent;
```

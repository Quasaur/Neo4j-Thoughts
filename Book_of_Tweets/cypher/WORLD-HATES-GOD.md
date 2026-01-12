---
name: "thought.WORLD HATES GOD"
alias: "Thought: World Hates God"
type: THOUGHT
en_content: "God loves the world. The world hates God. This is not going to end well for the world."
parent: "topic.HUMANITY"
tags:
- world
- hate
- god
- judgment
- humanity
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.WORLD HATES GOD",
    alias: "Thought: World Hates God",
    parent: "topic.HUMANITY",
    tags: ['world', 'hate', 'god', 'judgment', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WORLD HATES GOD",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WORLD HATES GOD" AND c.name = "content.WORLD HATES GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WORLD HATES GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.WORLD HATES GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >WORLD HATES GOD" }]->(child);
```

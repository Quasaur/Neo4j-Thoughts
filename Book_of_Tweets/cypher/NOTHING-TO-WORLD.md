---
name: "thought.NOTHING TO WORLD"
alias: "Thought: Nothing To World"
type: THOUGHT
en_content: "You cannot be something in God until you are nothing to the world."
parent: "topic.SPIRITUALITY"
tags:
- spirituality
- surrender
- world
- identity
- humility
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Dec-2011a)
CREATE (t:THOUGHT {
    name: "thought.NOTHING TO WORLD",
    alias: "Thought: Nothing To World",
    parent: "topic.SPIRITUALITY",
    tags: ['spirituality', 'surrender', 'world', 'identity', 'humility'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NOTHING TO WORLD",
    en_title: "Nothing To World",
    en_content: "You cannot be something in God until you are nothing to the world.",
    es_title: "Nada Para el Mundo",
    es_content: "No puedes ser algo en Dios hasta que no seas nada para el mundo.",
    fr_title: "Rien Pour le Monde",
    fr_content: "Tu ne peux être quelque chose en Dieu tant que tu n'es rien pour le monde.",
    hi_title: "संसार के लिए कुछ नहीं",
    hi_content: "तुम परमेश्वर में कुछ नहीं हो सकते जब तक तुम संसार के लिए कुछ नहीं नहीं हो।",
    zh_title: "Dui Shijie Wu Suo Wei",
    zh_content: "Zhi you dang ni dui shijie wu suo wei shi, ni cai neng zai Shen li cheng wei shen me."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOTHING TO WORLD" AND c.name = "content.NOTHING TO WORLD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING TO WORLD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.NOTHING TO WORLD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >NOTHING TO WORLD" }]->(child);
```

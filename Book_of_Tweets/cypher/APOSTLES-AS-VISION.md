---
name: "thought.APOSTLES AS VISION"
alias: "Thought: Apostles As Vision"
type: THOUGHT
en_content: "The Apostles loved Jesus' Vision because the Apostles WERE Jesus' Vision!"
parent: "topic.RELIGION"
tags:
- apostles
- vision
- jesus
- church
- history
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.APOSTLES AS VISION",
    alias: "Thought: Apostles As Vision",
    parent: "topic.RELIGION",
    tags: ['apostles', 'vision', 'jesus', 'church', 'history'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.APOSTLES AS VISION",
    en_title: "Apostles As Vision",
    en_content: "The Apostles loved Jesus' Vision because the Apostles WERE Jesus' Vision!",
    es_title: "Los Apóstoles como Visión",
    es_content: "¡Los Apóstoles amaban la Visión de Jesús porque los Apóstoles ERAN la Visión de Jesús!",
    fr_title: "Les Apôtres comme Vision",
    fr_content: "Les Apôtres aimaient la Vision de Jésus parce que les Apôtres ÉTAIENT la Vision de Jésus !",
    hi_title: "दृष्टि के रूप में प्रेरित",
    hi_content: "प्रेरितों ने यीशु की दृष्टि से प्यार किया क्योंकि प्रेरित यीशु की दृष्टि थे!",
    zh_title: "使徒作为异象",
    zh_content: "使徒们热爱耶稣的异象，因为使徒们就是耶稣的异象！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.APOSTLES AS VISION" AND c.name = "content.APOSTLES AS VISION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.APOSTLES AS VISION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.APOSTLES AS VISION"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >APOSTLES AS VISION" }]->(child);
```

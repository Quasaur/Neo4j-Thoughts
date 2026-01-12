---
name: "thought.JESUS THE MONARCH"
alias: "Thought: Jesus The Monarch"
type: THOUGHT
en_content: "Jesus is neither a Republican nor a Democrat; Jesus is God...an Absolute Monarch."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- monarchy
- authority
- politics
- divinity
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Aug-2010a)
CREATE (t:THOUGHT {
    name: "thought.JESUS THE MONARCH",
    alias: "Thought: Jesus The Monarch",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'monarchy', 'authority', 'politics', 'divinity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.JESUS THE MONARCH",
    en_title: "Jesus The Monarch",
    en_content: "Jesus is neither a Republican nor a Democrat; Jesus is God...an Absolute Monarch.",
    es_title: "Jesús el monarca",
    es_content: "Jesús no es ni republicano ni demócrata;Jesús es Dios... un Monarca Absoluto.",
    fr_title: "Jésus le monarque",
    fr_content: "Jésus n'est ni républicain ni démocrate ;Jésus est Dieu... un monarque absolu.",
    hi_title: "यीशु सम्राट",
    hi_content: "यीशु न तो रिपब्लिकन हैं और न ही डेमोक्रेट;यीशु ईश्वर हैं...एक पूर्ण सम्राट।",
    zh_title: "耶稣君王",
    zh_content: "耶稣既不是共和党人，也不是民主党人。耶稣是神……绝对的君主。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.JESUS THE MONARCH" AND c.name = "content.JESUS THE MONARCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.JESUS THE MONARCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.JESUS THE MONARCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >JESUS THE MONARCH" }]->(child);
```

---
type: THOUGHT
name: "thought.AMBITION"
alias: "Thought: Ambition"
parent: "topic.THE-GOSPEL"
tags: ["dailyroutine", "eating", "sleeping", "working", "discipline"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.AMBITION",
    alias: "Thought: Ambition",
    parent: "topic.THE-GOSPEL",
    tags: ["dailyroutine", "eating", "sleeping", "working", "discipline"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.AMBITION",
    ctype: "THOUGHT",
    en_title: "Ambition",
 es_title: "AMBICIÓN",
 fr_title: "AMBITION",
 hi_title: "महत्वाकांक्षा",
 zh_title: "zhì xiàng",
    en_content: "",
 es_content: "¡Dios es todo lo que quieres ser!",
 fr_content: "Dieu est tout ce que vous voulez être !",
 hi_content: "ईश्वर वह सब कुछ है जो आप बनना चाहते हैं!",
 zh_content: "shén jiù shì nǐ xiǎng chéng wéi de yī qiè ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AMBITION" AND c.name = "content.AMBITION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.AMBITION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.AMBITION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GOSPEL->AMBITION"}]->(child);
```
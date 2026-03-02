---
type: THOUGHT
name: "thought.ANXIETY"
alias: "Thought: ANXIETY"
parent: "topic.FAITH"
tags: ["peace", "faith", "carefree", "confident", "trust"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ANXIETY",
    alias: "Thought: ANXIETY",
    parent: "topic.FAITH",
    tags: ["peace", "faith", "carefree", "confident", "trust"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANXIETY",
    ctype: "THOUGHT",
    en_title: "ANXIETY",
    en_content: "Don't worry...be obedient!",
 es_title: "ANSIEDAD",
 es_content: "No te preocupes... ¡sé obediente!",
 fr_title: "ANXIÉTÉ",
 fr_content: "Ne vous inquiétez pas... soyez obéissant !",
 hi_title: "चिंता",
 hi_content: "चिंता मत करो...आज्ञाकारी बनो!",
 zh_title: "jiāo lǜ",
 zh_content: "bié dān xīn …… tīng huà ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANXIETY" AND c.name = "content.ANXIETY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.ANXIETY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.ANXIETY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITH->ANXIETY"}]->(child);
```
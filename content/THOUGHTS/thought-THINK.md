---
type: THOUGHT
name: "thought.THINK"
alias: "Thought: THINK"
parent: "topic.PSYCHOLOGY"
tags: ["think", "howto", "cognition", "critical", "logic"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THINK",
    alias: "Thought: THINK",
    parent: "topic.PSYCHOLOGY",
    tags: ["think", "howto", "cognition", "critical", "logic"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THINK",
    ctype: "THOUGHT",
    en_title: "THINK",
 es_title: "PENSAR",
 fr_title: "PENSE",
 hi_title: "सोचना",
 zh_title: "sī kǎo",
    en_content: "",
 es_content: "¿Crees que sabes pensar?",
 fr_content: "Pensez-vous que vous savez penser ?",
 hi_content: "क्या आपको लगता है कि आप सोचना जानते हैं?",
 zh_content: "nǐ rèn wéi nǐ zhī dào rú hé sī kǎo ma ？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THINK" AND c.name = "content.THINK"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.THINK"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.THINK"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->THINK"}]->(child);
```
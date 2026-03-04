---
type: THOUGHT
name: "thought.FOCUS"
alias: "Thought: Focus"
parent: "topic.PSYCHOLOGY"
tags: ["focus", "crisis", "forward", "criticalthinking", "faith"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FOCUS",
    alias: "Thought: Focus",
    parent: "topic.PSYCHOLOGY",
    tags: ["focus", "crisis", "forward", "criticalthinking", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FOCUS",
    ctype: "THOUGHT",
    en_title: "Focus",
 es_title: "ENFOCAR",
 fr_title: "SE CONCENTRER",
 hi_title: "केंद्र",
 zh_title: "zhòng diǎn",
    en_content: "",
 es_content: "Cuando tu espalda está contra la pared, no tienes que mirar hacia atrás.",
 fr_content: "Lorsque vous êtes dos au mur, vous n’avez pas besoin de regarder derrière vous.",
 hi_content: "जब आपकी पीठ दीवार से सटी हो तो आपको पीछे देखने की जरूरत नहीं है।",
 zh_content: "dāng nǐ bèi kào qiáng shí ， nǐ bù bì xiàng hòu kàn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FOCUS" AND c.name = "content.FOCUS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FOCUS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.FOCUS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->FOCUS"}]->(child);
```
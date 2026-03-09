---
type: THOUGHT
name: "thought.EMPATHY"
alias: "Thought: Empathy"
parent: "topic.LOVE"
tags: ["emptiness", "void", "hunger", "addiction", "spirituality"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.EMPATHY",
    alias: "Thought: Empathy",
    parent: "topic.LOVE",
    tags: ["emptiness", "void", "hunger", "addiction", "spirituality"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EMPATHY",
    ctype: "THOUGHT",
    en_title: "Empathy",
 es_title: "EMPATÍA",
 fr_title: "EMPATHIE",
 hi_title: "समानुभूति",
 zh_title: "gòng qíng",
    en_content: "",
 es_content: "Para AMARTE, debo ser tan tolerante con tus defectos como lo soy con los míos propios.",
 fr_content: "Pour t’aimer, je dois être aussi tolérante envers tes défauts que envers les miens.",
 hi_content: "आपसे प्यार करने के लिए, मुझे आपकी कमियों के प्रति उतना ही सहनशील होना होगा जितना कि अपनी कमियों के प्रति।",
 zh_content: "wèi le ài nǐ ， wǒ bì xū xiàng róng rěn wǒ zì jǐ de quē diǎn yī yàng róng rěn nǐ de quē diǎn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EMPATHY" AND c.name = "content.EMPATHY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.EMPATHY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LOVE" AND child.name = "thought.EMPATHY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.LOVE->EMPATHY"}]->(child);
```
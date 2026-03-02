---
type: THOUGHT
name: "thought.PERSEVERANCE"
alias: "Thought: PERSEVERANCE"
parent: "topic.ATTITUDE"
tags: ["persistence", "failure", "quitting", "consequence", "success"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PERSEVERANCE",
    alias: "Thought: PERSEVERANCE",
    parent: "topic.ATTITUDE",
    tags: ["persistence", "failure", "quitting", "consequence", "success"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PERSEVERANCE",
    ctype: "THOUGHT",
    en_title: "PERSEVERANCE",
 es_title: "PERSERVERANCIA",
 fr_title: "PERSÉVÉRANCE",
 hi_title: "दृढ़ता",
 zh_title: "yì lì",
    en_content: "",
 es_content: "El fracaso está asegurado para quien deja de intentarlo.",
 fr_content: "L'échec est assuré à celui qui cesse d'essayer.",
 hi_content: "जो प्रयास करना बंद कर देता है, उसकी असफलता निश्चित है।",
 zh_content: "duì yú tíng zhǐ cháng shì de rén lái shuō ， shī bài shì zhù dìng de 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PERSEVERANCE" AND c.name = "content.PERSEVERANCE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.PERSEVERANCE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.PERSEVERANCE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->PERSEVERANCE"}]->(child);
```
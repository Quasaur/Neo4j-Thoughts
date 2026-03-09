---
type: THOUGHT
name: "thought.UNFORGIVENESS"
alias: "Thought: Unforgiveness"
parent: "topic.ATTITUDE"
tags: ["unforgiveness", "hell", "unmerciful", "condemnation", "salvation"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.UNFORGIVENESS",
    alias: "Thought: Unforgiveness",
    parent: "topic.ATTITUDE",
    tags: ["unforgiveness", "hell", "unmerciful", "condemnation", "salvation"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNFORGIVENESS",
    ctype: "THOUGHT",
    en_title: "Unforgiveness",
 es_title: "PERDÓN",
 fr_title: "IMPARDONNANCE",
 hi_title: "क्षमा न करना",
 zh_title: "bù kě ráo shù",
    en_content: "",
 es_content: "¡Las ÚNICAS personas que van al infierno son aquellas que NO PODRÍAN PERDONAR!",
 fr_content: "Les SEULS gens qui vont en Enfer sont ceux qui NE PEUVENT PAS PARDONNER !",
 hi_content: "नर्क में जाने वाले केवल वही लोग हैं जो क्षमा नहीं कर सकते!",
 zh_content: "wéi yī xià dì yù de rén jiù shì nà xiē wú fǎ kuān shù de rén ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNFORGIVENESS" AND c.name = "content.UNFORGIVENESS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.UNFORGIVENESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.UNFORGIVENESS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->UNFORGIVENESS"}]->(child);
```
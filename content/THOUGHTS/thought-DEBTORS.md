---
type: THOUGHT
name: "thought.DEBTORS"
alias: "Thought: DEBTORS"
parent: "topic.ECONOMICS"
tags: ["economics", "nation", "debtors", "slaves", "liability"]
ptopic: "[[topic-ECONOMICS]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DEBTORS",
    alias: "Thought: DEBTORS",
    parent: "topic.ECONOMICS",
    tags: ["economics", "nation", "debtors", "slaves", "liability"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEBTORS",
    ctype: "THOUGHT",
    en_title: "DEBTORS",
    en_content: "A nation of debtors is a nation of slaves.",
 es_title: "DEUDORES",
 es_content: "Una nación de deudores es una nación de esclavos.",
 fr_title: "DÉBITEURS",
 fr_content: "Une nation de débiteurs est une nation d’esclaves.",
 hi_title: "देनदार",
 hi_content: "कर्ज़दारों का राष्ट्र गुलामों का राष्ट्र होता है।",
 zh_title: "zhài wù rén",
 zh_content: "yí gè zhài wù rén de guó jiā jiù shì yí gè nú lì de guó jiā 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEBTORS" AND c.name = "content.DEBTORS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.DEBTORS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ECONOMICS" AND child.name = "thought.DEBTORS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ECONOMICS->DEBTORS"}]->(child);
```
---
type: THOUGHT
name: "thought.COWARDS"
alias: "Thought: The Terrorist Delusion"
en_content: "Terrorists and freedom fighters are children of the Devil...COWARDS...just like their daddy."
tags: ["terrorists", "freedom_fighters", "cowards", "children", "satan"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---






```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.COWARDS",
    alias: "Thought: The Terrorist Delusion",
    parent: "topic.EVIL",
    tags: ["terrorists", "freedom_fighters", "cowards", "children", "satan"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.COWARDS",
    ctype: "THOUGHT",
    en_title: "Cowards",
    en_content: "Terrorists and freedom fighters are children of the Devil...COWARDS...just like their daddy.",
    es_title: "Cobardes",
    es_content: "Los terroristas y los luchadores por la libertad son hijos del diablo... COBARDES... igual que su papá.",
    fr_title: "Lâches",
    fr_content: "Les terroristes et les combattants de la liberté sont des enfants du Diable... des lâches... tout comme leur père.",
    hi_title: "कायर",
    hi_content: "आतंकवादी और स्वतंत्रता सेनानी शैतान के बच्चे हैं...कायर...ठीक अपने बाप की तरह।",
    zh_title: "Nuòfū",
    zh_content: "kǒngbù fèn zǐ hé zìyóu zhànshì dōu shì móguǐ de zǐsì……nuòfū……jiù xiàng tāmen de lǎo diē yīyàng."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.COWARDS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->COWARDS"
RETURN t, parent;
```

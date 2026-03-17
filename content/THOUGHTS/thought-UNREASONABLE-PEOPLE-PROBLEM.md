---
type: THOUGHT
name: "thought.UNREASONABLE PEOPLE PROBLEM"
alias: "Thought: Unreasonable People Problem"
parent: "topic.WISDOM"
en_content: "Life would be perfect but for the presence of unreasonable people."
tags: ["people", "reason", "life", "attitude", "problem"]
ptopic: "[[topic-WISDOM]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.UNREASONABLE PEOPLE PROBLEM",
    alias: "Thought: Unreasonable People Problem",
    parent: "topic.WISDOM",
    tags: ['people', 'reason', 'life', 'attitude', 'problem'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNREASONABLE PEOPLE PROBLEM",
    ctype: "THOUGHT",
    en_title: "Unreasonable People Problem",
    en_content: "Life would be perfect but for the presence of unreasonable people.",
    es_title: "El Problema de la Gente Irrazonable",
    es_content: "La vida sería perfecta si no fuera por la presencia de personas irrazonables.",
    fr_title: "Le Problème des Gens Déraisonnables",
    fr_content: "La vie serait parfaite sans la présence de personnes déraisonnables.",
    hi_title: "अतार्किक लोगों की समस्या",
    hi_content: "जीवन संपूर्ण होता लेकिन अतार्किक लोगों की उपस्थिति इसे बिगाड़ देती है।",
    zh_title: "Bù lǐxìng zhī rén de wèntí 不理性之人的问题",
    zh_content: "Rúguǒ bù shì yīnwèi bù lǐxìng zhī rén de cúnzài, shēnghuó jiàng shì wánměi de. 如果不是因为不理性之人的存在，生活将是完美的。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNREASONABLE PEOPLE PROBLEM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->UNREASONABLE PEOPLE PROBLEM"
RETURN t, parent;
```

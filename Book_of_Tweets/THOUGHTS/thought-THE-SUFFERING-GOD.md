---
type: THOUGHT
name: "thought.THE SUFFERING GOD"
alias: "Thought: The Suffering God"
parent: "topic.THE GODHEAD"
en_content: "In Christ God has suffered more than any human."
tags: ["suffering", "empathy", "christ", "incarnation", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011e)
CREATE (t:THOUGHT {    name: "thought.THE SUFFERING GOD",
    alias: "Thought: The Suffering God",
    parent: "topic.THE GODHEAD",
    tags: ['suffering', 'empathy', 'christ', 'incarnation', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.THE SUFFERING GOD",
    ctype: "THOUGHT",
    en_title: "The Suffering God",
    en_content: "In Christ God has suffered more than any human.",
    es_title: "El Dios que Sufre",
    es_content: "En Cristo, Dios ha sufrido más que cualquier ser humano.",
    fr_title: "Le Dieu Souffrant",
    fr_content: "En Christ, Dieu a souffert plus que tout être humain.",
    hi_title: "दुःख सहने वाले परमेश्वर",
    hi_content: "मसीह में परमेश्वर ने किसी भी मनुष्य से अधिक दुःख सहा है।",
    zh_title: "Shòukǔ de Shàngdì",
    zh_content: "Zài Jīdū lǐ, Shàngdì bǐ rènhé rén dōu chéngshòu le gèng duō de kǔnàn."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.THE SUFFERING GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->THE SUFFERING GOD"
RETURN t, parent;
```

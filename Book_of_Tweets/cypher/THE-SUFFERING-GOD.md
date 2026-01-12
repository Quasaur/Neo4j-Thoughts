---
name: "thought.THE SUFFERING GOD"
alias: "Thought: The Suffering God"
type: THOUGHT
en_content: "In Christ God has suffered more than any human."
parent: "topic.THE GODHEAD"
tags:
- suffering
- empathy
- christ
- incarnation
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011e)
CREATE (t:THOUGHT {
    name: "thought.THE SUFFERING GOD",
    alias: "Thought: The Suffering God",
    parent: "topic.THE GODHEAD",
    tags: ['suffering', 'empathy', 'christ', 'incarnation', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.THE SUFFERING GOD",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE SUFFERING GOD" AND c.name = "content.THE SUFFERING GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE SUFFERING GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.THE SUFFERING GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >THE SUFFERING GOD" }]->(child);
```

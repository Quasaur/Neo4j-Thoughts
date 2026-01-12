---
name: "thought.MOTHER OF JESUS"
alias: "Thought: Mother Of Jesus"
type: THOUGHT
en_content: "Mary is the BIOLOGICAL mother of Jesus, not the SPIRITUAL mother of God."
parent: "topic.THE GODHEAD"
tags:
- mary
- jesus
- divinity
- theology
- incarnation
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011c)
CREATE (t:THOUGHT {
    name: "thought.MOTHER OF JESUS",
    alias: "Thought: Mother Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['mary', 'jesus', 'divinity', 'theology', 'incarnation'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MOTHER OF JESUS",
    en_title: "Mother Of Jesus",
    en_content: "Mary is the BIOLOGICAL mother of Jesus, not the SPIRITUAL mother of God.",
    es_title: "Madre de Jesús",
    es_content: "María es la madre BIOLÓGICA de Jesús, no la madre ESPIRITUAL de Dios.",
    fr_title: "Mère de Jésus",
    fr_content: "Marie est la mère BIOLOGIQUE de Jésus, non la mère SPIRITUELLE de Dieu.",
    hi_title: "यीशु की माता",
    hi_content: "मरियम यीशु की जैविक माता है, परमेश्वर की आध्यात्मिक माता नहीं।",
    zh_title: "Yesu de muqin",
    zh_content: "Maliya shi Yesu de shengwu muqin, bushi Shen de shengling muqin."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MOTHER OF JESUS" AND c.name = "content.MOTHER OF JESUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MOTHER OF JESUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MOTHER OF JESUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >MOTHER OF JESUS" }]->(child);
```

---
name: "thought.KINDNESS OF JESUS"
alias: "Thought: Kindness Of Jesus"
type: THOUGHT
en_content: "I have NEVER met anyone more kind that Jesus...and I never will!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- kindness
- love
- divinity
- compassion
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2010b)
CREATE (t:THOUGHT {
    name: "thought.KINDNESS OF JESUS",
    alias: "Thought: Kindness Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'kindness', 'love', 'divinity', 'compassion'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.KINDNESS OF JESUS",
    en_title: "Kindness Of Jesus",
    en_content: "I have NEVER met anyone more kind that Jesus...and I never will!",
    es_title: "Bondad de Jesús",
    es_content: "NUNCA he conocido a nadie más amable que Jesús... ¡y nunca lo haré!",
    fr_title: "La bonté de Jésus",
    fr_content: "Je n'ai JAMAIS rencontré quelqu'un de plus gentil que Jésus... et je ne le ferai jamais !",
    hi_title: "यीशु की दयालुता",
    hi_content: "मैं यीशु से अधिक दयालु किसी व्यक्ति से कभी नहीं मिला...और मैं कभी नहीं मिलूंगा!",
    zh_title: "耶稣的仁慈",
    zh_content: "我从来没有遇到过比耶稣更仁慈的人……我永远也不会！"
});

MATCH (t:THOUGHT {name: "thought.KINDNESS OF JESUS"})
MATCH (c:CONTENT {name: "content.KINDNESS OF JESUS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.KINDNESS OF JESUS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.KINDNESS OF JESUS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->KINDNESS OF JESUS" }]->(child);
```

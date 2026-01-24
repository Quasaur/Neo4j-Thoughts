---
name: "thought.HAPPY IF GOD PLEASED"
alias: "Thought: Happy If God Pleased"
type: THOUGHT
en_content: How can I not be happy if God is pleased with me?
parent: topic.WORSHIP
tags:
  - happiness
  - pleasure
  - god
  - attitude
level: 3
neo4j: true
ptopic: "[[topic-WORSHIP]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Mar-2014)
CREATE (t:THOUGHT {
    name: "thought.HAPPY IF GOD PLEASED",
    alias: "Thought: Happy If God Pleased",
    parent: "topic.ATTITUDE",
    tags: ['happiness', 'pleasure', 'god', 'attitude'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HAPPY IF GOD PLEASED",
    en_title: "Happy If God Pleased",
    en_content: "How can I not be happy if God is pleased with me?",
    es_title: "Feliz Si Dios Está Complacido",
    es_content: "¿Cómo no puedo estar feliz si Dios está complacido conmigo?",
    fr_title: "Heureux Si Dieu Est Satisfait",
    fr_content: "Comment ne puis-je pas être heureux si Dieu est satisfait de moi ?",
    hi_title: "खुश यदि भगवान प्रसन्न हैं",
    hi_content: "यदि भगवान मुझसे प्रसन्न हैं तो मैं कैसे खुश नहीं हो सकता?",
    zh_title: "Ruò Shén Xǐyuè Zé Kuàilè",
    zh_content: "Rúguǒ Shén duì wǒ mǎnyì, wǒ zěnme néng bù kuàilè ne?"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HAPPY IF GOD PLEASED" AND c.name = "content.HAPPY IF GOD PLEASED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HAPPY IF GOD PLEASED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HAPPY IF GOD PLEASED"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->HAPPY IF GOD PLEASED" }]->(child);
```

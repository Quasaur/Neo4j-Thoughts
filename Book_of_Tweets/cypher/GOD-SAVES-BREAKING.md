---
name: "thought.GOD SAVES BREAKING"
alias: "Thought: God Saves Breaking"
type: THOUGHT
en_content: "God will save you...after He breaks you. Matthew 21:44"
parent: "topic.GRACE"
tags:
- salvation
- breaking
- grace
- god
- transformation
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD SAVES BREAKING",
    alias: "Thought: God Saves Breaking",
    parent: "topic.GRACE",
    tags: ['salvation', 'breaking', 'grace', 'god', 'transformation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GOD SAVES BREAKING",
    en_title: "God Saves Breaking",
    en_content: "God will save you...after He breaks you. Matthew 21:44",
    es_title: "Dios Salva Quebrantando",
    es_content: "Dios te salvará...después de quebrantarte. Mateo 21:44",
    fr_title: "Dieu Sauve en Brisant",
    fr_content: "Dieu te sauvera...après t'avoir brisé. Matthieu 21:44",
    hi_title: "परमेश्वर तोड़कर बचाता है",
    hi_content: "परमेश्वर तुम्हें बचाएगा...तुम्हें तोड़ने के बाद। मत्ती 21:44",
    zh_title: "Shén Pòsuì Ér Zhěngjiù",
    zh_content: "Shén huì zhěngjiù nǐ...zài Tā pòsuì nǐ zhīhòu. Mǎtàifúyīn 21:44"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD SAVES BREAKING" AND c.name = "content.GOD SAVES BREAKING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD SAVES BREAKING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.GOD SAVES BREAKING"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >GOD SAVES BREAKING" }]->(child);
```

---
name: "thought.SAVED FROM GOD"
alias: "Thought: Saved From God"
type: THOUGHT
en_content: "God can save you from anybody...but who can save you from God?"
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- salvation
- sovereignty
- power
- judgment
- mercy
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Nov-2010)
CREATE (t:THOUGHT {
    name: "thought.SAVED FROM GOD",
    alias: "Thought: Saved From God",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['salvation', 'sovereignty', 'power', 'judgment', 'mercy'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SAVED FROM GOD",
    en_title: "Saved From God",
    en_content: "God can save you from anybody...but who can save you from God?",
    es_title: "Salvado de Dios",
    es_content: "Dios puede salvarte de cualquiera...pero ¿quién puede salvarte de Dios?",
    fr_title: "Sauvé de Dieu",
    fr_content: "Dieu peut vous sauver de n'importe qui...mais qui peut vous sauver de Dieu ?",
    hi_title: "परमेश्वर से छुटकारा",
    hi_content: "परमेश्वर आपको किसी से भी बचा सकता है...लेकिन कौन आपको परमेश्वर से बचा सकता है?",
    zh_title: "Cóng Shàngdì Zhōng Déjiù",
    zh_content: "Shàngdì kěyǐ jiù nǐ tuōlí rènhé rén...dàn shuí néng jiù nǐ tuōlí Shàngdì ne?"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SAVED FROM GOD" AND c.name = "content.SAVED FROM GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SAVED FROM GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.SAVED FROM GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >SAVED FROM GOD" }]->(child);
```

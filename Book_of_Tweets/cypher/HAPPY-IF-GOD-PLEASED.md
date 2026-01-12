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
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HAPPY IF GOD PLEASED" AND c.name = "content.HAPPY IF GOD PLEASED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HAPPY IF GOD PLEASED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HAPPY IF GOD PLEASED"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >HAPPY IF GOD PLEASED" }]->(child);
```

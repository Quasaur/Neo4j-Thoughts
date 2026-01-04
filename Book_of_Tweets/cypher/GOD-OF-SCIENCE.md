---
name: "thought.GOD OF SCIENCE"
alias: "Thought: God Of Science"
type: THOUGHT
en_content: "Jesus Christ is The God of Wisdom, Knowledge, Science and Technology."
parent: "topic.THE GODHEAD"
tags:
- jesus
- science
- technology
- wisdom
- knowledge
level: 1
neo4j: true
insert: true
---
# God Of Science

> [!Thought-en]
> Jesus Christ is The God of Wisdom, Knowledge, Science and Technology.

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jun-2011a)
CREATE (t:THOUGHT {
    name: "thought.GOD OF SCIENCE",
    alias: "Thought: God Of Science",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'science', 'technology', 'wisdom', 'knowledge'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD OF SCIENCE",
    en_title: "God Of Science",
    en_content: "Jesus Christ is The God of Wisdom, Knowledge, Science and Technology.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD OF SCIENCE" AND c.name = "content.GOD OF SCIENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD OF SCIENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD OF SCIENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD OF SCIENCE" }]->(child);
```
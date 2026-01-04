---
name: "thought.ANGER AND PAIN"
alias: "Thought: Anger And Pain"
type: THOUGHT
parent: "topic.PSYCHOLOGY"
tags:
- anger
- pain
- psychology
- response
- character
level: 3
neo4j: true
insert: true
---
# Anger And Pain

> [!Thought-en]
> Anger as a first response is often indicative of an underlying issue...that issue usually being pain.

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2012b)
CREATE (t:THOUGHT {
    name: "thought.ANGER AND PAIN",
    alias: "Thought: Anger And Pain",
    parent: "topic.PSYCHOLOGY",
    tags: ['anger', 'pain', 'psychology', 'response', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ANGER AND PAIN",
    en_title: "Anger And Pain",
    en_content: "Anger as a first response is often indicative of an underlying issue...that issue usually being pain.",
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
WHERE t.name = "thought.ANGER AND PAIN" AND c.name = "content.ANGER AND PAIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ANGER AND PAIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.ANGER AND PAIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >ANGER AND PAIN" }]->(child);
```
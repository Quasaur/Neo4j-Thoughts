---
name: "thought.EDUCATION AND SCRIPTURE"
alias: "Thought: Education And Scripture"
type: THOUGHT
parent: "topic.TRUTH"
tags:
- education
- scripture
- bible
- survey
- truth
level: 2
neo4j: true
insert: true
---
# Education And Scripture

> [!Thought-en]
> How can anyone be considered educated without having surveyed the Holy Scriptures?

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.EDUCATION AND SCRIPTURE",
    alias: "Thought: Education And Scripture",
    parent: "topic.TRUTH",
    tags: ['education', 'scripture', 'bible', 'survey', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EDUCATION AND SCRIPTURE",
    en_title: "Education And Scripture",
    en_content: "How can anyone be considered educated without having surveyed the Holy Scriptures?",
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
WHERE t.name = "thought.EDUCATION AND SCRIPTURE" AND c.name = "content.EDUCATION AND SCRIPTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EDUCATION AND SCRIPTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.EDUCATION AND SCRIPTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >EDUCATION AND SCRIPTURE" }]->(child);
```
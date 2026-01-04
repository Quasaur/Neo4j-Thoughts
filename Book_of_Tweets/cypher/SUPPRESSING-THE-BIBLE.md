---
name: "thought.SUPPRESSING THE BIBLE"
alias: "Thought: Suppressing The Bible"
type: THOUGHT
parent: "topic.TRUTH"
tags:
- bible
- satan
- truth
- deception
- revelation
level: 2
neo4j: true
insert: true
---
# Suppressing The Bible

> [!Thought-en]
> Where Satan cannot suppress the distribution of the Bible he has convinced the population to stay away from it.

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.SUPPRESSING THE BIBLE",
    alias: "Thought: Suppressing The Bible",
    parent: "topic.TRUTH",
    tags: ['bible', 'satan', 'truth', 'deception', 'revelation'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SUPPRESSING THE BIBLE",
    en_title: "Suppressing The Bible",
    en_content: "Where Satan cannot suppress the distribution of the Bible he has convinced the population to stay away from it.",
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
WHERE t.name = "thought.SUPPRESSING THE BIBLE" AND c.name = "content.SUPPRESSING THE BIBLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SUPPRESSING THE BIBLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.SUPPRESSING THE BIBLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >SUPPRESSING THE BIBLE" }]->(child);
```
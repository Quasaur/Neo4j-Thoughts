---
name: "thought.TWO GARDENS"
alias: "Thought: Two Gardens"
type: THOUGHT
en_content: "In the Bible there are 2 gardens. In the 1st garden are 2 trees; in the 2nd garden is only 1 tree. What happened to the 2nd tree?"
parent: "topic.CREATION"
tags:
- bible
- creation
- eden
- paradise
- symbolism
level: 2
neo4j: true
insert: true
---
# Two Gardens

> [!Thought-en]
> In the Bible there are 2 gardens. In the 1st garden are 2 trees; in the 2nd garden is only 1 tree. What happened to the 2nd tree?

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Feb-2011)
CREATE (t:THOUGHT {
    name: "thought.TWO GARDENS",
    alias: "Thought: Two Gardens",
    parent: "topic.CREATION",
    tags: ['bible', 'creation', 'eden', 'paradise', 'symbolism'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TWO GARDENS",
    en_title: "Two Gardens",
    en_content: "In the Bible there are 2 gardens. In the 1st garden are 2 trees; in the 2nd garden is only 1 tree. What happened to the 2nd tree?",
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
WHERE t.name = "thought.TWO GARDENS" AND c.name = "content.TWO GARDENS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TWO GARDENS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.TWO GARDENS"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >TWO GARDENS" }]->(child);
```
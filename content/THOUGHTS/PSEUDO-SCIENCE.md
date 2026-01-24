---
name: "thought.PSEUDO_SCIENCE"
alias: "Thought: PSEUDO-SCIENCE"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- science
- divinity
- pseudoscience
- truth
- deity
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PSEUDO_SCIENCE",
    alias: "Thought: PSEUDO-SCIENCE",
    parent: "topic.COSMOLOGY",
    tags: ["science", "divinity", "pseudoscience", "truth", "deity"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PSEUDO_SCIENCE",
    en_title: "PSEUDO-SCIENCE",
    en_content: "There is no science without God.",
    es_title: "PSEUDO-CIENCIA",
    es_content: "No hay ciencia sin Dios.",
    fr_title: "PSEUDO-SCIENCE",
    fr_content: "Il n'y a pas de science sans Dieu.",
    hi_title: "छद्म विज्ञान",
    hi_content: "ईश्वर के बिना कोई विज्ञान नहीं है।",
    zh_title: "wěi kē xué",
    zh_content: "méi yǒu shàng dì jiù méi yǒu kē xué 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PSEUDO_SCIENCE" AND c.name = "content.PSEUDO_SCIENCE"
MERGE (t)-[:HAS_CONTENT {name: "edge.PSEUDO_SCIENCE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.PSEUDO_SCIENCE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.COSMOLOGY->PSEUDO_SCIENCE"}]->(child);
```

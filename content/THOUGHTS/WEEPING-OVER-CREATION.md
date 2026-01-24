---
name: "thought.WEEPING OVER CREATION"
alias: "Thought: Ecological Care"
type: THOUGHT
en_content: "(Weeping over BP Oil Spill)."
parent: "topic.ENVIRONMENTAL SCIENCE"
tags:
- creation
- sorrow
- environment
- stewardship
- pollution
level: 6
neo4j: true
ptopic: "[[topic-ENVIRONMENTAL-SCIENCE]]"
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.WEEPING OVER CREATION",
    alias: "Thought: Ecological Care",
    parent: "topic.ENVIRONMENTAL SCIENCE",
    tags: ["creation", "sorrow", "environment", "stewardship", "pollution"],
    notes: "",
    level: 6
});

CREATE (c:CONTENT {
    name: "content.WEEPING OVER CREATION",
    en_title: "Weeping over Creation",
    en_content: "(Weeping over BP Oil Spill).",
    es_title: "Llorando por creación",
    es_content: "(Llorando por el derrame de petróleo de BP).",
    fr_title: "Pleurs sur la création",
    fr_content: "(Pleurant sur la marée noire de BP).",
    hi_title: "srshti par rona",
    hi_content: "(बीपी तेल रिसाव पर रोते हुए)।",
    zh_title: "Wèi chuàngzào kūqì",
    zh_content: "( wèi BP shí yóu xiè lòu kū qì )."
});

MATCH (t:THOUGHT {name: "thought.WEEPING OVER CREATION"})
MATCH (c:CONTENT {name: "content.WEEPING OVER CREATION"})
MERGE (t)-[:HAS_CONTENT {name: "edge.WEEPING OVER CREATION"}]->(c);

MATCH (parent:TOPIC {name: "topic.ENVIRONMENTAL SCIENCE"})
MATCH (child:THOUGHT {name: "thought.WEEPING OVER CREATION"})
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ENVIRONMENTAL SCIENCE>WEEPING OVER CREATION"}]->(child);
```

---
name: "thought.WEEPING OVER CREATION"
alias: "Thought: Ecological Care"
type: THOUGHT
en_content: "(Weeping over BP Oil Spill)."
parent: "topic.CREATION"
tags:
- creation
- sorrow
- environment
- stewardship
- pollution
level: 2
neo4j: true
insert: true
---
# Weeping over Creation

> [!Thought-en]
> (Weeping over BP Oil Spill).

```Cypher
CREATE (t:THOUGHT {
    name: "thought.WEEPING OVER CREATION",
    alias: "Thought: Ecological Care",
    parent: "topic.CREATION",
    tags: ["creation", "sorrow", "environment", "stewardship", "pollution"],
    notes: "",
    level: 2
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
    zh_title: "wèi chuàng zào kū qì",
    zh_content: "( wèi BP shí yóu xiè lòu kū qì )."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WEEPING OVER CREATION" AND c.name = "content.WEEPING OVER CREATION"
MERGE (t)-[:HAS_CONTENT {name: "edge.WEEPING OVER CREATION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.WEEPING OVER CREATION"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION >WEEPING OVER CREATION"}]->(child);
```

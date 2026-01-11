---
name: "thought.DARK_MATTER"
alias: "Thought: DARK MATTER"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- genesis
- creation
- universe
- waters
- science
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DARK_MATTER",
    alias: "Thought: DARK MATTER",
    parent: "topic.COSMOLOGY",
    tags: ["genesis", "creation", "universe", "waters", "science"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DARK_MATTER",
    en_title: "DARK MATTER",
    en_content: "What if dark matter is a type of WATER?",
    es_title: "MATERIA OSCURA",
    es_content: "¿Y si la materia oscura fuera un tipo de AGUA?",
    fr_title: "MATIÈRE NOIRE",
    fr_content: "Et si la matière noire était un type d’EAU ?",
    hi_title: "गहरे द्रव्य",
    hi_content: "क्या होगा यदि डार्क मैटर पानी का एक प्रकार है?",
    zh_title: "àn wù zhì",
    zh_content: "rú guǒ àn wù zhì shì shuǐ de yī zhǒng zěn me bàn ？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DARK_MATTER" AND c.name = "content.DARK_MATTER"
MERGE (t)-[:HAS_CONTENT {name: "edge.DARK_MATTER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.DARK_MATTER"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.COSMOLOGY->DARK_MATTER"}]->(child);
```

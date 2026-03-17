---
type: THOUGHT
name: "thought.DARK MATTER"
alias: "Thought: Dark Matter"
parent: "topic.COSMOLOGY"
en_content: "What if dark matter is a type of WATER?"
tags: ["genesis", "creation", "universe", "waters", "science"]
ptopic: "[[topic-COSMOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DARK MATTER",
    alias: "Thought: Dark Matter",
    parent: "topic.COSMOLOGY",
    tags: ["genesis", "creation", "universe", "waters", "science"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DARK MATTER",
    ctype: "THOUGHT",
    en_title: "Dark Matter",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DARK MATTER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.COSMOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.COSMOLOGY->DARK MATTER"
RETURN t, parent;
```

---
name: "thought.BOX JELLYFISH EYES"
alias: "Thought: Box Jellyfish Eyes"
type: THOUGHT
en_content: "The box jellyfish--nature's most poisonous creature--has 24 eyes and 360-degree vision...God is great!"
parent: "topic.CREATION"
tags:
- creation
- nature
- jellyfish
- design
- power
level: 2
neo4j: true
insert: true
---
# Box Jellyfish Eyes

> [!Thought-en]
> The box jellyfish--nature's most poisonous creature--has 24 eyes and 360-degree vision...God is great!

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Aug-2011a)
CREATE (t:THOUGHT {
    name: "thought.BOX JELLYFISH EYES",
    alias: "Thought: Box Jellyfish Eyes",
    parent: "topic.CREATION",
    tags: ['creation', 'nature', 'jellyfish', 'design', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BOX JELLYFISH EYES",
    en_title: "Box Jellyfish Eyes",
    en_content: "The box jellyfish--nature's most poisonous creature--has 24 eyes and 360-degree vision...God is great!",
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
WHERE t.name = "thought.BOX JELLYFISH EYES" AND c.name = "content.BOX JELLYFISH EYES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BOX JELLYFISH EYES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.BOX JELLYFISH EYES"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >BOX JELLYFISH EYES" }]->(child);
```
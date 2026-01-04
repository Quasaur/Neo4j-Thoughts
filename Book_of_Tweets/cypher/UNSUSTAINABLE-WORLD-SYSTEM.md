---
name: "thought.UNSUSTAINABLE WORLD SYSTEM"
alias: "Thought: Unsustainable World System"
type: THOUGHT
en_content: "I believe the Hebrew Scriptures...this world system is unsustainable."
parent: "topic.HUMANITY"
tags:
- humanity
- world
- society
- bible
- truth
level: 3
neo4j: true
insert: true
---
# Unsustainable World System

> [!Thought-en]
> I believe the Hebrew Scriptures...this world system is unsustainable.

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.UNSUSTAINABLE WORLD SYSTEM",
    alias: "Thought: Unsustainable World System",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'world', 'society', 'bible', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNSUSTAINABLE WORLD SYSTEM",
    en_title: "Unsustainable World System",
    en_content: "I believe the Hebrew Scriptures...this world system is unsustainable.",
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
WHERE t.name = "thought.UNSUSTAINABLE WORLD SYSTEM" AND c.name = "content.UNSUSTAINABLE WORLD SYSTEM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNSUSTAINABLE WORLD SYSTEM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.UNSUSTAINABLE WORLD SYSTEM"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >UNSUSTAINABLE WORLD SYSTEM" }]->(child);
```
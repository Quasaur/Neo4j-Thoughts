---
name: "thought.WICKEDNESS AND GUN LAWS"
alias: "Thought: Wickedness And Gun Laws"
type: THOUGHT
en_content: "Humanity will continue to grow more wicked. As a nation we would be IDIOTS to leave our gun laws in their current state."
parent: "topic.MORALITY"
tags:
- guns
- law
- wickedness
- morality
- society
level: 3
neo4j: true
insert: true
---
# Wickedness And Gun Laws

> [!Thought-en]
> Humanity will continue to grow more wicked. As a nation we would be IDIOTS to leave our gun laws in their current state.

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.WICKEDNESS AND GUN LAWS",
    alias: "Thought: Wickedness And Gun Laws",
    parent: "topic.MORALITY",
    tags: ['guns', 'law', 'wickedness', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WICKEDNESS AND GUN LAWS",
    en_title: "Wickedness And Gun Laws",
    en_content: "Humanity will continue to grow more wicked. As a nation we would be IDIOTS to leave our gun laws in their current state.",
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
WHERE t.name = "thought.WICKEDNESS AND GUN LAWS" AND c.name = "content.WICKEDNESS AND GUN LAWS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WICKEDNESS AND GUN LAWS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.WICKEDNESS AND GUN LAWS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >WICKEDNESS AND GUN LAWS" }]->(child);
```
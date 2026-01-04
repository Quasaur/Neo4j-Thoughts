---
name: "thought.OPPRESSIVE WEALTH"
alias: "Thought: Oppressive Wealth"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- wealth
- oppression
- justice
- bible
- accuracy
- morality
level: 3
neo4j: true
insert: true
---
# Oppressive Wealth

> [!Thought-en]
> The Bible says some nasty things about rich people who oppress the masses.

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-May-2012)
CREATE (t:THOUGHT {
    name: "thought.OPPRESSIVE WEALTH",
    alias: "Thought: Oppressive Wealth",
    parent: "topic.MORALITY",
    tags: ['wealth', 'oppression', 'justice', 'bible', 'accuracy', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OPPRESSIVE WEALTH",
    en_title: "Oppressive Wealth",
    en_content: "The Bible says some nasty things about rich people who oppress the masses.",
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
WHERE t.name = "thought.OPPRESSIVE WEALTH" AND c.name = "content.OPPRESSIVE WEALTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OPPRESSIVE WEALTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.OPPRESSIVE WEALTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >OPPRESSIVE WEALTH" }]->(child);
```
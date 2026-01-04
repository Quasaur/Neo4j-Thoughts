---
name: "thought.PRAYER MAKES HUMAN"
alias: "Thought: Prayer Makes Human"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- prayer
- humanity
- animal
- spirituality
- essence
level: 2
neo4j: true
insert: true
---
# Prayer Makes Human

> [!Thought-en]
> Prayer, above all else, is what makes me Human; without it, I'm just an animal.

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013i)
CREATE (t:THOUGHT {
    name: "thought.PRAYER MAKES HUMAN",
    alias: "Thought: Prayer Makes Human",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'humanity', 'animal', 'spirituality', 'essence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER MAKES HUMAN",
    en_title: "Prayer Makes Human",
    en_content: "Prayer, above all else, is what makes me Human; without it, I'm just an animal.",
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
WHERE t.name = "thought.PRAYER MAKES HUMAN" AND c.name = "content.PRAYER MAKES HUMAN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER MAKES HUMAN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER MAKES HUMAN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER MAKES HUMAN" }]->(child);
```
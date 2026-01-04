---
name: "thought.GREED ECONOMIC WOES"
alias: "Thought: Greed Economic Woes"
type: THOUGHT
en_content: "The true source of our economic woes is GREED; therefore no recovery will ever be permanent until Christ returns."
parent: "topic.MORALITY"
tags:
- greed
- economy
- morality
- recovery
- society
level: 3
neo4j: true
insert: true
---
# Greed Economic Woes

> [!Thought-en]
> The true source of our economic woes is GREED; therefore no recovery will ever be permanent until Christ returns.

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012d)
CREATE (t:THOUGHT {
    name: "thought.GREED ECONOMIC WOES",
    alias: "Thought: Greed Economic Woes",
    parent: "topic.MORALITY",
    tags: ['greed', 'economy', 'morality', 'recovery', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GREED ECONOMIC WOES",
    en_title: "Greed Economic Woes",
    en_content: "The true source of our economic woes is GREED; therefore no recovery will ever be permanent until Christ returns.",
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
WHERE t.name = "thought.GREED ECONOMIC WOES" AND c.name = "content.GREED ECONOMIC WOES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GREED ECONOMIC WOES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.GREED ECONOMIC WOES"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >GREED ECONOMIC WOES" }]->(child);
```
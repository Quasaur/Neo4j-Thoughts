---
name: "thought.LAWS AND THE RICH"
alias: "Thought: Laws And The Rich"
type: THOUGHT
en_content: "As long as the laws favor the rich, the poor will always exist."
parent: "topic.MORALITY"
tags:
- poverty
- law
- wealth
- morality
- society
level: 3
neo4j: true
insert: true
---
# Laws And The Rich

> [!Thought-en]
> As long as the laws favor the rich, the poor will always exist.

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012e)
CREATE (t:THOUGHT {
    name: "thought.LAWS AND THE RICH",
    alias: "Thought: Laws And The Rich",
    parent: "topic.MORALITY",
    tags: ['poverty', 'law', 'wealth', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LAWS AND THE RICH",
    en_title: "Laws And The Rich",
    en_content: "As long as the laws favor the rich, the poor will always exist.",
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
WHERE t.name = "thought.LAWS AND THE RICH" AND c.name = "content.LAWS AND THE RICH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LAWS AND THE RICH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.LAWS AND THE RICH"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >LAWS AND THE RICH" }]->(child);
```
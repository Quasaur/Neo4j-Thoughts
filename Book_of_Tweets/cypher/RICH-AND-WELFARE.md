---
name: "thought.RICH AND WELFARE"
alias: "Thought: Rich And Welfare"
type: THOUGHT
en_content: "The rich don't want to pay for welfare ...nor do they wish to hire welfare recipients."
parent: "topic.MORALITY"
tags:
- wealth
- morality
- society
- poverty
- character
level: 3
neo4j: true
insert: true
---
# Rich And Welfare

> [!Thought-en]
> The rich don't want to pay for welfare ...nor do they wish to hire welfare recipients.

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2011d)
CREATE (t:THOUGHT {
    name: "thought.RICH AND WELFARE",
    alias: "Thought: Rich And Welfare",
    parent: "topic.MORALITY",
    tags: ['wealth', 'morality', 'society', 'poverty', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RICH AND WELFARE",
    en_title: "Rich And Welfare",
    en_content: "The rich don't want to pay for welfare ...nor do they wish to hire welfare recipients.",
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
WHERE t.name = "thought.RICH AND WELFARE" AND c.name = "content.RICH AND WELFARE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RICH AND WELFARE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.RICH AND WELFARE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >RICH AND WELFARE" }]->(child);
```
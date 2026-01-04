---
name: "thought.CHURCH IS BIG BUSINESS"
alias: "Thought: Church Is Big Business"
type: THOUGHT
en_content: "In America church is big business...that's a problem."
parent: "topic.RELIGION"
tags:
- church
- business
- money
- religion
- america
level: 3
neo4j: true
insert: true
---
# Church Is Big Business

> [!Thought-en]
> In America church is big business...that's a problem.

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.CHURCH IS BIG BUSINESS",
    alias: "Thought: Church Is Big Business",
    parent: "topic.RELIGION",
    tags: ['church', 'business', 'money', 'religion', 'america'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHURCH IS BIG BUSINESS",
    en_title: "Church Is Big Business",
    en_content: "In America church is big business...that's a problem.",
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
WHERE t.name = "thought.CHURCH IS BIG BUSINESS" AND c.name = "content.CHURCH IS BIG BUSINESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHURCH IS BIG BUSINESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.CHURCH IS BIG BUSINESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHURCH IS BIG BUSINESS" }]->(child);
```
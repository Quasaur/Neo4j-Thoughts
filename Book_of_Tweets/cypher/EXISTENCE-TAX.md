---
name: "thought.EXISTENCE TAX"
alias: "Thought: Existence Tax"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- life
- morality
- society
- tax
- creation
level: 3
neo4j: true
insert: true
---
# Existence Tax

> [!Thought-en]
> Cost of Living: Men can't CREATE Life...so they're gonna charge it an existence tax...are you kidding me?!?

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.EXISTENCE TAX",
    alias: "Thought: Existence Tax",
    parent: "topic.MORALITY",
    tags: ['life', 'morality', 'society', 'tax', 'creation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.EXISTENCE TAX",
    en_title: "Existence Tax",
    en_content: "Cost of Living: Men can't CREATE Life...so they're gonna charge it an existence tax...are you kidding me?!?",
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
WHERE t.name = "thought.EXISTENCE TAX" AND c.name = "content.EXISTENCE TAX"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EXISTENCE TAX" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.EXISTENCE TAX"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >EXISTENCE TAX" }]->(child);
```
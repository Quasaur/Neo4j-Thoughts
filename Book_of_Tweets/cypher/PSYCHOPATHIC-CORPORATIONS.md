---
name: "thought.PSYCHOPATHIC CORPORATIONS"
alias: "Thought: Psychopathic Corporations"
type: THOUGHT
en_content: "The corporation as a legal \"person\" is demonstrably psychopathic."
parent: "topic.MORALITY"
tags:
- morality
- corporations
- society
- ethics
- justice
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.PSYCHOPATHIC CORPORATIONS",
    alias: "Thought: Psychopathic Corporations",
    parent: "topic.MORALITY",
    tags: ['morality', 'corporations', 'society', 'ethics', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PSYCHOPATHIC CORPORATIONS",
    en_title: "Psychopathic Corporations",
    en_content: "The corporation as a legal \"person\" is demonstrably psychopathic.",
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
WHERE t.name = "thought.PSYCHOPATHIC CORPORATIONS" AND c.name = "content.PSYCHOPATHIC CORPORATIONS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PSYCHOPATHIC CORPORATIONS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.PSYCHOPATHIC CORPORATIONS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >PSYCHOPATHIC CORPORATIONS" }]->(child);
```

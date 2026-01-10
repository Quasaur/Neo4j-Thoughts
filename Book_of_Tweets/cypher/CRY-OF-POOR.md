---
name: "thought.CRY OF POOR"
alias: "Thought: Cry Of Poor"
type: THOUGHT
en_content: "Whoever closes his ear to the cry of the poor will himself call out and not be answered. Proverbs 21:13, ESV"
parent: "topic.MORALITY"
tags:
- poor
- justice
- bible
- morality
- consequences
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.CRY OF POOR",
    alias: "Thought: Cry Of Poor",
    parent: "topic.MORALITY",
    tags: ['poor', 'justice', 'bible', 'morality', 'consequences'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CRY OF POOR",
    en_title: "Cry Of Poor",
    en_content: "Whoever closes his ear to the cry of the poor will himself call out and not be answered. Proverbs 21:13, ESV",
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
WHERE t.name = "thought.CRY OF POOR" AND c.name = "content.CRY OF POOR"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CRY OF POOR" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CRY OF POOR"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CRY OF POOR" }]->(child);
```

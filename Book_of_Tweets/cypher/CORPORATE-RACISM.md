---
name: "thought.CORPORATE RACISM"
alias: "Thought: Corporate Racism"
type: THOUGHT
en_content: "Racism, Discrimination and Prejudice are alive and well in Corporate America."
parent: "topic.MORALITY"
tags:
- racism
- discrimination
- morality
- corporations
- justice
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.CORPORATE RACISM",
    alias: "Thought: Corporate Racism",
    parent: "topic.MORALITY",
    tags: ['racism', 'discrimination', 'morality', 'corporations', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CORPORATE RACISM",
    en_title: "Corporate Racism",
    en_content: "Racism, Discrimination and Prejudice are alive and well in Corporate America.",
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
WHERE t.name = "thought.CORPORATE RACISM" AND c.name = "content.CORPORATE RACISM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CORPORATE RACISM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CORPORATE RACISM"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CORPORATE RACISM" }]->(child);
```

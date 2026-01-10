---
name: "thought.OPPRESSING THE POOR"
alias: "Thought: Oppressing The Poor"
type: THOUGHT
en_content: "Whoever oppresses the poor to increase his own wealth, or gives to the rich, will only come to poverty. Proverbs 22:16, ESV"
parent: "topic.MORALITY"
tags:
- oppression
- wealth
- poverty
- morality
- character
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2012c)
CREATE (t:THOUGHT {
    name: "thought.OPPRESSING THE POOR",
    alias: "Thought: Oppressing The Poor",
    parent: "topic.MORALITY",
    tags: ['oppression', 'wealth', 'poverty', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OPPRESSING THE POOR",
    en_title: "Oppressing The Poor",
    en_content: "Whoever oppresses the poor to increase his own wealth, or gives to the rich, will only come to poverty. Proverbs 22:16, ESV",
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
WHERE t.name = "thought.OPPRESSING THE POOR" AND c.name = "content.OPPRESSING THE POOR"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OPPRESSING THE POOR" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.OPPRESSING THE POOR"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >OPPRESSING THE POOR" }]->(child);
```

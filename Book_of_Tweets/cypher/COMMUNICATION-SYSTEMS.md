---
name: "thought.COMMUNICATION SYSTEMS"
alias: "Thought: Communication Systems"
type: THOUGHT
en_content: "Every communication system must have a language, a medium, a device that reads, and an intelligence that writes/interprets...God is Great!"
parent: "topic.CREATION"
tags:
- design
- language
- intelligence
- communication
- creation
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2011d)
CREATE (t:THOUGHT {
    name: "thought.COMMUNICATION SYSTEMS",
    alias: "Thought: Communication Systems",
    parent: "topic.CREATION",
    tags: ['design', 'language', 'intelligence', 'communication', 'creation'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.COMMUNICATION SYSTEMS",
    en_title: "Communication Systems",
    en_content: "Every communication system must have a language, a medium, a device that reads, and an intelligence that writes/interprets...God is Great!",
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
WHERE t.name = "thought.COMMUNICATION SYSTEMS" AND c.name = "content.COMMUNICATION SYSTEMS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.COMMUNICATION SYSTEMS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.COMMUNICATION SYSTEMS"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >COMMUNICATION SYSTEMS" }]->(child);
```

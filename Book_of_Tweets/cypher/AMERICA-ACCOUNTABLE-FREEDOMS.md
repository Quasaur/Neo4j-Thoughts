---
name: "thought.AMERICA ACCOUNTABLE FREEDOMS"
alias: "Thought: America Accountable Freedoms"
type: THOUGHT
en_content: "America, God will hold you accountable for the way you spent your freedoms."
parent: "topic.MORALITY"
tags:
- america
- freedom
- accountability
- morality
- judgment
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Jul-2013)
CREATE (t:THOUGHT {
    name: "thought.AMERICA ACCOUNTABLE FREEDOMS",
    alias: "Thought: America Accountable Freedoms",
    parent: "topic.MORALITY",
    tags: ['america', 'freedom', 'accountability', 'morality', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AMERICA ACCOUNTABLE FREEDOMS",
    en_title: "America Accountable Freedoms",
    en_content: "America, God will hold you accountable for the way you spent your freedoms.",
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
WHERE t.name = "thought.AMERICA ACCOUNTABLE FREEDOMS" AND c.name = "content.AMERICA ACCOUNTABLE FREEDOMS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.AMERICA ACCOUNTABLE FREEDOMS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.AMERICA ACCOUNTABLE FREEDOMS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >AMERICA ACCOUNTABLE FREEDOMS" }]->(child);
```

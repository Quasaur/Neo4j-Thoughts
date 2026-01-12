---
name: "thought.VOICE OF THE DEVIL"
alias: "Thought: Voice Of The Devil"
type: THOUGHT
en_content: "Submitting to hate, bitterness and violence is giving a voice to The Devil; these have become his most cherished attributes."
parent: "topic.EVIL"
tags:
- hate
- bitterness
- violence
- devil
- spiritual_warfare
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.VOICE OF THE DEVIL",
    alias: "Thought: Voice Of The Devil",
    parent: "topic.EVIL",
    tags: ['hate', 'bitterness', 'violence', 'devil', 'spiritual_warfare'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.VOICE OF THE DEVIL",
    en_title: "Voice Of The Devil",
    en_content: "Submitting to hate, bitterness and violence is giving a voice to The Devil; these have become his most cherished attributes.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOICE OF THE DEVIL" AND c.name = "content.VOICE OF THE DEVIL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.VOICE OF THE DEVIL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.VOICE OF THE DEVIL"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >VOICE OF THE DEVIL" }]->(child);
```

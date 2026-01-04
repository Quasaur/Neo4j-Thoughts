---
name: "thought.DEVIL THE ACCUSER"
alias: "Thought: Devil The Accuser"
type: THOUGHT
parent: "topic.GRACE"
tags:
- accuser
- devil
- focus
- grace
level: 3
neo4j: true
insert: true
---
# Devil The Accuser

> [!Thought-en]
> The Devil is called the Accuser (Prosecutor) for a reason: he directs our focus to what we have done than what Christ has done for us.

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Mar-2014)
CREATE (t:THOUGHT {
    name: "thought.DEVIL THE ACCUSER",
    alias: "Thought: Devil The Accuser",
    parent: "topic.GRACE",
    tags: ['accuser', 'devil', 'focus', 'grace'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEVIL THE ACCUSER",
    en_title: "Devil The Accuser",
    en_content: "The Devil is called the Accuser (Prosecutor) for a reason: he directs our focus to what we have done than what Christ has done for us.",
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
WHERE t.name = "thought.DEVIL THE ACCUSER" AND c.name = "content.DEVIL THE ACCUSER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEVIL THE ACCUSER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.DEVIL THE ACCUSER"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >DEVIL THE ACCUSER" }]->(child);
```
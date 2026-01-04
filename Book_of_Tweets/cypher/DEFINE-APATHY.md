---
name: "thought.DEFINE APATHY"
alias: "Thought: Define Apathy"
type: THOUGHT
parent: "topic.ATTITUDE"
tags:
- love
- hate
- apathy
- attitude
- philosophy
level: 2
neo4j: true
insert: true
---
# Define Apathy

> [!Thought-en]
> Love & hate are not opposites...they are 2 halves of the same coin; the opposite of love / hate is Apathy.

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Mar-2011)
CREATE (t:THOUGHT {
    name: "thought.DEFINE APATHY",
    alias: "Thought: Define Apathy",
    parent: "topic.ATTITUDE",
    tags: ['love', 'hate', 'apathy', 'attitude', 'philosophy'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEFINE APATHY",
    en_title: "Define Apathy",
    en_content: "Love & hate are not opposites...they are 2 halves of the same coin; the opposite of love / hate is Apathy.",
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
WHERE t.name = "thought.DEFINE APATHY" AND c.name = "content.DEFINE APATHY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE APATHY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.DEFINE APATHY"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >DEFINE APATHY" }]->(child);
```
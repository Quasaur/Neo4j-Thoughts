---
name: "thought.CHRISTS FINAL VIRTUE"
alias: "Thought: Christs Final Virtue"
type: THOUGHT
parent: "topic.GRACE"
tags:
- jesus
- virtue
- humanity
- grace
- rejection
level: 3
neo4j: true
insert: true
---
# Christs Final Virtue

> [!Thought-en]
> Humanity's Last and only remaining Virtue is Jesus Christ; rejecting Him is turning our backs on the only Good left to us.

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.CHRISTS FINAL VIRTUE",
    alias: "Thought: Christs Final Virtue",
    parent: "topic.GRACE",
    tags: ['jesus', 'virtue', 'humanity', 'grace', 'rejection'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHRISTS FINAL VIRTUE",
    en_title: "Christs Final Virtue",
    en_content: "Humanity's Last and only remaining Virtue is Jesus Christ; rejecting Him is turning our backs on the only Good left to us.",
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
WHERE t.name = "thought.CHRISTS FINAL VIRTUE" AND c.name = "content.CHRISTS FINAL VIRTUE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRISTS FINAL VIRTUE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.CHRISTS FINAL VIRTUE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >CHRISTS FINAL VIRTUE" }]->(child);
```
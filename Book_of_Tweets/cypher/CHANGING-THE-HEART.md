---
name: "thought.CHANGING THE HEART"
alias: "Thought: Changing The Heart"
type: THOUGHT
en_content: "Proverbs 21:1; Matthew 19:25, 26. God has--and uses--the ability to change the heart's intent...otherwise no one would be saved."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- salvation
- heart
- transformation
- providence
level: 2
neo4j: true
insert: true
---
# Changing The Heart

> [!Thought-en]
> Proverbs 21:1; Matthew 19:25, 26. God has--and uses--the ability to change the heart's intent...otherwise no one would be saved.

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-May-2011a)
CREATE (t:THOUGHT {
    name: "thought.CHANGING THE HEART",
    alias: "Thought: Changing The Heart",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'salvation', 'heart', 'transformation', 'providence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.CHANGING THE HEART",
    en_title: "Changing The Heart",
    en_content: "Proverbs 21:1; Matthew 19:25, 26. God has--and uses--the ability to change the heart's intent...otherwise no one would be saved.",
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
WHERE t.name = "thought.CHANGING THE HEART" AND c.name = "content.CHANGING THE HEART"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHANGING THE HEART" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.CHANGING THE HEART"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >CHANGING THE HEART" }]->(child);
```
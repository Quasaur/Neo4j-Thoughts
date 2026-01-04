---
name: "thought.BORN FOR SERMON"
alias: "Thought: Born For Sermon"
type: THOUGHT
en_content: "Christmas sermon at the Pittsburgh prison was well-received...this is what I was born to do!"
parent: "topic.SPIRITUALITY"
tags:
- calling
- ministry
- prison
- sermon
- purpose
level: 2
neo4j: true
insert: true
---
# Born For Sermon

> [!Thought-en]
> Christmas sermon at the Pittsburgh prison was well-received...this is what I was born to do!

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Dec-2010)
CREATE (t:THOUGHT {
    name: "thought.BORN FOR SERMON",
    alias: "Thought: Born For Sermon",
    parent: "topic.SPIRITUALITY",
    tags: ['calling', 'ministry', 'prison', 'sermon', 'purpose'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BORN FOR SERMON",
    en_title: "Born For Sermon",
    en_content: "Christmas sermon at the Pittsburgh prison was well-received...this is what I was born to do!",
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
WHERE t.name = "thought.BORN FOR SERMON" AND c.name = "content.BORN FOR SERMON"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BORN FOR SERMON" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.BORN FOR SERMON"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >BORN FOR SERMON" }]->(child);
```
---
name: "thought.TWITTER TO HEAVEN"
alias: "Thought: Twitter To Heaven"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- heaven
- desire
- compassion
- followers
- eternity
level: 2
neo4j: true
insert: true
---
# Twitter To Heaven

> [!Thought-en]
> If I could, I'd take my Twitter followers to Heaven with me.

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.TWITTER TO HEAVEN",
    alias: "Thought: Twitter To Heaven",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'desire', 'compassion', 'followers', 'eternity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TWITTER TO HEAVEN",
    en_title: "Twitter To Heaven",
    en_content: "If I could, I'd take my Twitter followers to Heaven with me.",
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
WHERE t.name = "thought.TWITTER TO HEAVEN" AND c.name = "content.TWITTER TO HEAVEN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TWITTER TO HEAVEN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.TWITTER TO HEAVEN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >TWITTER TO HEAVEN" }]->(child);
```
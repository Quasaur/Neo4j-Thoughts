---
name: "thought.UNPATRIOTIC CORPORATIONS"
alias: "Thought: Unpatriotic Corporations"
type: THOUGHT
en_content: "The corporation as a legal \"person\" is unpatriotic."
parent: "topic.MORALITY"
tags:
- morality
- corporations
- society
- patriotism
- justice
level: 3
neo4j: true
insert: true
---
# Unpatriotic Corporations

> [!Thought-en]
> The corporation as a legal "person" is unpatriotic.

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011c)
CREATE (t:THOUGHT {
    name: "thought.UNPATRIOTIC CORPORATIONS",
    alias: "Thought: Unpatriotic Corporations",
    parent: "topic.MORALITY",
    tags: ['morality', 'corporations', 'society', 'patriotism', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNPATRIOTIC CORPORATIONS",
    en_title: "Unpatriotic Corporations",
    en_content: "The corporation as a legal \"person\" is unpatriotic.",
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
WHERE t.name = "thought.UNPATRIOTIC CORPORATIONS" AND c.name = "content.UNPATRIOTIC CORPORATIONS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNPATRIOTIC CORPORATIONS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.UNPATRIOTIC CORPORATIONS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >UNPATRIOTIC CORPORATIONS" }]->(child);
```
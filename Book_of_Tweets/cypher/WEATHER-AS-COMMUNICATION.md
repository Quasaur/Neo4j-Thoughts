---
name: "thought.WEATHER AS COMMUNICATION"
alias: "Thought: Weather As Communication"
type: THOUGHT
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- weather
- judgment
- nature
- communication
level: 2
neo4j: true
insert: true
---
# Weather As Communication

> [!Thought-en]
> 2 Chronicles 7:12-14; Leviticus 18:25: Yes, God DOES communicate and punish through weather and nature.

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011d)
CREATE (t:THOUGHT {
    name: "thought.WEATHER AS COMMUNICATION",
    alias: "Thought: Weather As Communication",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'weather', 'judgment', 'nature', 'communication'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WEATHER AS COMMUNICATION",
    en_title: "Weather As Communication",
    en_content: "2 Chronicles 7:12-14; Leviticus 18:25: Yes, God DOES communicate and punish through weather and nature.",
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
WHERE t.name = "thought.WEATHER AS COMMUNICATION" AND c.name = "content.WEATHER AS COMMUNICATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WEATHER AS COMMUNICATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.WEATHER AS COMMUNICATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >WEATHER AS COMMUNICATION" }]->(child);
```
---
name: "thought.JUDGMENT OF NATIONS"
alias: "Thought: Judgment Of Nations"
type: THOUGHT
en_content: "God will not only judge individuals, but nations (ethnic and political). May God grant repentance to the USA."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- judgment
- nations
- politics
- repentance
- sovereignty
level: 2
neo4j: true
insert: true
---
# Judgment Of Nations

> [!Thought-en]
> God will not only judge individuals, but nations (ethnic and political). May God grant repentance to the USA.

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-May-2011b)
CREATE (t:THOUGHT {
    name: "thought.JUDGMENT OF NATIONS",
    alias: "Thought: Judgment Of Nations",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['judgment', 'nations', 'politics', 'repentance', 'sovereignty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.JUDGMENT OF NATIONS",
    en_title: "Judgment Of Nations",
    en_content: "God will not only judge individuals, but nations (ethnic and political). May God grant repentance to the USA.",
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
WHERE t.name = "thought.JUDGMENT OF NATIONS" AND c.name = "content.JUDGMENT OF NATIONS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.JUDGMENT OF NATIONS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.JUDGMENT OF NATIONS"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >JUDGMENT OF NATIONS" }]->(child);
```
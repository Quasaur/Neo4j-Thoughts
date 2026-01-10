---
name: "thought.PREFERENCE VS NECESSITY"
alias: "Thought: Preference Vs Necessity"
type: THOUGHT
en_content: "Preference must give way to Necessity."
parent: "topic.WISDOM"
tags:
- wisdom
- choice
- necessity
- priority
- truth
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jul-2011b)
CREATE (t:THOUGHT {
    name: "thought.PREFERENCE VS NECESSITY",
    alias: "Thought: Preference Vs Necessity",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'choice', 'necessity', 'priority', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PREFERENCE VS NECESSITY",
    en_title: "Preference Vs Necessity",
    en_content: "Preference must give way to Necessity.",
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
WHERE t.name = "thought.PREFERENCE VS NECESSITY" AND c.name = "content.PREFERENCE VS NECESSITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PREFERENCE VS NECESSITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.PREFERENCE VS NECESSITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >PREFERENCE VS NECESSITY" }]->(child);
```

---
name: "thought.EDUCATION AS SELLING OUT"
alias: "Thought: Education As Selling Out"
type: THOUGHT
en_content: "At what point in history did African American men decide that being educated was selling out??"
parent: "topic.TRUTH"
tags:
- education
- truth
- selling_out
- race
- history
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012d)
CREATE (t:THOUGHT {
    name: "thought.EDUCATION AS SELLING OUT",
    alias: "Thought: Education As Selling Out",
    parent: "topic.TRUTH",
    tags: ['education', 'truth', 'selling_out', 'race', 'history'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EDUCATION AS SELLING OUT",
    en_title: "Education As Selling Out",
    en_content: "At what point in history did African American men decide that being educated was selling out??",
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
WHERE t.name = "thought.EDUCATION AS SELLING OUT" AND c.name = "content.EDUCATION AS SELLING OUT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EDUCATION AS SELLING OUT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.EDUCATION AS SELLING OUT"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >EDUCATION AS SELLING OUT" }]->(child);
```

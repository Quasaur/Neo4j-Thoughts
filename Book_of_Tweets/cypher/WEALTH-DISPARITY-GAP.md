---
name: "thought.WEALTH DISPARITY GAP"
alias: "Thought: Wealth Disparity Gap"
type: THOUGHT
en_content: "Median White household wealth: $US113,000. Median Black household wealth: $US5,700. Oh yeah...life's fair!"
parent: "topic.MORALITY"
tags:
- wealth
- race
- inequality
- society
- justice
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.WEALTH DISPARITY GAP",
    alias: "Thought: Wealth Disparity Gap",
    parent: "topic.MORALITY",
    tags: ['wealth', 'race', 'inequality', 'society', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WEALTH DISPARITY GAP",
    en_title: "Wealth Disparity Gap",
    en_content: "Median White household wealth: $US113,000. Median Black household wealth: $US5,700. Oh yeah...life's fair!",
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
WHERE t.name = "thought.WEALTH DISPARITY GAP" AND c.name = "content.WEALTH DISPARITY GAP"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WEALTH DISPARITY GAP" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.WEALTH DISPARITY GAP"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >WEALTH DISPARITY GAP" }]->(child);
```

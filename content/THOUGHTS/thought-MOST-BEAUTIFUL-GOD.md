---
type: THOUGHT
name: "thought.MOST BEAUTIFUL GOD"
alias: "Thought: Most Beautiful God"
parent: "topic.BEAUTY"
en_content: "There is no being God has created that is more handsome, beautiful or gorgeous than Himself."
tags: ["beauty", "aesthetics", "holiness", "character", "divinity"]
ptopic: "[[topic-BEAUTY]]"
level: 5
neo4j: false
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.MOST BEAUTIFUL GOD",
    alias: "Thought: Most Beautiful God",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'aesthetics', 'holiness', 'character', 'divinity'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.MOST BEAUTIFUL GOD",
    ctype: "THOUGHT",
    en_title: "Most Beautiful God",
    en_content: "There is no being God has created that is more handsome, beautiful or gorgeous than Himself.",
    es_title: "Dios Hermosísimo",
    es_content: "No hay ser que Dios haya creado que sea más hermoso, bello o magnífico que Él mismo.",
    fr_title: "Dieu le Plus Beau",
    fr_content: "Il n'y a aucun être que Dieu ait créé qui soit plus beau, magnifique ou splendide que Lui-même.",
    hi_title: "सबसे सुंदर परमेश्वर",
    hi_content: "परमेश्वर द्वारा रचा गया कोई भी प्राणी स्वयं परमेश्वर से अधिक सुंदर, मनोहर या भव्य नहीं है।",
    zh_title: "Zui Mei Li De Shen",
    zh_content: "Mei you ren he Shen suo chuang zao de sheng ming bi Ta zi ji geng ying jun, mei li huo hua li."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MOST BEAUTIFUL GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.BEAUTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.BEAUTY->MOST BEAUTIFUL GOD"
RETURN t, parent;
```

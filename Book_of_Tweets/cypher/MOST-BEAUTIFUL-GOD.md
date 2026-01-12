---
name: "thought.MOST BEAUTIFUL GOD"
alias: "Thought: Most Beautiful God"
type: THOUGHT
en_content: "There is no being God has created that is more handsome, beautiful or gorgeous than Himself."
parent: "topic.BEAUTY"
tags:
- beauty
- aesthetics
- holiness
- character
- divinity
level: 5
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-May-2012)
CREATE (t:THOUGHT {
    name: "thought.MOST BEAUTIFUL GOD",
    alias: "Thought: Most Beautiful God",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'aesthetics', 'holiness', 'character', 'divinity'],
    notes: "",
    level: 5
});

CREATE (c:CONTENT {
    name: "content.MOST BEAUTIFUL GOD",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MOST BEAUTIFUL GOD" AND c.name = "content.MOST BEAUTIFUL GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MOST BEAUTIFUL GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.MOST BEAUTIFUL GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "BEAUTY >MOST BEAUTIFUL GOD" }]->(child);
```

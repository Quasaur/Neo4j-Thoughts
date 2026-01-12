---
name: "thought.NOTHING NEW TRUTH"
alias: "Thought: Nothing New Truth"
type: THOUGHT
en_content: "There is nothing new about Truth."
parent: "topic.TRUTH"
tags:
- truth
- antiquity
- consistency
- philosophy
- reality
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.NOTHING NEW TRUTH",
    alias: "Thought: Nothing New Truth",
    parent: "topic.TRUTH",
    tags: ['truth', 'antiquity', 'consistency', 'philosophy', 'reality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NOTHING NEW TRUTH",
    en_title: "Nothing New Truth",
    en_content: "There is nothing new about Truth.",
    es_title: "Nada Nuevo en la Verdad",
    es_content: "No hay nada nuevo acerca de la Verdad.",
    fr_title: "Rien de Nouveau dans la Vérité",
    fr_content: "Il n'y a rien de nouveau concernant la Vérité.",
    hi_title: "सत्य में कुछ भी नया नहीं",
    hi_content: "सत्य के बारे में कुछ भी नया नहीं है।",
    zh_title: "Zhenli Mei You Xin Shi",
    zh_content: "Zhenli mei you shenme xin de dongxi."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOTHING NEW TRUTH" AND c.name = "content.NOTHING NEW TRUTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING NEW TRUTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.NOTHING NEW TRUTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >NOTHING NEW TRUTH" }]->(child);
```

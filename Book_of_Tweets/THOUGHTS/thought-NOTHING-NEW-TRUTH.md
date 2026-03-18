---
type: THOUGHT
name: "thought.NOTHING NEW TRUTH"
alias: "Thought: Nothing New Truth"
parent: "topic.TRUTH"
en_content: "There is nothing new about Truth."
tags: ["truth", "antiquity", "consistency", "philosophy", "reality"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Dec-2012)
CREATE (t:THOUGHT {    name: "thought.NOTHING NEW TRUTH",
    alias: "Thought: Nothing New Truth",
    parent: "topic.TRUTH",
    tags: ['truth', 'antiquity', 'consistency', 'philosophy', 'reality'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.NOTHING NEW TRUTH",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NOTHING NEW TRUTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.TRUTH->NOTHING NEW TRUTH"
RETURN t, parent;
```

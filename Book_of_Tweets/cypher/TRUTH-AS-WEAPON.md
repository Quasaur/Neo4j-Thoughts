---
name: "thought.TRUTH AS WEAPON"
alias: "Thought: Truth As Weapon"
type: THOUGHT
en_content: "Truth is a weapon far more dangerous than the hydrogen bomb."
parent: "topic.TRUTH"
tags:
- truth
- power
- weapon
- danger
- reality
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.TRUTH AS WEAPON",
    alias: "Thought: Truth As Weapon",
    parent: "topic.TRUTH",
    tags: ['truth', 'power', 'weapon', 'danger', 'reality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TRUTH AS WEAPON",
    en_title: "Truth As Weapon",
    en_content: "Truth is a weapon far more dangerous than the hydrogen bomb.",
    es_title: "La Verdad Como Arma",
    es_content: "La verdad es un arma mucho más peligrosa que la bomba de hidrógeno.",
    fr_title: "La Vérité Comme Arme",
    fr_content: "La vérité est une arme bien plus dangereuse que la bombe à hydrogène.",
    hi_title: "हथियार के रूप में सत्य",
    hi_content: "सत्य हाइड्रोजन बम से कहीं अधिक खतरनाक हथियार है।",
    zh_title: "Zhen Li Ru Wu Qi",
    zh_content: "Zhen li shi bi qing dan geng wei xian xian de wu qi."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRUTH AS WEAPON" AND c.name = "content.TRUTH AS WEAPON"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRUTH AS WEAPON" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.TRUTH AS WEAPON"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >TRUTH AS WEAPON" }]->(child);
```

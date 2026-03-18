---
type: THOUGHT
name: "thought.TRUTH AS WEAPON"
alias: "Thought: Truth As Weapon"
parent: "topic.TRUTH"
en_content: "Truth is a weapon far more dangerous than the hydrogen bomb."
tags: ["truth", "power", "weapon", "danger", "reality"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Sep-2011b)
CREATE (t:THOUGHT {    name: "thought.TRUTH AS WEAPON",
    alias: "Thought: Truth As Weapon",
    parent: "topic.TRUTH",
    tags: ['truth', 'power', 'weapon', 'danger', 'reality'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.TRUTH AS WEAPON",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TRUTH AS WEAPON"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.TRUTH->TRUTH AS WEAPON"
RETURN t, parent;
```

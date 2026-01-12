---
name: "thought.PAYCHECK VS SOUL"
alias: "Thought: Paycheck Vs Soul"
type: THOUGHT
en_content: "Stop living like your paycheck is worth more than the dignity of your SOUL! Matthew 16:26"
parent: "topic.MORALITY"
tags:
- soul
- dignity
- wealth
- morality
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012d_2)
CREATE (t:THOUGHT {
    name: "thought.PAYCHECK VS SOUL",
    alias: "Thought: Paycheck Vs Soul",
    parent: "topic.MORALITY",
    tags: ['soul', 'dignity', 'wealth', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PAYCHECK VS SOUL",
    en_title: "Paycheck Vs Soul",
    en_content: "Stop living like your paycheck is worth more than the dignity of your SOUL! Matthew 16:26",
    es_title: "Sueldo Vs Alma",
    es_content: "¡Deja de vivir como si tu sueldo valiera más que la dignidad de tu ALMA! Mateo 16:26",
    fr_title: "Salaire Vs Âme",
    fr_content: "Arrêtez de vivre comme si votre salaire valait plus que la dignité de votre ÂME ! Matthieu 16:26",
    hi_title: "वेतन बनाम आत्मा",
    hi_content: "अपने वेतन को अपनी आत्मा की गरिमा से अधिक मूल्यवान समझकर जीना बंद करो! मत्ती 16:26",
    zh_title: "Gongzi Dui Linghun",
    zh_content: "Bie zai xiang ni de gongzi bi ni LINGHUN de zunyan geng zhongyao yiyang shenghuo le! Mataifuyyin 16:26"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PAYCHECK VS SOUL" AND c.name = "content.PAYCHECK VS SOUL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PAYCHECK VS SOUL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.PAYCHECK VS SOUL"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >PAYCHECK VS SOUL" }]->(child);
```

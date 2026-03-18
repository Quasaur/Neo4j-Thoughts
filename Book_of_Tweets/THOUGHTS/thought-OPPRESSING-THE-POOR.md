---
type: THOUGHT
name: "thought.OPPRESSING THE POOR"
alias: "Thought: Oppressing The Poor"
parent: "topic.MORALITY"
en_content: "Whoever oppresses the poor to increase his own wealth, or gives to the rich, will only come to poverty. Proverbs 22:16, ESV"
tags: ["oppression", "wealth", "poverty", "morality", "character"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2012c)
CREATE (t:THOUGHT {    name: "thought.OPPRESSING THE POOR",
    alias: "Thought: Oppressing The Poor",
    parent: "topic.MORALITY",
    tags: ['oppression', 'wealth', 'poverty', 'morality', 'character'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.OPPRESSING THE POOR",
    ctype: "THOUGHT",
    en_title: "Oppressing The Poor",
    en_content: "Whoever oppresses the poor to increase his own wealth, or gives to the rich, will only come to poverty. Proverbs 22:16, ESV",
    es_title: "Oprimiendo a los Pobres",
    es_content: "El que oprime al pobre para aumentar sus riquezas, o da al rico, ciertamente vendrá a pobreza. Proverbios 22:16, RVR1960",
    fr_title: "Opprimer les Pauvres",
    fr_content: "Celui qui opprime le pauvre pour augmenter son gain, celui qui donne au riche, n'arrivera qu'à la disette. Proverbes 22:16, LSG",
    hi_title: "गरीबों पर अत्याचार",
    hi_content: "जो निर्धन पर अन्धेर करके अपनी सम्पत्ति बढ़ाता है, और जो धनवान को देता है, वे दोनों निश्चय कंगाल हो जाएंगे। नीतिवचन 22:16, HCV",
    zh_title: "Ya Po Pin Qiong",
    zh_content: "Yu ya pin qiong zhu li zi ji de, he song li gei fu zu de, dou bi que fa. Zhen yan 22:16, CUV"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.OPPRESSING THE POOR"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->OPPRESSING THE POOR"
RETURN t, parent;
```

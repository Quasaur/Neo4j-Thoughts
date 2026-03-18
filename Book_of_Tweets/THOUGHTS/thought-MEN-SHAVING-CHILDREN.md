---
type: THOUGHT
name: "thought.MEN SHAVING CHILDREN"
alias: "Thought: Men Shaving Children"
parent: "topic.HUMANITY"
en_content: "It may be that women like us men to shave that they may treat us like children."
tags: ["men", "women", "shaving", "children", "humor"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Sep-2013)
CREATE (t:THOUGHT {    name: "thought.MEN SHAVING CHILDREN",
    alias: "Thought: Men Shaving Children",
    parent: "topic.HUMANITY",
    tags: ['men', 'women', 'shaving', 'children', 'humor'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.MEN SHAVING CHILDREN",
    ctype: "THOUGHT",
    en_title: "Men Shaving Children",
    en_content: "It may be that women like us men to shave that they may treat us like children.",
    es_title: "Hombres Afeitándose Niños",
    es_content: "Puede ser que a las mujeres les guste que los hombres nos afeitemos para que nos traten como a niños.",
    fr_title: "Hommes rasant des enfants",
    fr_content: "Il se peut que les femmes aiment que nous, les hommes, nous rasions et qu'elles nous traitent comme des enfants.",
    hi_title: "बच्चों का मुंडन करते पुरुष",
    hi_content: "हो सकता है कि महिलाएं हम पुरुषों की तरह शेविंग करती हों ताकि वे हमारे साथ बच्चों जैसा व्यवहार करें।",
    zh_title: "nán shì tì xū   ér tóng",
    zh_content: "yě xǔ nǚ rén xǐ huān wǒ men nán rén guā hú zi ， suǒ yǐ tā men kě néng huì xiàng duì dài hái zi yī yàng duì dài wǒ men 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MEN SHAVING CHILDREN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->MEN SHAVING CHILDREN"
RETURN t, parent;
```

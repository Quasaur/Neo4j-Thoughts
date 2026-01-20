---
name: "thought.MEN SHAVING CHILDREN"
alias: "Thought: Men Shaving Children"
type: THOUGHT
en_content: "It may be that women like us men to shave that they may treat us like children."
parent: "topic.HUMANITY"
tags:
- men
- women
- shaving
- children
- humor
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Sep-2013)
CREATE (t:THOUGHT {
    name: "thought.MEN SHAVING CHILDREN",
    alias: "Thought: Men Shaving Children",
    parent: "topic.HUMANITY",
    tags: ['men', 'women', 'shaving', 'children', 'humor'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MEN SHAVING CHILDREN",
    en_title: "Men Shaving Children",
    en_content: "It may be that women like us men to shave that they may treat us like children.",
    es_title: "Hombres Afeitándose Niños",
    es_content: "Puede ser que a las mujeres les guste que los hombres nos afeitemos para que nos traten como a niños.",
    fr_title: "Hommes rasant des enfants",
    fr_content: "Il se peut que les femmes aiment que nous, les hommes, nous rasions et qu'elles nous traitent comme des enfants.",
    hi_title: "बच्चों का मुंडन करते पुरुष",
    hi_content: "हो सकता है कि महिलाएं हम पुरुषों की तरह शेविंग करती हों ताकि वे हमारे साथ बच्चों जैसा व्यवहार करें।",
    zh_title: "男士剃须 儿童",
    zh_content: "也许女人喜欢我们男人刮胡子，所以她们可能会像对待孩子一样对待我们。"
});

MATCH (t:THOUGHT {name: "thought.MEN SHAVING CHILDREN"})
MATCH (c:CONTENT {name: "content.MEN SHAVING CHILDREN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.MEN SHAVING CHILDREN" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.MEN SHAVING CHILDREN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >MEN SHAVING CHILDREN" }]->(child);
```

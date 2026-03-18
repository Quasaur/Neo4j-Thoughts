---
type: THOUGHT
name: "thought.SANHEDRIN CONCERNS"
alias: "Thought: Sanhedrin Concerns"
parent: "topic.MORALITY"
en_content: "The Sanhedrin was more concerned about their authority and money than about serving God or God's people."
tags: ["authority", "money", "morality", "church", "history"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Sep-2012)
CREATE (t:THOUGHT {    name: "thought.SANHEDRIN CONCERNS",
    alias: "Thought: Sanhedrin Concerns",
    parent: "topic.MORALITY",
    tags: ['authority', 'money', 'morality', 'church', 'history'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.SANHEDRIN CONCERNS",
    ctype: "THOUGHT",
    en_title: "Sanhedrin Concerns",
    en_content: "The Sanhedrin was more concerned about their authority and money than about serving God or God's people.",
    es_title: "Preocupaciones del Sanedrín",
    es_content: "El Sanedrín estaba más preocupado por su autoridad y dinero que por servir a Dios o al pueblo de Dios.",
    fr_title: "Préoccupations du Sanhédrin",
    fr_content: "Le Sanhédrin était plus préoccupé par son autorité et son argent que par servir Dieu ou le peuple de Dieu.",
    hi_title: "सैन्हेड्रिन की चिंताएं",
    hi_content: "सैन्हेड्रिन परमेश्वर या परमेश्वर के लोगों की सेवा करने की अपेक्षा अपने अधिकार और धन के बारे में अधिक चिंतित था।",
    zh_title: "Gonghui de Danxin",
    zh_content: "Gonghui geng guanxin tamen de quanwei he jinqian, er bu shi fuwu Shangdi huo Shangdi de renmin."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SANHEDRIN CONCERNS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->SANHEDRIN CONCERNS"
RETURN t, parent;
```

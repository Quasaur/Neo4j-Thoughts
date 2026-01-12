---
name: "thought.SANHEDRIN CONCERNS"
alias: "Thought: Sanhedrin Concerns"
type: THOUGHT
en_content: "The Sanhedrin was more concerned about their authority and money than about serving God or God's people."
parent: "topic.MORALITY"
tags:
- authority
- money
- morality
- church
- history
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.SANHEDRIN CONCERNS",
    alias: "Thought: Sanhedrin Concerns",
    parent: "topic.MORALITY",
    tags: ['authority', 'money', 'morality', 'church', 'history'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SANHEDRIN CONCERNS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SANHEDRIN CONCERNS" AND c.name = "content.SANHEDRIN CONCERNS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SANHEDRIN CONCERNS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SANHEDRIN CONCERNS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SANHEDRIN CONCERNS" }]->(child);
```

---
type: THOUGHT
name: "thought.UNSUBMISSIVE"
alias: "Thought: Unsubmissive"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["unsubmissive", "rebellious", "pointless", "meaningless", "god"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.UNSUBMISSIVE",
    alias: "Thought: Unsubmissive",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["unsubmissive", "rebellious", "pointless", "meaningless", "god"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.UNSUBMISSIVE",
    ctype: "THOUGHT",
    en_title: "Unsubmissive",
    en_content: "",
    es_title: "INSUMISO",
    es_content: "Es una lástima que tantas personas prefieran llevar una vida sin sentido que 
 someterse a la autoridad divina.",
    fr_title: "NON SOUMIS",
    fr_content: "C'est juste dommage que tant de gens préfèrent mener une vie inutile plutôt que 
 soumettre à l'autorité divine.",
    hi_title: "अलग",
    hi_content: "यह शर्म की बात है कि इतने सारे लोग इसके बजाय निरर्थक जीवन जीना पसंद करेंगे 
 ईश्वरीय प्राधिकार को समर्पित करें.",
    zh_title: "bù fú cóng",
    zh_content: "yí hàn de shì ， zhè me duō rén nìng yuàn guò zhe háo wú yì yì de shēng huó ， yě bù yuàn guò zhe wú yì yì de shēng huó 。 
  fú cóng shén shèng de quán wēi 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNSUBMISSIVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE-SOVEREIGNTY->UNSUBMISSIVE"
RETURN t, parent;
```

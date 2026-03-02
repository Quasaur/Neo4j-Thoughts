---
type: THOUGHT
name: "thought.UNSUBMISSIVE"
alias: "Thought: UNSUBMISSIVE"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["unsubmissive", "rebellious", "pointless", "meaningless", "god"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.UNSUBMISSIVE",
    alias: "Thought: UNSUBMISSIVE",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["unsubmissive", "rebellious", "pointless", "meaningless", "god"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.UNSUBMISSIVE",
    ctype: "THOUGHT",
    en_title: "UNSUBMISSIVE",
 es_title: "INSUMISO",
 fr_title: "NON SOUMIS",
 hi_title: "अलग",
 zh_title: "bù fú cóng",
    en_content: "",
 es_content: "Es una lástima que tantas personas prefieran llevar una vida sin sentido que 
 someterse a la autoridad divina.",
 fr_content: "C'est juste dommage que tant de gens préfèrent mener une vie inutile plutôt que 
 soumettre à l'autorité divine.",
 hi_content: "यह शर्म की बात है कि इतने सारे लोग इसके बजाय निरर्थक जीवन जीना पसंद करेंगे 
 ईश्वरीय प्राधिकार को समर्पित करें.",
 zh_content: "yí hàn de shì ， zhè me duō rén nìng yuàn guò zhe háo wú yì yì de shēng huó ， yě bù yuàn guò zhe wú yì yì de shēng huó 。 
  fú cóng shén shèng de quán wēi 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNSUBMISSIVE" AND c.name = "content.UNSUBMISSIVE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.UNSUBMISSIVE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.UNSUBMISSIVE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->UNSUBMISSIVE"}]->(child);
```
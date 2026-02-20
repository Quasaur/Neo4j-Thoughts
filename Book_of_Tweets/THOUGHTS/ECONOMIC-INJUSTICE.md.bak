---
name: "thought.ECONOMIC INJUSTICE"
alias: "Thought: Economic Injustice"
type: THOUGHT
en_content: "This economic downturn is especially difficult for African Americans; we're the last to get hired and the 1st to get fired."
parent: "topic.MORALITY"
tags:
- justice
- economy
- society
- race
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Nov-2010a)
CREATE (t:THOUGHT {
    name: "thought.ECONOMIC INJUSTICE",
    alias: "Thought: Economic Injustice",
    parent: "topic.MORALITY",
    tags: ['justice', 'economy', 'society', 'race', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ECONOMIC INJUSTICE",
    en_title: "Economic Injustice",
    en_content: "This economic downturn is especially difficult for African Americans; we're the last to get hired and the 1st to get fired.",
    es_title: "Injusticia Económica",
    es_content: "Esta recesión económica es especialmente difícil para los afroamericanos; somos los últimos en ser contratados y los primeros en ser despedidos.",
    fr_title: "Injustice Économique",
    fr_content: "Ce ralentissement économique est particulièrement difficile pour les Afro-Américains ; nous sommes les derniers à être embauchés et les premiers à être licenciés.",
    hi_title: "आर्थिक अन्याय",
    hi_content: "यह आर्थिक मंदी अफ्रीकी अमेरिकियों के लिए विशेष रूप से कठिन है; हम नौकरी पाने वालों में आखिरी और निकाले जाने वालों में पहले हैं।",
    zh_title: "Jīngjì bùgōngzhèng 经济不公正",
    zh_content: "Zhè cì jīngjì dīmi ào duì Fēizhōu Měiguó rén yóuqián kùnnán; wǒmen shì zuíhòu bèi gùyòng de, yě shì di yī gè bèi jiěgù de. 这次经济低迷对非洲美国人尤其困难；我们是最后被雇用的，也是第一个被解雇的。"
});

MATCH (t:THOUGHT {name: "thought.ECONOMIC INJUSTICE"})
MATCH (c:CONTENT {name: "content.ECONOMIC INJUSTICE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ECONOMIC INJUSTICE" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.ECONOMIC INJUSTICE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->ECONOMIC INJUSTICE" }]->(child);
```

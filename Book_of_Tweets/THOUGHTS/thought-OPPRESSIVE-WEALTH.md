---
type: THOUGHT
name: "thought.OPPRESSIVE WEALTH"
alias: "Thought: Oppressive Wealth"
parent: "topic.MORALITY"
en_content: "The Bible says some nasty things about rich people who oppress the masses."
tags: ["wealth", "oppression", "justice", "bible", "accuracy", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-May-2012)
CREATE (t:THOUGHT {    name: "thought.OPPRESSIVE WEALTH",
    alias: "Thought: Oppressive Wealth",
    parent: "topic.MORALITY",
    tags: ['wealth', 'oppression', 'justice', 'bible', 'accuracy', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.OPPRESSIVE WEALTH",
    ctype: "THOUGHT",
    en_title: "Oppressive Wealth",
    en_content: "The Bible says some nasty things about rich people who oppress the masses.",
    es_title: "Riqueza Opresiva",
    es_content: "La Biblia dice cosas duras acerca de los ricos que oprimen a las masas.",
    fr_title: "Richesse Oppressive",
    fr_content: "La Bible dit des choses sévères sur les riches qui oppriment les masses.",
    hi_title: "उत्पीड़नकारी धन",
    hi_content: "बाइबल उन अमीर लोगों के बारे में कड़ी बातें कहती है जो जनसाधारण पर अत्याचार करते हैं।",
    zh_title: "Ya Po Xing De Cai Fu",
    zh_content: "Sheng Jing Dui Ya Po Min Zhong De Fu Ren Shuo Le Xie Yan Li De Hua."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.OPPRESSIVE WEALTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->OPPRESSIVE WEALTH"
RETURN t, parent;
```

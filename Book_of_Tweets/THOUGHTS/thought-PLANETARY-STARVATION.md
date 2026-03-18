---
type: THOUGHT
name: "thought.PLANETARY STARVATION"
alias: "Thought: Planetary Starvation"
parent: "topic.MORALITY"
en_content: "There's enough resources on Planet Earth for EVERYONE...so why are people starving?!?"
tags: ["poverty", "hunger", "resources", "justice", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jun-2012b)
CREATE (t:THOUGHT {    name: "thought.PLANETARY STARVATION",
    alias: "Thought: Planetary Starvation",
    parent: "topic.MORALITY",
    tags: ['poverty', 'hunger', 'resources', 'justice', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.PLANETARY STARVATION",
    ctype: "THOUGHT",
    en_title: "Planetary Starvation",
    en_content: "There's enough resources on Planet Earth for EVERYONE...so why are people starving?!?",
    es_title: "Hambruna Planetaria",
    es_content: "Hay suficientes recursos en el Planeta Tierra para TODOS...¡¿entonces por qué la gente está muriendo de hambre?!?",
    fr_title: "Famine Planétaire",
    fr_content: "Il y a assez de ressources sur la Planète Terre pour TOUT LE MONDE...alors pourquoi les gens meurent-ils de faim ?!?",
    hi_title: "ग्रहीय भुखमरी",
    hi_content: "पृथ्वी ग्रह पर सभी के लिए पर्याप्त संसाधन हैं...तो फिर लोग भूखे क्यों मर रहे हैं?!?",
    zh_title: "Xing Qiu Ji E",
    zh_content: "Di Qiu Shang You Zu Gou De Zi Yuan Gong Suo You Ren Shi Yong...Na Me Wei Shen Me Hai You Ren Ai E Ne?!?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PLANETARY STARVATION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->PLANETARY STARVATION"
RETURN t, parent;
```

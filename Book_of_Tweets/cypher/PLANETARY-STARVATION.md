---
name: "thought.PLANETARY STARVATION"
alias: "Thought: Planetary Starvation"
type: THOUGHT
en_content: "There's enough resources on Planet Earth for EVERYONE...so why are people starving?!?"
parent: "topic.MORALITY"
tags:
- poverty
- hunger
- resources
- justice
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jun-2012b)
CREATE (t:THOUGHT {
    name: "thought.PLANETARY STARVATION",
    alias: "Thought: Planetary Starvation",
    parent: "topic.MORALITY",
    tags: ['poverty', 'hunger', 'resources', 'justice', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PLANETARY STARVATION",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PLANETARY STARVATION" AND c.name = "content.PLANETARY STARVATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PLANETARY STARVATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.PLANETARY STARVATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >PLANETARY STARVATION" }]->(child);
```

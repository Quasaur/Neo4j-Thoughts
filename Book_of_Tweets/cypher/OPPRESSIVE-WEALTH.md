---
name: "thought.OPPRESSIVE WEALTH"
alias: "Thought: Oppressive Wealth"
type: THOUGHT
en_content: "The Bible says some nasty things about rich people who oppress the masses."
parent: "topic.MORALITY"
tags:
- wealth
- oppression
- justice
- bible
- accuracy
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-May-2012)
CREATE (t:THOUGHT {
    name: "thought.OPPRESSIVE WEALTH",
    alias: "Thought: Oppressive Wealth",
    parent: "topic.MORALITY",
    tags: ['wealth', 'oppression', 'justice', 'bible', 'accuracy', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OPPRESSIVE WEALTH",
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

MATCH (t:THOUGHT {name: "thought.OPPRESSIVE WEALTH"})
MATCH (c:CONTENT {name: "content.OPPRESSIVE WEALTH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.OPPRESSIVE WEALTH" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.OPPRESSIVE WEALTH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >OPPRESSIVE WEALTH" }]->(child);
```

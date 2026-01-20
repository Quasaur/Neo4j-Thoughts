---
name: "thought.FORGIVING OTHERS PROBLEM"
alias: "Thought: Forgiving Others Problem"
type: THOUGHT
en_content: "If a person has received forgiveness from God for EVERY sin, why would they have a problem forgiving anyone else?"
parent: "topic.GRACE"
tags:
- forgiveness
- grace
- character
- love
- peace
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.FORGIVING OTHERS PROBLEM",
    alias: "Thought: Forgiving Others Problem",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'grace', 'character', 'love', 'peace'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FORGIVING OTHERS PROBLEM",
    en_title: "Forgiving Others Problem",
    en_content: "If a person has received forgiveness from God for EVERY sin, why would they have a problem forgiving anyone else?",
    es_title: "Problema de Perdonar a Otros",
    es_content: "Si una persona ha recibido el perdón de Dios por CADA pecado, ¿por qué tendría problemas para perdonar a cualquier otra persona?",
    fr_title: "Problème de Pardonner aux Autres",
    fr_content: "Si une personne a reçu le pardon de Dieu pour CHAQUE péché, pourquoi aurait-elle un problème à pardonner à quelqu'un d'autre?",
    hi_title: "दूसरों को क्षमा करने की समस्या",
    hi_content: "यदि किसी व्यक्ति को परमेश्वर से हर पाप के लिए क्षमा मिली है, तो वह किसी और को क्षमा करने में समस्या क्यों करेगा?",
    zh_title: "Kuangshu Taren Wenti",
    zh_content: "Ruguo yi ge ren yijing cong Shangdi dedao le dui mei yi ge zuie de kuangshu, weishenme ta hai hui zai kuangshu bieren shang you wenti ne?"
});

MATCH (t:THOUGHT {name: "thought.FORGIVING OTHERS PROBLEM"})
MATCH (c:CONTENT {name: "content.FORGIVING OTHERS PROBLEM"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FORGIVING OTHERS PROBLEM" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.FORGIVING OTHERS PROBLEM"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >FORGIVING OTHERS PROBLEM" }]->(child);
```

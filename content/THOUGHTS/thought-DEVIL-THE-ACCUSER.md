---
type: THOUGHT
name: "thought.DEVIL THE ACCUSER"
alias: "Thought: Devil The Accuser"
parent: "topic.GUILT"
en_content: "The Devil is called the Accuser (Prosecutor) for a reason: he directs our focus to what we have done rather than what Christ has done for us."
tags: ["accuser", "devil", "focus", "grace"]
ptopic: "[[topic-GUILT]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEVIL THE ACCUSER",
    alias: "Thought: Devil The Accuser",
    parent: "topic.GUILT",
    tags: ['accuser', 'devil', 'focus', 'grace'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.DEVIL THE ACCUSER",
    ctype: "THOUGHT",
    en_title: "Devil The Accuser",
    en_content: "The Devil is called the Accuser (Prosecutor) for a reason: he directs our focus to what we have done than what Christ has done for us.",
    es_title: "El Diablo El Acusador",
    es_content: "El Diablo es llamado el Acusador (Fiscal) por una razón: él dirige nuestro enfoque hacia lo que hemos hecho más que hacia lo que Cristo ha hecho por nosotros.",
    fr_title: "Le Diable L'Accusateur",
    fr_content: "Le Diable est appelé l'Accusateur (Procureur) pour une raison : il dirige notre attention sur ce que nous avons fait plutôt que sur ce que le Christ a fait pour nous.",
    hi_title: "शैतान अभियोगकर्ता",
    hi_content: "शैतान को अभियोगकर्ता (अभियोजक) कहा जाता है एक कारण से: वह हमारा ध्यान इस बात पर केंद्रित करता है कि हमने क्या किया है, इस बात पर नहीं कि मसीह ने हमारे लिए क्या किया है।",
    zh_title: "E Mo Kong Gao Zhe",
    zh_content: "E mo bei cheng wei kong gao zhe (jian cha guan) shi you yuan yin de: ta jiang wo men de zhu yi li zhuan xiang wo men suo zuo de shi, er bu shi Ji du wei wo men suo zuo de shi."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEVIL THE ACCUSER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->DEVIL THE ACCUSER"
RETURN t, parent;
```

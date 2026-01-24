---
name: "thought.DEVIL THE ACCUSER"
alias: "Thought: Devil The Accuser"
type: THOUGHT
en_content: "The Devil is called the Accuser (Prosecutor) for a reason: he directs our focus to what we have done than what Christ has done for us."
parent: "topic.GRACE"
tags:
- accuser
- devil
- focus
- grace
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Mar-2014)
CREATE (t:THOUGHT {
    name: "thought.DEVIL THE ACCUSER",
    alias: "Thought: Devil The Accuser",
    parent: "topic.GRACE",
    tags: ['accuser', 'devil', 'focus', 'grace'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEVIL THE ACCUSER",
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

MATCH (t:THOUGHT {name: "thought.DEVIL THE ACCUSER"})
MATCH (c:CONTENT {name: "content.DEVIL THE ACCUSER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEVIL THE ACCUSER" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.DEVIL THE ACCUSER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE->DEVIL THE ACCUSER" }]->(child);
```

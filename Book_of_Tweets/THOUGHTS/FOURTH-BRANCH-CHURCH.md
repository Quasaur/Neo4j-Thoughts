---
name: "thought.FOURTH BRANCH CHURCH"
alias: "Thought: Fourth Branch Church"
type: THOUGHT
en_content: "The true power of the Church is demonstrated by its tax-free status AND that no one's willing to ADMIT it's the 4th Branch of the U.S. Gov."
parent: "topic.RELIGION"
tags:
- church
- government
- politics
- religion
- society
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Apr-2012a)
CREATE (t:THOUGHT {
    name: "thought.FOURTH BRANCH CHURCH",
    alias: "Thought: Fourth Branch Church",
    parent: "topic.RELIGION",
    tags: ['church', 'government', 'politics', 'religion', 'society'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FOURTH BRANCH CHURCH",
    en_title: "Fourth Branch Church",
    en_content: "The true power of the Church is demonstrated by its tax-free status AND that no one's willing to ADMIT it's the 4th Branch of the U.S. Gov.",
    es_title: "Iglesia Cuarta Rama",
    es_content: "El verdadero poder de la Iglesia se demuestra por su estatus libre de impuestos Y que nadie está dispuesto a ADMITIR que es la 4ta Rama del Gobierno de EE.UU.",
    fr_title: "Église Quatrième Branche",
    fr_content: "Le vrai pouvoir de l'Église se démontre par son statut d'exemption fiscale ET que personne n'est disposé à ADMETTRE que c'est la 4ème Branche du Gouvernement américain.",
    hi_title: "चौथी शाखा चर्च",
    hi_content: "चर्च की वास्तविक शक्ति इसकी कर-मुक्त स्थिति से प्रदर्शित होती है और यह कि कोई भी यह स्वीकार करने को तैयार नहीं है कि यह अमेरिकी सरकार की चौथी शाखा है।",
    zh_title: "Di Si Bu Men Jiao Hui",
    zh_content: "Jiao Hui de zhen zheng li liang tong guo qi mian shui di wei lai zheng ming, ER QIE mei you ren yuan yi CHENG REN ta shi Mei Guo Zheng Fu de di si ge bu men."
});

MATCH (t:THOUGHT {name: "thought.FOURTH BRANCH CHURCH"})
MATCH (c:CONTENT {name: "content.FOURTH BRANCH CHURCH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FOURTH BRANCH CHURCH" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.FOURTH BRANCH CHURCH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >FOURTH BRANCH CHURCH" }]->(child);
```

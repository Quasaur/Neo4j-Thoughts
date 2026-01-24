---
name: "thought.PRIEST OF CHRIST"
alias: "Thought: Priest Of Christ"
type: THOUGHT
en_content: "As a priest of Christ, it's my job to speak God's Word (The Holy Bible) into the planetary atmosphere."
parent: "topic.SPIRITUALITY"
tags:
- priest
- christ
- atmosphere
- bible
- assignment
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Apr-2012b)
CREATE (t:THOUGHT {
    name: "thought.PRIEST OF CHRIST",
    alias: "Thought: Priest Of Christ",
    parent: "topic.SPIRITUALITY",
    tags: ['priest', 'christ', 'atmosphere', 'bible', 'assignment'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRIEST OF CHRIST",
    en_title: "Priest Of Christ",
    en_content: "As a priest of Christ, it's my job to speak God's Word (The Holy Bible) into the planetary atmosphere.",
    es_title: "Sacerdote de Cristo",
    es_content: "Como sacerdote de Cristo, mi trabajo es proclamar la Palabra de Dios (La Santa Biblia) en la atmósfera planetaria.",
    fr_title: "Prêtre du Christ",
    fr_content: "En tant que prêtre du Christ, mon travail est de proclamer la Parole de Dieu (La Sainte Bible) dans l'atmosphère planétaire.",
    hi_title: "मसीह के याजक",
    hi_content: "मसीह के एक याजक के रूप में, मेरा काम परमेश्वर के वचन (पवित्र बाइबिल) को पृथ्वी के वायुमंडल में घोषित करना है।",
    zh_title: "Jīdū de Jìsī",
    zh_content: "Zuòwéi Jīdū de jìsī, wǒ de gōngzuò shì jiāng Shàngdì de Huà (Shèngjīng) shuō dào xíngxīng dàqìcéng zhōng."
});

MATCH (t:THOUGHT {name: "thought.PRIEST OF CHRIST"})
MATCH (c:CONTENT {name: "content.PRIEST OF CHRIST"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRIEST OF CHRIST" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.PRIEST OF CHRIST"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->PRIEST OF CHRIST" }]->(child);
```

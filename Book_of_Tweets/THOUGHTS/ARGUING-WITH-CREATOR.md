---
name: "thought.ARGUING WITH CREATOR"
alias: "Thought: Arguing With Creator"
type: THOUGHT
en_content: "Humanity's constant pastime is to argue with its Creator."
parent: "topic.HUMANITY"
tags:
- humanity
- rebellion
- creation
- argument
- pride
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.ARGUING WITH CREATOR",
    alias: "Thought: Arguing With Creator",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'rebellion', 'creation', 'argument', 'pride'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ARGUING WITH CREATOR",
    en_title: "Arguing With Creator",
    en_content: "Humanity's constant pastime is to argue with its Creator.",
    es_title: "Discutiendo con el Creador",
    es_content: "El pasatiempo constante de la humanidad es discutir con su Creador.",
    fr_title: "Disputer avec le Créateur",
    fr_content: "Le passe-temps constant de l'humanité est de discuter avec son Créateur.",
    hi_title: "सृष्टिकर्ता से बहस करना",
    hi_content: "मानवता का निरंतर शगल अपने सृष्टिकर्ता से बहस करना है।",
    zh_title: "Yǔ Chuàngzàozhǔ zhēnglùn 与造物主争论",
    zh_content: "Rénlèi de chángjiǔ xiāoqiǎn jiùshì yǔ qí Chuàngzàozhǔ zhēnglùn. 人类的长久消遣就是与其造物主争论。"
});

MATCH (t:THOUGHT {name: "thought.ARGUING WITH CREATOR"})
MATCH (c:CONTENT {name: "content.ARGUING WITH CREATOR"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ARGUING WITH CREATOR" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.ARGUING WITH CREATOR"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->ARGUING WITH CREATOR" }]->(child);
```

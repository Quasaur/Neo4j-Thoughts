---
name: "thought.OBSOLETE HUMAN RACE"
alias: "Thought: Obsolete Human Race"
type: THOUGHT
en_content: "The human race is obsolete...God is creating a new race with Christ as The Adam; familyship is granted by Grace through Faith."
parent: "topic.HUMANITY"
tags:
- humanity
- christ
- grace
- faith
- creation
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.OBSOLETE HUMAN RACE",
    alias: "Thought: Obsolete Human Race",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'christ', 'grace', 'faith', 'creation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OBSOLETE HUMAN RACE",
    en_title: "Obsolete Human Race",
    en_content: "The human race is obsolete...God is creating a new race with Christ as The Adam; familyship is granted by Grace through Faith.",
    es_title: "Raza Humana Obsoleta",
    es_content: "La raza humana es obsoleta...Dios está creando una nueva raza con Cristo como El Adán; la filiación familiar es otorgada por Gracia mediante la Fe.",
    fr_title: "Race Humaine Obsolète",
    fr_content: "La race humaine est obsolète...Dieu crée une nouvelle race avec le Christ comme L'Adam; l'appartenance familiale est accordée par Grâce par la Foi.",
    hi_title: "अप्रचलित मानव जाति",
    hi_content: "मानव जाति अप्रचलित है...परमेश्वर मसीह को आदम के रूप में रखकर एक नई जाति का सृजन कर रहा है; पारिवारिक संबंध अनुग्रह द्वारा विश्वास के माध्यम से प्रदान किया जाता है।",
    zh_title: "Guòshí de Rénlèi",
    zh_content: "Rénlèi yǐjīng guòshí le...Shàngdì zhèngzài chuàngzào yī gè xīn zhǒngzú, yǐ Jīdū wéi nà Yàdāng; jiātíng guānxì tōngguò ēndiǎn jiè zhe xìnxīn ér cìyǔ."
});

MATCH (t:THOUGHT {name: "thought.OBSOLETE HUMAN RACE"})
MATCH (c:CONTENT {name: "content.OBSOLETE HUMAN RACE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.OBSOLETE HUMAN RACE" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.OBSOLETE HUMAN RACE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->OBSOLETE HUMAN RACE" }]->(child);
```

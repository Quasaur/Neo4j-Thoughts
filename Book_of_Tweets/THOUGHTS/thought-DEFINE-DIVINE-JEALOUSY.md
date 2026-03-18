---
type: THOUGHT
name: "thought.DEFINE DIVINE JEALOUSY"
alias: "Thought: Define Divine Jealousy"
parent: "topic.THE GODHEAD"
en_content: "Divine Jealousy: Ownership in Love with Responsibility and Accountability."
tags: ["jealousy", "ownership", "love", "responsibility", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Feb-2012b)
CREATE (t:THOUGHT {    name: "thought.DEFINE DIVINE JEALOUSY",
    alias: "Thought: Define Divine Jealousy",
    parent: "topic.THE GODHEAD",
    tags: ['jealousy', 'ownership', 'love', 'responsibility', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.DEFINE DIVINE JEALOUSY",
    ctype: "THOUGHT",
    en_title: "Define Divine Jealousy",
    en_content: "Divine Jealousy: Ownership in Love with Responsibility and Accountability.",
    es_title: "Definir Celos Divinos",
    es_content: "Celos Divinos: Propiedad en Amor con Responsabilidad y Rendición de Cuentas.",
    fr_title: "Définir la Jalousie Divine",
    fr_content: "Jalousie Divine : Propriété dans l'Amour avec Responsabilité et Responsabilité.",
    hi_title: "दैवी ईर्ष्या को परिभाषित करें",
    hi_content: "दैवी ईर्ष्या: जिम्मेदारी और जवाबदेही के साथ प्रेम में स्वामित्व।",
    zh_title: "Dìngyì shén shèng de jídù",
    zh_content: "Shén shèng de jídù: Zài ài zhōng de suǒyǒu quán yǔ zérèn hé zérèn."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE DIVINE JEALOUSY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->DEFINE DIVINE JEALOUSY"
RETURN t, parent;
```

---
name: "thought.DEFINE DIVINE JEALOUSY"
alias: "Thought: Define Divine Jealousy"
type: THOUGHT
en_content: "Divine Jealousy: Ownership in Love with Responsibility and Accountability."
parent: "topic.THE GODHEAD"
tags:
- jealousy
- ownership
- love
- responsibility
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.DEFINE DIVINE JEALOUSY",
    alias: "Thought: Define Divine Jealousy",
    parent: "topic.THE GODHEAD",
    tags: ['jealousy', 'ownership', 'love', 'responsibility', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.DEFINE DIVINE JEALOUSY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEFINE DIVINE JEALOUSY" AND c.name = "content.DEFINE DIVINE JEALOUSY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE DIVINE JEALOUSY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.DEFINE DIVINE JEALOUSY"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >DEFINE DIVINE JEALOUSY" }]->(child);
```

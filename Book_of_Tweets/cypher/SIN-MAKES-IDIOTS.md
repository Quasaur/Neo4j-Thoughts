---
name: "thought.SIN MAKES IDIOTS"
alias: "Thought: Sin Makes Idiots"
type: THOUGHT
en_content: "Sin makes idiots of us all; Christ came to take away the sins of the body (disease) as well as the sins of the soul!"
parent: "topic.GRACE"
tags:
- sin
- christ
- healing
- body
- soul
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013e)
CREATE (t:THOUGHT {
    name: "thought.SIN MAKES IDIOTS",
    alias: "Thought: Sin Makes Idiots",
    parent: "topic.GRACE",
    tags: ['sin', 'christ', 'healing', 'body', 'soul'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIN MAKES IDIOTS",
    en_title: "Sin Makes Idiots",
    en_content: "Sin makes idiots of us all; Christ came to take away the sins of the body (disease) as well as the sins of the soul!",
    es_title: "El Pecado Nos Hace Idiotas",
    es_content: "¡El pecado nos hace idiotas a todos; Cristo vino para quitar los pecados del cuerpo (enfermedad) así como los pecados del alma!",
    fr_title: "Le Péché Nous Rend Idiots",
    fr_content: "Le péché nous rend tous idiots ; le Christ est venu pour enlever les péchés du corps (maladie) ainsi que les péchés de l'âme !",
    hi_title: "पाप हमें मूर्ख बनाता है",
    hi_content: "पाप हम सभी को मूर्ख बनाता है; मसीह शरीर के पापों (रोग) के साथ-साथ आत्मा के पापों को भी दूर करने के लिए आया!",
    zh_title: "Zuì'è Shǐ Wǒmen Biàn Chéng Báichī",
    zh_content: "Zuì'è shǐ wǒmen dōu biàn chéng báichī; Jīdū lái dào shì wèile chúqù shēntǐ de zuì'è (jíbìng) yǐjí línghún de zuì'è!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SIN MAKES IDIOTS" AND c.name = "content.SIN MAKES IDIOTS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIN MAKES IDIOTS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.SIN MAKES IDIOTS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >SIN MAKES IDIOTS" }]->(child);
```

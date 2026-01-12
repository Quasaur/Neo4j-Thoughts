---
name: "thought.SIN IS EXPENSIVE"
alias: "Thought: Sin Is Expensive"
type: THOUGHT
en_content: "Law enforcement, court costs incarceration, healthcare, security, protection, insurance premiums, funeral costs...Sin is expensive!"
parent: "topic.MORALITY"
tags:
- sin
- cost
- society
- morality
- consequences
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Nov-2013a)
CREATE (t:THOUGHT {
    name: "thought.SIN IS EXPENSIVE",
    alias: "Thought: Sin Is Expensive",
    parent: "topic.MORALITY",
    tags: ['sin', 'cost', 'society', 'morality', 'consequences'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIN IS EXPENSIVE",
    en_title: "Sin Is Expensive",
    en_content: "Law enforcement, court costs incarceration, healthcare, security, protection, insurance premiums, funeral costs...Sin is expensive!",
    es_title: "El Pecado Es Costoso",
    es_content: "Aplicación de la ley, costos judiciales, encarcelamiento, atención médica, seguridad, protección, primas de seguro, costos funerarios...¡El pecado es costoso!",
    fr_title: "Le Péché Coûte Cher",
    fr_content: "Application de la loi, frais judiciaires, incarcération, soins de santé, sécurité, protection, primes d'assurance, frais funéraires...Le péché coûte cher !",
    hi_title: "पाप महंगा है",
    hi_content: "कानून व्यवस्था, न्यायालय की लागत, कारावास, स्वास्थ्य सेवा, सुरक्षा, संरक्षण, बीमा प्रीमियम, अंतिम संस्कार की लागत...पाप महंगा है!",
    zh_title: "Zuì È Hěn Ángguì",
    zh_content: "Zhí fǎ, fǎtíng fèiyòng, jiānjìn, yīliáo, ānquán, bǎohù, bǎoxiǎn fèi, zànglǐ fèiyòng...Zuì è hěn ángguì!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SIN IS EXPENSIVE" AND c.name = "content.SIN IS EXPENSIVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIN IS EXPENSIVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SIN IS EXPENSIVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SIN IS EXPENSIVE" }]->(child);
```

---
type: THOUGHT
name: "thought.TO BE LED"
alias: "Thought: To Be Led"
parent: "topic.GRACE"
tags: ["led", "follow", "leadership", "holy_spirit", "travel"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.TO BE LED",
    alias: "Thought: To Be Led",
    parent: "topic.GRACE",
    tags: ["led", "follow", "leadership", "holy_spirit", "travel"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TO BE LED",
    ctype: "THOUGHT",
    en_title: "To Be Led",
    en_content: "",
    es_title: "SER LED",
    es_content: "Ser “guiado” por el Espíritu Santo significa DEJAR donde estás y lo que crees saber, e ir a algún lugar donde nunca has estado… hacia lo Desconocido (Las Partes del Reino de Dios que nunca has visto antes).",
    fr_title: "A LED",
    fr_content: "Être « conduit » par le Saint-Esprit signifie QUITTER où vous êtes et ce que vous pensez savoir, et aller quelque part où vous n’êtes jamais allé… dans l’Inconnu (les parties du Royaume de Dieu que vous n’avez jamais vues auparavant).",
    hi_title: "द्वारा नेतृत्व",
    hi_content: "पवित्र आत्मा द्वारा \\\"नेतृत्व\\\" किए जाने का मतलब है कि आप जहां हैं और जो आप सोचते हैं कि आप जानते हैं उसे छोड़ दें, और ऐसी जगह चले जाएं जहां आप कभी नहीं गए हों... अज्ञात में (ईश्वर के राज्य के वे हिस्से जिन्हें आपने पहले कभी नहीं देखा है)।",
    zh_title: "bèi LED",
    zh_content: ""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TO BE LED"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->TO BE LED"
RETURN t, parent;
```

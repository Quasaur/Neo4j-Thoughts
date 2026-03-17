---
type: THOUGHT
name: "thought.TIME"
alias: "Thought: Time"
parent: "topic.JUSTICE"
tags: ["spirituality", "damnation", "soul", "lake_of_fire", "judgment"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.TIME",
    alias: "Thought: Time",
    parent: "topic.JUSTICE",
    tags: ["spirituality", "damnation", "soul", "lake_of_fire", "judgment"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.TIME",
    ctype: "THOUGHT",
    en_title: "Time",
    en_content: "",
    es_title: "TIEMPO",
    es_content: "Pasarás más tiempo en la Eternidad que en esta vida (o en vidas “anteriores”)… ¡¿y NO te preocupas por el destino de tu alma?!",
    fr_title: "TEMPS",
    fr_content: "Vous passerez plus de temps dans l’Éternité que vous ne l’avez jamais fait dans cette vie (ou dans vos vies « précédentes »)… et vous n’avez AUCUNE préoccupation concernant le sort de votre âme ?!",
    hi_title: "समय",
    hi_content: "आप अनंत काल में इस जीवन (या \\\"पिछले\\\" जीवन) की तुलना में अधिक समय व्यतीत करेंगे...और आपको अपनी आत्मा के भाग्य के बारे में कोई चिंता नहीं है?!",
    zh_title: "shí jiān",
    zh_content: ""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TIME"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.JUSTICE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.JUSTICE->TIME"
RETURN t, parent;
```

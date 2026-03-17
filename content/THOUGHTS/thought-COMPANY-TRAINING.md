---
type: THOUGHT
name: "thought.COMPANY TRAINING"
alias: "Thought: Company Training"
parent: "topic.PSYCHOLOGY"
en_content: "Why is it that companies don't give their employees time to complete Web- and Computer-based training courses?"
tags: ["time", "training", "courses", "company", "mismanagement"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.COMPANY TRAINING",
    alias: "Thought: Company Training",
    parent: "topic.PSYCHOLOGY",
    tags: ["time", "training", "courses", "company", "mismanagement"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.COMPANY TRAINING",
    ctype: "THOUGHT",
    en_title: "Company Training",
    en_content: "Why is it that companies don't give their employees time to complete Web- and Computer-based training courses?",
    es_title: "FORMACIÓN EN EMPRESA",
    es_content: "¿Por qué las empresas no dan a sus empleados tiempo para completar cursos de formación basados ​​en la Web y en ordenador?",
    fr_title: "FORMATION EN ENTREPRISE",
    fr_content: "Pourquoi les entreprises ne donnent-elles pas à leurs employés le temps de suivre des formations sur le Web et sur ordinateur ?",
    hi_title: "कंपनी प्रशिक्षण",
    hi_content: "ऐसा क्यों है कि कंपनियां अपने कर्मचारियों को वेब और कंप्यूटर-आधारित प्रशिक्षण पाठ्यक्रम पूरा करने के लिए समय नहीं देती हैं?",
    zh_title: "gōng sī péi xùn",
    zh_content: "wèi shén me gōng sī bù gěi yuán gōng shí jiān wán chéng jī yú wǎng luò hé jì suàn jī de péi xùn kè chéng ？"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.COMPANY TRAINING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->COMPANY TRAINING"
RETURN t, parent;
```

---
name: "thought.COMPANY_TRAINING"
alias: "Thought: COMPANY TRAINING"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- time
- training
- courses
- company
- mismanagement
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.COMPANY_TRAINING",
    alias: "Thought: COMPANY TRAINING",
    parent: "topic.PSYCHOLOGY",
    tags: ["time", "training", "courses", "company", "mismanagement"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.COMPANY_TRAINING",
    en_title: "COMPANY TRAINING",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.COMPANY_TRAINING" AND c.name = "content.COMPANY_TRAINING"
MERGE (t)-[:HAS_CONTENT {name: "edge.COMPANY_TRAINING"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.COMPANY_TRAINING"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->COMPANY_TRAINING"}]->(child);
```

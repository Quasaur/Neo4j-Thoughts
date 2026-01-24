---
name: "thought.DEHUMANIZING LABOR WATCHING"
alias: "Thought: Dehumanizing Labor Watching"
type: THOUGHT
en_content: "To those that continue to dehumanize blue and white collar laborers: GOD IS WATCHING."
parent: "topic.MORALITY"
tags:
- labor
- dehumanization
- watching
- justice
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jul-2013b)
CREATE (t:THOUGHT {
    name: "thought.DEHUMANIZING LABOR WATCHING",
    alias: "Thought: Dehumanizing Labor Watching",
    parent: "topic.MORALITY",
    tags: ['labor', 'dehumanization', 'watching', 'justice', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEHUMANIZING LABOR WATCHING",
    en_title: "Dehumanizing Labor Watching",
    en_content: "To those that continue to dehumanize blue and white collar laborers: GOD IS WATCHING.",
    es_title: "Dios Observa la Deshumanización Laboral",
    es_content: "A aquellos que continúan deshumanizando a los trabajadores de cuello azul y blanco: DIOS ESTÁ OBSERVANDO.",
    fr_title: "Dieu Observe la Déshumanisation du Travail",
    fr_content: "À ceux qui continuent à déshumaniser les travailleurs cols bleus et cols blancs : DIEU REGARDE.",
    hi_title: "श्रम का अमानवीकरण देख रहा परमेश्वर",
    hi_content: "उन लोगों के लिए जो नीले और सफेद कॉलर श्रमिकों का अमानवीकरण करना जारी रखते हैं: परमेश्वर देख रहा है।",
    zh_title: "Shén zài kànzhe láodòng de qùrénxìnghuà",
    zh_content: "Duì nàxiē jìxù shǐ lánlǐng hé báilǐng láodòngzhě qùrénxìnghuà de rén: SHÀNGDÌ ZÀI KÀNZHE."
});

MATCH (t:THOUGHT {name: "thought.DEHUMANIZING LABOR WATCHING"})
MATCH (c:CONTENT {name: "content.DEHUMANIZING LABOR WATCHING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEHUMANIZING LABOR WATCHING" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.DEHUMANIZING LABOR WATCHING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->DEHUMANIZING LABOR WATCHING" }]->(child);
```

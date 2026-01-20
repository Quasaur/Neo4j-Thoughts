---
name: "thought.IMPORTANCE OF DEUTERONOMY"
alias: "Thought: Importance Of Deuteronomy"
type: THOUGHT
en_content: "I'm convinced that the most important book of the Old Testament is Deuteronomy, which contains the ENTIRE PANORAMA of Biblical history."
parent: "topic.TRUTH"
tags:
- bible
- truth
- history
- deuteronomy
- law
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.IMPORTANCE OF DEUTERONOMY",
    alias: "Thought: Importance Of Deuteronomy",
    parent: "topic.TRUTH",
    tags: ['bible', 'truth', 'history', 'deuteronomy', 'law'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IMPORTANCE OF DEUTERONOMY",
    en_title: "Importance Of Deuteronomy",
    en_content: "I'm convinced that the most important book of the Old Testament is Deuteronomy, which contains the ENTIRE PANORAMA of Biblical history.",
    es_title: "Importancia del Deuteronomio",
    es_content: "Estoy convencido de que el libro más importante del Antiguo Testamento es Deuteronomio, que contiene todo el PANORAMA COMPLETO de la historia bíblica.",
    fr_title: "Importance du Deutéronome",
    fr_content: "Je suis convaincu que le livre le plus important de l'Ancien Testament est le Deutéronome, qui contient le PANORAMA ENTIER de l'histoire biblique.",
    hi_title: "व्यवस्थाविवरण का महत्व",
    hi_content: "मैं आश्वस्त हूं कि पुराने नियम की सबसे महत्वपूर्ण पुस्तक व्यवस्थाविवरण है, जिसमें बाइबिल के इतिहास का संपूर्ण चित्रपट समाहित है।",
    zh_title: "Shēnmìngjì de Zhòngyàoxìng",
    zh_content: "Wǒ xiāngxìn Jiùyuē zhōng zuì zhòngyào de shū shì Shēnmìngjì, tā bāohánle Shèngjīng lìshǐ de ZHĚNGGÈ QUÁNJǏNG."
});

MATCH (t:THOUGHT {name: "thought.IMPORTANCE OF DEUTERONOMY"})
MATCH (c:CONTENT {name: "content.IMPORTANCE OF DEUTERONOMY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.IMPORTANCE OF DEUTERONOMY" }]->(c);

MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:THOUGHT {name: "thought.IMPORTANCE OF DEUTERONOMY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >IMPORTANCE OF DEUTERONOMY" }]->(child);
```

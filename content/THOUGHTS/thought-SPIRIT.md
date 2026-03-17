---
type: THOUGHT
name: "thought.SPIRIT"
alias: "Thought: Spirit"
parent: "topic.SPIRITS"
tags: ["holy_spirit", "spirit_of_christ", "spirit_of_truth", "spirit_of_grace", "jesus_christ"]
ptopic: "[[topic-SPIRITS]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SPIRIT",
    alias: "Thought: Spirit",
    parent: "topic.SPIRITS",
    tags: ["holy_spirit", "spirit_of_christ", "spirit_of_truth", "spirit_of_grace", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SPIRIT",
    ctype: "THOUGHT",
    en_title: "Spirit",
    en_content: "",
    es_title: "ESPÍRITU",
    es_content: "La cuenta de los espíritus en el cosmos es innumerable; sin embargo, ¡solo UN ESPÍRITU lleva el Título SANTO (los ángeles y los santos no cuentan, porque su santidad es PRESTADA)!",
    fr_title: "ESPRIT",
    fr_content: "Le nombre d’esprits dans le cosmos est incalculable ; cependant un SEUL ESPRIT porte le Titre SAINT (les anges et les saints ne comptent pas, car leur sainteté est EMPRUNT) !",
    hi_title: "आत्मा",
    hi_content: "ब्रह्मांड में आत्माओं की गिनती अनगिनत है; हालाँकि केवल एक आत्मा ही पवित्र उपाधि रखती है (स्वर्गदूतों और संतों की गिनती नहीं है, क्योंकि उनकी पवित्रता उधार ली गई है)!",
    zh_title: "jīng shén",
    zh_content: "yǔ zhòu zhōng de shén líng shǔ bù shèng shǔ ， rán ér ， zhǐ yǒu yī zhǒng jīng shén jù yǒu shén shèng de chēng hào （ tiān shǐ hé shèng rén bù suàn shù ， yīn wèi tā men de shén shèng xìng shì jiè lái de ）！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SPIRIT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITS->SPIRIT"
RETURN t, parent;
```

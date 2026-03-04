---
type: THOUGHT
name: "thought.SPIRIT"
alias: "Thought: Spirit"
parent: "topic.SPIRITS"
tags: ["holy_spirit", "spirit_of_christ", "spirit_of_truth", "spirit_of_grace", "jesus_christ"]
ptopic: "[[topic-SPIRITS]]"
level: 3
neo4j: true
---

```Cypher
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
 es_title: "ESPÍRITU",
 fr_title: "ESPRIT",
 hi_title: "आत्मा",
 zh_title: "jīng shén",
    en_content: "",
 es_content: "La cuenta de los espíritus en el cosmos es innumerable; sin embargo, ¡solo UN ESPÍRITU lleva el Título SANTO (los ángeles y los santos no cuentan, porque su santidad es PRESTADA)!",
 fr_content: "Le nombre d’esprits dans le cosmos est incalculable ; cependant un SEUL ESPRIT porte le Titre SAINT (les anges et les saints ne comptent pas, car leur sainteté est EMPRUNT) !",
 hi_content: "ब्रह्मांड में आत्माओं की गिनती अनगिनत है; हालाँकि केवल एक आत्मा ही पवित्र उपाधि रखती है (स्वर्गदूतों और संतों की गिनती नहीं है, क्योंकि उनकी पवित्रता उधार ली गई है)!",
 zh_content: "yǔ zhòu zhōng de shén líng shǔ bù shèng shǔ ， rán ér ， zhǐ yǒu yī zhǒng jīng shén jù yǒu shén shèng de chēng hào （ tiān shǐ hé shèng rén bù suàn shù ， yīn wèi tā men de shén shèng xìng shì jiè lái de ）！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SPIRIT" AND c.name = "content.SPIRIT"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.SPIRIT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITS" AND child.name = "thought.SPIRIT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.SPIRITS->SPIRIT"}]->(child);
```
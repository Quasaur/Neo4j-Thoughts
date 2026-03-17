---
type: THOUGHT
name: "thought.DIVINE WORTH"
alias: "Thought: Divine Worth"
parent: "topic.HOLINESS"
en_content: "God is holy. Which means that God is worth more than you or I...more than all the life in the cosmos put together."
tags: ["deity", "holy", "worth", "value", "diine"]
ptopic: "[[topic-HOLINESS]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DIVINE WORTH",
    alias: "Thought: Divine Worth",
    parent: "topic.HOLINESS",
    tags: ["deity", "holy", "worth", "value", "diine"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DIVINE WORTH",
    ctype: "THOUGHT",
    en_title: "Divine Worth",
    en_content: "God is holy. Which means that God is worth more than you or I...more than all the life in the cosmos put together.",
    es_title: "VALOR DIVINO",
    es_content: "Dios es santo. Lo que significa que Dios vale más que tú o que yo... más que toda la vida en el cosmos junta.",
    fr_title: "VALEUR DIVINE",
    fr_content: "Dieu est saint. Ce qui signifie que Dieu vaut plus que vous ou moi... plus que toute la vie du cosmos réunie.",
    hi_title: "दिव्य मूल्य",
    hi_content: "भगवान पवित्र है. जिसका अर्थ यह है कि ईश्वर आपसे या मुझसे अधिक मूल्यवान है...ब्रह्मांड के समस्त जीवन से अधिक मूल्यवान है।",
    zh_title: "shén shèng de jià zhí",
    zh_content: "shàng dì shì shén shèng de 。 zhè yì wèi zhe shàng dì bǐ nǐ huò wǒ gèng yǒu jià zhí …… bǐ yǔ zhòu zhōng suǒ yǒu shēng mìng de zǒng hé gèng yǒu jià zhí 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DIVINE WORTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HOLINESS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HOLINESS->DIVINE WORTH"
RETURN t, parent;
```

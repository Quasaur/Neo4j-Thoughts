---
type: THOUGHT
name: "thought.JUSTICE"
alias: "Thought: Justice"
parent: "topic.JUSTICE"
tags: ["justice", "spirituality", "forgiveness", "gospel", "fair"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.JUSTICE",
    alias: "Thought: Justice",
    parent: "topic.JUSTICE",
    tags: ["justice", "spirituality", "forgiveness", "gospel", "fair"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.JUSTICE",
    ctype: "THOUGHT",
    en_title: "Justice",
    en_content: "",
    es_title: "Justicia",
    es_content: "Tienes razón: El Evangelio de Jesucristo no es justo… ¡pero es justo!
No es justo que a NINGÚN pecador se le perdonen sus pecados y escape del Lago de Fuego y Azufre; sin embargo, ¡es justo que La Cruz de Cristo expía al pecador que, por la Fe, está clavado en Esa Misma Cruz junto con Cristo! 
Gálatas 2:20",
    fr_title: "Justice",
    fr_content: "Vous avez raison : l’Évangile de Jésus-Christ n’est pas juste… pourtant il est juste !
Il n'est pas juste que TOUT pécheur soit pardonné de ses péchés et échappe au Lac de Feu et de Soufre ; pourtant, il est juste que la Croix du Christ expie le pécheur qui, par la foi, est cloué sur cette même croix avec Christ ! 
Galates 2:20",
    hi_title: "न्याय",
    hi_content: "आप सही हैं: यीशु मसीह का सुसमाचार निष्पक्ष नहीं है... फिर भी यह उचित है!
यह उचित नहीं है कि किसी भी पापी को उसके पापों को माफ कर दिया जाए और वह आग और गंधक की झील से बच जाए; फिर भी यह पापी के लिए प्रायश्चित करने के लिए मसीह के क्रॉस के लिए है, जो विश्वास के द्वारा, मसीह के साथ उसी क्रॉस पर कीलों से ठोका गया है! 
गलातियों 2:20",
    zh_title: "zhèng yì",
    zh_content: "nǐ shì duì de ： yē sū jī dū de fú yīn bù gōng píng …… dàn què shì gōng zhèng de ！
 rèn hé zuì rén de zuì niè bèi kuān shù bìng táo lí huǒ yǔ liú huáng zhī hú shì bù gōng píng de ； rán ér ， zhǐ yǒu jī dū de shí zì jià cái néng wèi zuì rén shú zuì ， zuì rén píng zhe xìn xīn ， yǔ jī dū yì qǐ bèi dīng zài tóng yī gè shí zì jià shàng ！ 
 jiā lā tài shū  2:20"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.JUSTICE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.JUSTICE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.JUSTICE->JUSTICE"
RETURN t, parent;
```

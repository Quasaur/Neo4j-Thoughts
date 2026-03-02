---
type: THOUGHT
name: "thought.JUSTICE"
alias: "Thought: Justice"
parent: "topic.JUSTICE"
tags: ["justice", "spirituality", "forgiveness", "gospel", "fair"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
---

```Cypher
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
 es_title: "Justicia",
 fr_title: "Justice",
 hi_title: "न्याय",
 zh_title: "zhèng yì",
    en_content: "",
 es_content: "Tienes razón: El Evangelio de Jesucristo no es justo… ¡pero es justo!
No es justo que a NINGÚN pecador se le perdonen sus pecados y escape del Lago de Fuego y Azufre; sin embargo, ¡es justo que La Cruz de Cristo expía al pecador que, por la Fe, está clavado en Esa Misma Cruz junto con Cristo! 
Gálatas 2:20",
 fr_content: "Vous avez raison : l’Évangile de Jésus-Christ n’est pas juste… pourtant il est juste !
Il n'est pas juste que TOUT pécheur soit pardonné de ses péchés et échappe au Lac de Feu et de Soufre ; pourtant, il est juste que la Croix du Christ expie le pécheur qui, par la foi, est cloué sur cette même croix avec Christ ! 
Galates 2:20",
 hi_content: "आप सही हैं: यीशु मसीह का सुसमाचार निष्पक्ष नहीं है... फिर भी यह उचित है!
यह उचित नहीं है कि किसी भी पापी को उसके पापों को माफ कर दिया जाए और वह आग और गंधक की झील से बच जाए; फिर भी यह पापी के लिए प्रायश्चित करने के लिए मसीह के क्रॉस के लिए है, जो विश्वास के द्वारा, मसीह के साथ उसी क्रॉस पर कीलों से ठोका गया है! 
गलातियों 2:20",
 zh_content: "nǐ shì duì de ： yē sū jī dū de fú yīn bù gōng píng …… dàn què shì gōng zhèng de ！
 rèn hé zuì rén de zuì niè bèi kuān shù bìng táo lí huǒ yǔ liú huáng zhī hú shì bù gōng píng de ； rán ér ， zhǐ yǒu jī dū de shí zì jià cái néng wèi zuì rén shú zuì ， zuì rén píng zhe xìn xīn ， yǔ jī dū yì qǐ bèi dīng zài tóng yī gè shí zì jià shàng ！ 
 jiā lā tài shū  2:20"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.JUSTICE" AND c.name = "content.JUSTICE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.JUSTICE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.JUSTICE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.JUSTICE->JUSTICE"}]->(child);
```
---
type: THOUGHT
name: "thought.THE IRC"
alias: "Thought: The Irc"
parent: "topic.FIN GOV"
en_content: "The United States tax code, otherwise know as the Internal Revenue Code (IRC), was written by The Devil; his paw prints are all over it."
tags: ["government", "finance", "code", "usa", "tax"]
ptopic: "[[topic-FIN GOV]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.THE IRC",
    alias: "Thought: The Irc",
    parent: "topic.FIN GOV",
    tags: ["government", "finance", "code", "usa", "tax"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.THE IRC",
    ctype: "THOUGHT",
    en_title: "The Irc",
    en_content: "The United States tax code, otherwise know as the Internal Revenue Code (IRC), was written by The Devil; his paw prints are all over it.",
    es_title: "EL IRC",
    es_content: "El código tributario de los Estados Unidos, también conocido como Código de Rentas Internas (IRC), fue escrito por El Diablo; sus huellas están por todas partes.",
    fr_title: "LE IRC",
    fr_content: "Le code fiscal des États-Unis, également connu sous le nom d’Internal Revenue Code (IRC), a été rédigé par le Diable ; ses empreintes de pattes sont partout.",
    hi_title: "आईआरसी",
    hi_content: "संयुक्त राज्य कर कोड, जिसे अन्यथा आंतरिक राजस्व कोड (आईआरसी) के रूप में जाना जाता है, द डेविल द्वारा लिखा गया था; उसके पंजे के निशान इस पर हैं।",
    zh_title: "IRC",
    zh_content: "měi guó shuì fǎ ， yě chēng wéi 《 guó nèi shuì shōu fǎ diǎn 》（IRC）， shì yóu mó guǐ zhì dìng de ； shàng miàn dào chù dōu shì tā de zhǎo yìn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.THE IRC"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FIN GOV"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FIN GOV->THE IRC"
RETURN t, parent;
```

---
type: THOUGHT
name: "thought.US FOREIGN POLICY"
alias: "Thought: Dark Us Foreign Policy"
parent: "topic.POLITICAL SCIENCE"
en_content: "USA foreign policy is imperial, dictatorial, ruthless, dirty, immoral...inevitably invoking the WRATH OF GOD against us all."
tags: ["usa", "foreignpolicy", "govoverthrow", "wrath_of_god", "threat"]
ptopic: "[[topic-POLITICAL SCIENCE]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.US FOREIGN POLICY",
    alias: "Thought: Dark Us Foreign Policy",
    parent: "topic.POLITICAL SCIENCE",
    tags: ["usa", "foreignpolicy", "govoverthrow", "wrath_of_god", "threat"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.US FOREIGN POLICY",
    ctype: "THOUGHT",
    en_title: "Dark Us Foreign Policy",
    en_content: "USA foreign policy is imperial, dictatorial, ruthless, dirty, immoral...inevitably invoking the WRATH OF GOD against us all.",
    es_title: "OSCURA POLÍTICA EXTERIOR DE EE.UU.",
    es_content: "La política exterior de Estados Unidos es imperial, dictatorial, despiadada, sucia, inmoral... inevitablemente invoca la IRA DE DIOS contra todos nosotros.",
    fr_title: "UNE POLITIQUE ÉTRANGÈRE AMÉRICAINE SOMBRE",
    fr_content: "La politique étrangère des États-Unis est impériale, dictatoriale, impitoyable, sale, immorale… invoquant inévitablement la COLÈRE DE DIEU contre nous tous.",
    hi_title: "अंधकारमय अमेरिकी विदेश नीति",
    hi_content: "संयुक्त राज्य अमेरिका की विदेश नीति शाही, तानाशाही, क्रूर, गंदी, अनैतिक है... अनिवार्य रूप से हम सभी के खिलाफ भगवान के क्रोध का आह्वान करती है।",
    zh_title: "hēi àn de měi guó wài jiāo zhèng cè",
    zh_content: "měi guó de wài jiāo zhèng cè shì dì guó zhǔ yì de 、 dú cái de 、 wú qíng de 、 āng zāng de 、 bù dào dé de …… bù kě bì miǎn dì huì yǐn qǐ shàng dì duì wǒ men suǒ yǒu rén de fèn nù 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.US FOREIGN POLICY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.POLITICAL-SCIENCE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.POLITICAL SCIENCE->US FOREIGN POLICY"
RETURN t, parent;
```

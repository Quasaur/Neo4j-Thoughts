---
name: "thought.US_FOREIGN_POLICY"
alias: "Thought: DARK US FOREIGN POLICY"
type: THOUGHT
parent: topic.POLITICAL-SCIENCE
tags:
- usa
- foreignpolicy
- govoverthrow
- wrathofgod
- threat
neo4j: true
ptopic: "[[topic-POLITICAL-SCIENCE]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.US_FOREIGN_POLICY",
    alias: "Thought: DARK US FOREIGN POLICY",
    parent: "topic.POLITICAL-SCIENCE",
    tags: ["usa", "foreignpolicy", "govoverthrow", "wrathofgod", "threat"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.US_FOREIGN_POLICY",
    en_title: "DARK US FOREIGN POLICY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.US_FOREIGN_POLICY" AND c.name = "content.US_FOREIGN_POLICY"
MERGE (t)-[:HAS_CONTENT {name: "edge.US_FOREIGN_POLICY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.POLITICAL-SCIENCE" AND child.name = "thought.US_FOREIGN_POLICY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.POLITICAL-SCIENCE->US_FOREIGN_POLICY"}]->(child);
```

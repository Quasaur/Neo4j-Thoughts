---
type: THOUGHT
name: "thought.YISRAEL"
alias: "Thought: Yisrael"
parent: "topic.HISTORY"
tags: ["israel", "apartheid", "genocide", "palestinians", "jesus_christ"]
ptopic: "[[topic-HISTORY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.YISRAEL",
    alias: "Thought: Yisrael",
    parent: "topic.HISTORY",
    tags: ["israel", "apartheid", "genocide", "palestinians", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.YISRAEL",
    ctype: "THOUGHT",
    en_title: "Yisrael",
    en_content: "",
    es_title: "YISRAEL",
    es_content: "Dos errores no hacen un bien… hasta que Israel reconozca a Jesús como el Mesías y se arrepienta de su apartheid y sus prácticas genocidas contra sus ciudadanos no judíos, “las desolaciones están determinadas…”
Daniel 9:26",
    fr_title: "YISRAËL",
    fr_content: "Deux torts ne font pas un bien… jusqu’à ce qu’Israël reconnaisse Jésus comme le Messie et se repente de ses pratiques d’apartheid et de génocide contre ses citoyens non juifs, « les désolations sont déterminées… »
Daniel 9:26",
    hi_title: "इजरेल",
    hi_content: "दो गलतियाँ सही नहीं बनतीं...जब तक इज़राइल यीशु को मसीहा के रूप में स्वीकार नहीं करता और अपने गैर-यहूदी नागरिकों के खिलाफ रंगभेद और नरसंहार प्रथाओं के लिए पश्चाताप नहीं करता, \\\"विनाश निर्धारित है...\\\"
दानिय्येल 9:26",
    zh_title: "yǐ sè liè",
    zh_content: "liǎng gè cuò wù bìng bù néng gòu chéng yí gè zhèng què …… chú fēi yǐ sè liè chéng rèn yē sū shì mí sài yà ， bìng duì qí zhēn duì fēi yóu tài gōng mín de zhǒng zú gé lí hé zhǒng zú miè jué zuò fǎ jìn xíng chàn huǐ ，“ huāng liáng yǐ chéng dìng jú ……”
 dàn yǐ lǐ shū  9:26"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.YISRAEL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HISTORY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HISTORY->YISRAEL"
RETURN t, parent;
```

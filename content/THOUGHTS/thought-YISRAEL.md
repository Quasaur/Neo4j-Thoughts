---
type: THOUGHT
name: "thought.YISRAEL"
alias: "Thought: YISRAEL"
parent: "topic.HISTORY"
tags: ["israel", "apartheid", "genocide", "palestinians", "jesus_christ"]
ptopic: "[[topic-HISTORY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.YISRAEL",
    alias: "Thought: YISRAEL",
    parent: "topic.HISTORY",
    tags: ["israel", "apartheid", "genocide", "palestinians", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.YISRAEL",
    ctype: "THOUGHT",
    en_title: "YISRAEL",
 es_title: "YISRAEL",
 fr_title: "YISRAËL",
 hi_title: "इजरेल",
 zh_title: "yǐ sè liè",
    en_content: "",
 es_content: "Dos errores no hacen un bien… hasta que Israel reconozca a Jesús como el Mesías y se arrepienta de su apartheid y sus prácticas genocidas contra sus ciudadanos no judíos, “las desolaciones están determinadas…”
Daniel 9:26",
 fr_content: "Deux torts ne font pas un bien… jusqu’à ce qu’Israël reconnaisse Jésus comme le Messie et se repente de ses pratiques d’apartheid et de génocide contre ses citoyens non juifs, « les désolations sont déterminées… »
Daniel 9:26",
 hi_content: "दो गलतियाँ सही नहीं बनतीं...जब तक इज़राइल यीशु को मसीहा के रूप में स्वीकार नहीं करता और अपने गैर-यहूदी नागरिकों के खिलाफ रंगभेद और नरसंहार प्रथाओं के लिए पश्चाताप नहीं करता, \"विनाश निर्धारित है...\"
दानिय्येल 9:26"विनाश निर्धारित है...\"
दानिय्येल 9:26"विनाश निर्धारित है...\"
दानिय्येल 9:26"विनाश निर्धारित है...\"
दानिय्येल 9:26",
 zh_content: "liǎng gè cuò wù bìng bù néng gòu chéng yí gè zhèng què …… chú fēi yǐ sè liè chéng rèn yē sū shì mí sài yà ， bìng duì qí zhēn duì fēi yóu tài gōng mín de zhǒng zú gé lí hé zhǒng zú miè jué zuò fǎ jìn xíng chàn huǐ ，“ huāng liáng yǐ chéng dìng jú ……”
 dàn yǐ lǐ shū  9:26"विनाश निर्धारित है...\"\nदानिय्येल 9:26"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.YISRAEL" AND c.name = "content.YISRAEL"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.YISRAEL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HISTORY" AND child.name = "thought.YISRAEL"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HISTORY->YISRAEL"}]->(child);
```
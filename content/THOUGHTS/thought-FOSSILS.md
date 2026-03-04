---
type: THOUGHT
name: "thought.FOSSILS"
alias: "Thought: Fossils"
parent: "topic.GEOLOGY"
tags: ["geology", "fossils", "creationism", "intelligentdesign", "evidence"]
ptopic: "[[topic-GEOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FOSSILS",
    alias: "Thought: Fossils",
    parent: "topic.GEOLOGY",
    tags: ["geology", "fossils", "creationism", "intelligentdesign", "evidence"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FOSSILS",
    ctype: "THOUGHT",
    en_title: "Fossils",
 es_title: "FÓSILES",
 fr_title: "FOSSILES",
 hi_title: "जीवाश्मों",
 zh_title: "huà shí",
    en_content: "",
 es_content: "¡Los fósiles, que según los evolucionistas demuestran cuán antigua es la Tierra, HAN SIDO DISEÑADOS EN LABORATORIOS EN 24 HORAS!",
 fr_content: "Les fossiles, qui, selon les évolutionnistes, prouvent l'ancienneté de la Terre, ONT ÉTÉ CONÇUS DANS DES LABORATOIRES EN 24 HEURES !",
 hi_content: "जीवाश्म, जिनके बारे में विकासवादियों का कहना है कि यह साबित करते हैं कि पृथ्वी कितनी प्राचीन है, 24 घंटों के भीतर प्रयोगशालाओं में इंजीनियर किए गए हैं!",
 zh_content: "jìn huà lùn zhě chēng huà shí zhèng míng liǎo dì qiú yǒu duō gǔ lǎo ， ér huà shí yǐ zài  24  xiǎo shí nèi zài shí yàn shì zhōng dàn shēng ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FOSSILS" AND c.name = "content.FOSSILS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FOSSILS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GEOLOGY" AND child.name = "thought.FOSSILS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GEOLOGY->FOSSILS"}]->(child);
```
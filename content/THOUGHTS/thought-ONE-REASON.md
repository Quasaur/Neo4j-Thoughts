---
type: THOUGHT
name: "thought.ONE REASON"
alias: "Thought: One Reason"
parent: "topic.ATTITUDE"
en_content: |
  There’s one reason why many will find themselves in the Lake of Fire when they could’ve been saved: Pride.
  Lay down your weapons and surrender your body and soul to The Lord Jesus Christ…you will NOT regret it!"
tags: ["apocalypse", "lake_of_fire", "pride", "judgment", "jesus_christ"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ONE REASON",
    alias: "Thought: One Reason",
    parent: "topic.ATTITUDE",
    tags: ["apocalypse", "lake_of_fire", "pride", "judgment", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ONE REASON",
    ctype: "THOUGHT",
    en_title: "One Reason",
    en_content: "There’s one reason why many will find themselves in the Lake of Fire when they could’ve been saved: Pride.
Lay down your weapons and surrender your body and soul to The Lord Jesus Christ…you will NOT regret it!",
    es_title: "UNA RAZÓN",
    es_content: "Hay una razón por la que muchos se encontrarán en el Lago de Fuego cuando podrían haber sido salvados: el orgullo.
Depongan sus armas y entreguen su cuerpo y alma a El Señor Jesucristo… ¡NO se arrepentirán!",
    fr_title: "UNE RAISON",
    fr_content: "Il y a une raison pour laquelle beaucoup se retrouveront dans l’étang de feu alors qu’ils auraient pu être sauvés : la fierté.
Déposez vos armes et abandonnez votre corps et votre âme au Seigneur Jésus-Christ… vous ne le regretterez PAS !",
    hi_title: "एक कारण",
    hi_content: "एक कारण है कि कई लोग खुद को आग की झील में पाएंगे जबकि उन्हें बचाया जा सकता था: गौरव।
अपने हथियार डाल दो और अपने शरीर और आत्मा को प्रभु यीशु मसीह को सौंप दो... तुम्हें इसका पछतावा नहीं होगा!",
    zh_title: "yí gè yuán yīn",
    zh_content: "xǔ duō rén běn lái kě yǐ dé jiù ， què fā xiàn zì jǐ diào jìn le huǒ hú ， yuán yīn zhǐ yǒu yí gè ： jiāo ào 。
 fàng xià nǐ de wǔ qì ， jiāng nǐ de shēn tǐ hé líng hún jiāo gěi zhǔ yē sū jī dū …… nǐ bú huì hòu huǐ de ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ONE REASON"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->ONE REASON"
RETURN t, parent;
```

---
type: THOUGHT
name: "thought.CHRIST COMING CLOUDS"
alias: "Thought: Christ Coming Clouds"
parent: "topic.RELIGION"
en_content: "History is going to play out just as the Bible says; what are you going to do when you see Christ coming in the clouds of Heaven?"
tags: ["prophecy", "jesus", "return", "eternity", "judgment"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Jun-2012)
CREATE (t:THOUGHT {    name: "thought.CHRIST COMING CLOUDS",
    alias: "Thought: Christ Coming Clouds",
    parent: "topic.RELIGION",
    tags: ['prophecy', 'jesus', 'return', 'eternity', 'judgment'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.CHRIST COMING CLOUDS",
    ctype: "THOUGHT",
    en_title: "Christ Coming Clouds",
    en_content: "History is going to play out just as the Bible says; what are you going to do when you see Christ coming in the clouds of Heaven?",
    es_title: "Cristo Viniendo en las Nubes",
    es_content: "La historia se desarrollará tal como lo dice la Biblia; ¿qué vas a hacer cuando veas a Cristo viniendo en las nubes del Cielo?",
    fr_title: "Le Christ Venant dans les Nuées",
    fr_content: "L'histoire se déroulera exactement comme la Bible le dit ; que ferez-vous lorsque vous verrez le Christ venir dans les nuées du Ciel ?",
    hi_title: "मसीह बादलों में आ रहे हैं",
    hi_content: "इतिहास वैसा ही घटित होगा जैसा बाइबिल कहती है; जब आप मसीह को स्वर्ग के बादलों में आते देखेंगे तो आप क्या करेंगे?",
    zh_title: "Jīdū Zài Yún Zhōng Jiànglín",
    zh_content: "Lìshǐ jiāng àn Shèngjīng suǒ shuō de fāzhǎn; Dāng nǐ kàn dào Jīdū zài tiānshàng de yún zhōng jiànglíng shí, Nǐ yào zuò shénme?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CHRIST COMING CLOUDS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->CHRIST COMING CLOUDS"
RETURN t, parent;
```

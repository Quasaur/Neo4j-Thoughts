---
type: THOUGHT
name: "thought.WICKEDNESS AND GUN LAWS"
alias: "Thought: Wickedness And Gun Laws"
parent: "topic.MORALITY"
en_content: "Humanity will continue to grow more wicked. As a nation we would be IDIOTS to leave our gun laws in their current state."
tags: ["guns", "law", "wickedness", "morality", "society"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013b)
CREATE (t:THOUGHT {    name: "thought.WICKEDNESS AND GUN LAWS",
    alias: "Thought: Wickedness And Gun Laws",
    parent: "topic.MORALITY",
    tags: ['guns', 'law', 'wickedness', 'morality', 'society'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.WICKEDNESS AND GUN LAWS",
    ctype: "THOUGHT",
    en_title: "Wickedness And Gun Laws",
    en_content: "Humanity will continue to grow more wicked. As a nation we would be IDIOTS to leave our gun laws in their current state.",
    es_title: "La Maldad Y Las Leyes De Armas",
    es_content: "La humanidad continuará volviéndose más malvada. Como nación seríamos IDIOTAS al dejar nuestras leyes de armas en su estado actual.",
    fr_title: "La Méchanceté Et Les Lois Sur Les Armes",
    fr_content: "L'humanité continuera à devenir de plus en plus méchante. En tant que nation, nous serions des IDIOTS de laisser nos lois sur les armes dans leur état actuel.",
    hi_title: "दुष्टता और बंदूक कानून",
    hi_content: "मानवता और भी दुष्ट होती जाएगी। एक राष्ट्र के रूप में हम मूर्ख होंगे यदि हम अपने बंदूक कानूनों को उनकी वर्तमान स्थिति में छोड़ दें।",
    zh_title: "Xié'è Hé Qiāngzhī Fǎlǜ",
    zh_content: "Rénlèi jiāng jìxù biàn dé gèng jiā xié'è. Zuòwéi yīgè guójiā, wǒmen rúguǒ ràng qiāngzhī fǎlǜ bǎochí xiànzhuàng jiù shì BÁICHĪ."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WICKEDNESS AND GUN LAWS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->WICKEDNESS AND GUN LAWS"
RETURN t, parent;
```

---
name: "thought.WICKEDNESS AND GUN LAWS"
alias: "Thought: Wickedness And Gun Laws"
type: THOUGHT
en_content: "Humanity will continue to grow more wicked. As a nation we would be IDIOTS to leave our gun laws in their current state."
parent: "topic.MORALITY"
tags:
- guns
- law
- wickedness
- morality
- society
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.WICKEDNESS AND GUN LAWS",
    alias: "Thought: Wickedness And Gun Laws",
    parent: "topic.MORALITY",
    tags: ['guns', 'law', 'wickedness', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WICKEDNESS AND GUN LAWS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WICKEDNESS AND GUN LAWS" AND c.name = "content.WICKEDNESS AND GUN LAWS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WICKEDNESS AND GUN LAWS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.WICKEDNESS AND GUN LAWS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >WICKEDNESS AND GUN LAWS" }]->(child);
```

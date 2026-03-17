---
type: THOUGHT
name: "thought.TREASURE"
alias: "Thought: Treasure"
parent: "topic.RELIGION"
tags: ["spirituality", "treasure", "wealth", "prosperity", "jesus_christ"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.TREASURE",
    alias: "Thought: Treasure",
    parent: "topic.RELIGION",
    tags: ["spirituality", "treasure", "wealth", "prosperity", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.TREASURE",
    ctype: "THOUGHT",
    en_title: "Treasure",
    en_content: "",
    es_title: "TESORO",
    es_content: "En La Cruz Jesús se vuelve TODO y nosotros nos convertimos en NADA; entonces los falsos evangelios se enfocan en las “bendiciones” de esta vida… mientras que el Verdadero Evangelio dirige nuestros corazones hacia la Bendición Eterna de CONOCER A CRISTO!!!! 
Mateo 6:21",
    fr_title: "TRÉSOR",
    fr_content: "À la croix, Jésus devient TOUT et nous ne devenons RIEN ; ainsi les faux évangiles se concentrent sur les « bénédictions » de cette vie… tandis que le véritable Évangile tourne nos cœurs vers la bénédiction éternelle de CONNAÎTRE LE CHRIST !!!! 
Matthieu 6:21",
    hi_title: "खज़ाना",
    hi_content: "क्रूस पर यीशु ही सब कुछ बन जाते हैं और हम कुछ भी नहीं बन जाते; इसलिए झूठे सुसमाचार इस जीवन के \\\"आशीर्वाद\\\" पर ध्यान केंद्रित करते हैं... जबकि वास्तविक सुसमाचार हमारे दिलों को मसीह को जानने के शाश्वत आशीर्वाद की ओर मोड़ता है!!!! 
मत्ती 6:21",
    zh_title: "bǎo zàng",
    zh_content: "zài shí zì jià shàng ， yē sū chéng wéi yī qiè ， ér wǒ men biàn dé yī wú suǒ yǒu ； yīn cǐ ， jiǎ fú yīn zhuān zhù yú jīn shēng de “ zhù fú ”…… ér zhēn zhèng de fú yīn zé jiāng wǒ men de xīn zhuǎn xiàng rèn shí jī dū de yǒng héng zhù fú ！！！！ 
 mǎ tài fú yīn  6:21"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TREASURE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->TREASURE"
RETURN t, parent;
```

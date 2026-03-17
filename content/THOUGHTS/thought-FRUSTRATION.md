---
type: THOUGHT
name: "thought.FRUSTRATION"
alias: "Thought: Frustration"
parent: "topic.FAITHFULNESS"
tags: ["frustration", "spirituality", "assurance", "fathergod", "jesus_christ"]
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FRUSTRATION",
    alias: "Thought: Frustration",
    parent: "topic.FAITHFULNESS",
    tags: ["frustration", "spirituality", "assurance", "fathergod", "jesus_christ"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FRUSTRATION",
    ctype: "THOUGHT",
    en_title: "Frustration",
    en_content: "",
    es_title: "FRUSTRACIÓN",
    es_content: "Te rendirás...
…antes que DIOS lo haga.
¡¡¡Ese es el PODER del Evangelio!!!
DIOS siempre termina lo que comienza, de lo contrario NINGUNO DE NOSOTROS se encontraría en el Cielo.",
    fr_title: "FRUSTRATION",
    fr_content: "Vous allez vous abandonner...
…avant DIEU.
C'est la PUISSANCE de l'Évangile !!!
DIEU termine toujours ce qu’Il ​​commence, sinon AUCUN D’ENTRE NOUS ne se retrouverait au paradis.",
    hi_title: "निराशा",
    hi_content: "तुम अपना साथ छोड़ दोगे...
...भगवान के ऐसा करने से पहले।
यही सुसमाचार की शक्ति है!!!
भगवान हमेशा जो शुरू करते हैं उसे पूरा करते हैं, अन्यथा हममें से कोई भी खुद को स्वर्ग में नहीं पाता।",
    zh_title: "cuò zhé",
    zh_content: "nǐ jiù huì fàng qì nǐ ...
…… zài shàng dì zhī qián 。
 zhè jiù shì fú yīn de lì liàng ！！！
 shàng dì zǒng shì wán chéng tā kāi shǐ de shì qíng ， fǒu zé wǒ men méi yǒu rén huì fā xiàn zì jǐ zài tiān táng 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FRUSTRATION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FAITHFULNESS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FAITHFULNESS->FRUSTRATION"
RETURN t, parent;
```

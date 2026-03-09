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
 es_title: "FRUSTRACIÓN",
 fr_title: "FRUSTRATION",
 hi_title: "निराशा",
 zh_title: "cuò zhé",
    en_content: "",
 es_content: "Te rendirás...
…antes que DIOS lo haga.
¡¡¡Ese es el PODER del Evangelio!!!
DIOS siempre termina lo que comienza, de lo contrario NINGUNO DE NOSOTROS se encontraría en el Cielo.",
 fr_content: "Vous allez vous abandonner...
…avant DIEU.
C'est la PUISSANCE de l'Évangile !!!
DIEU termine toujours ce qu’Il ​​commence, sinon AUCUN D’ENTRE NOUS ne se retrouverait au paradis.",
 hi_content: "तुम अपना साथ छोड़ दोगे...
...भगवान के ऐसा करने से पहले।
यही सुसमाचार की शक्ति है!!!
भगवान हमेशा जो शुरू करते हैं उसे पूरा करते हैं, अन्यथा हममें से कोई भी खुद को स्वर्ग में नहीं पाता।",
 zh_content: "nǐ jiù huì fàng qì nǐ ...
…… zài shàng dì zhī qián 。
 zhè jiù shì fú yīn de lì liàng ！！！
 shàng dì zǒng shì wán chéng tā kāi shǐ de shì qíng ， fǒu zé wǒ men méi yǒu rén huì fā xiàn zì jǐ zài tiān táng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FRUSTRATION" AND c.name = "content.FRUSTRATION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FRUSTRATION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITHFULNESS" AND child.name = "thought.FRUSTRATION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITHFULNESS->FRUSTRATION"}]->(child);
```
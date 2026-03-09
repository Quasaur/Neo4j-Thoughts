---
type: THOUGHT
name: "thought.NO MATCH"
alias: "Thought: No Match"
parent: "topic.BEAUTY"
en_content: |
  # Thought: NO MATCH
  [!Thought-en]
  The Most Beautiful Person on Earth is NO MATCH for the Ugliest Person in Heaven.
  
  [!Pensamiento-es]
  La persona más bella de la Tierra NO ES RIVAL para la persona más fea del cielo.
  
  [!Pensée-fr]
  La personne la plus belle sur Terre n’est PAS à la hauteur de la personne la plus laide du ciel.
  
  [!सोचा-hi]
  पृथ्वी पर सबसे सुन्दर व्यक्ति का स्वर्ग के सबसे कुरूप व्यक्ति से कोई मुकाबला नहीं है।
  
  [!思考-zh]
  世上最美丽的人也比不上天堂里最丑陋的人。
tags: ["evolution", "science", "religion", "evidence", "faith"]
ptopic: "[[topic-BEAUTY]]"
level: 5
neo4j: true
verified: false
---
```Cypher
CREATE (t:THOUGHT {
    name: "thought.NO MATCH",
    alias: "Thought: No Match",
    parent: "topic.BEAUTY",
    tags: ["evolution", "science", "religion", "evidence", "faith"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.NO MATCH",
    ctype: "THOUGHT",
    en_title: "No Match",
    en_content: "# Thought: NO MATCH
[!Thought-en]
The Most Beautiful Person on Earth is NO MATCH for the Ugliest Person in Heaven.

[!Pensamiento-es]
La persona más bella de la Tierra NO ES RIVAL para la persona más fea del cielo.

[!Pensée-fr]
La personne la plus belle sur Terre n’est PAS à la hauteur de la personne la plus laide du ciel.

[!सोचा-hi]
पृथ्वी पर सबसे सुन्दर व्यक्ति का स्वर्ग के सबसे कुरूप व्यक्ति से कोई मुकाबला नहीं है।

[!思考-zh]
世上最美丽的人也比不上天堂里最丑陋的人。",
    es_title: "NO HAY PARTIDO",
    es_content: "#Pensamiento: NO PARTIDO
[!Pensamiento-es]
La persona más bella de la Tierra NO ES COMPATIBLE con la persona más fea del cielo.

[!Pensamiento-es]
La persona más bella de la Tierra NO ES RIVAL para la persona más fea del cielo.

[!Pensée-fr]
Es el lugar perfecto para alojarse en Terre n'est Paris.

[!सोचा-hola]
पृथ्वी पर सबसे सुन्दर व्यक्ति क स्वर्ग के सबसे कुरूप व्यक्ति से कोई मुकबल नहीं है।

[!Piensa-zh]
La persona más bella del mundo no es tan buena como la persona más fea del cielo.",
    fr_title: "PAS DE CORRESPONDANCE",
    fr_content: "#Pensée : AUCUNE CORRESPONDANCE
[!Pensée-fr]
La plus belle personne sur Terre n’est PAS à la hauteur de la personne la plus laide du ciel.

[!Pensamiento-es]
La personne la plus belle de la Terre NO ES RIVAL pour la personne la plus belle du ciel.

[!Pensée-fr]
C’est l’endroit idéal pour séjourner à Terre n’est Paris.

[!सोचा-salut]
पृथ्वी पर सबसे सुन्दर व्यक्ति क स्वर्ग के सबसे कुरूप व्यक्ति से कोई मुकबल नहीं है।

[!Think-zh]
La personne la plus belle du monde n’est pas aussi bonne que la personne la plus laide du ciel.",
    hi_title: "कोई मेल नहीं",
    hi_content: "#सोचा: कोई मुकाबला नहीं
[!विचार-एन]
पृथ्वी पर सबसे सुंदर व्यक्ति का स्वर्ग के सबसे बदसूरत व्यक्ति से कोई मुकाबला नहीं है।

[!पेन्सामिएंटो-एस]
टिएरा के व्यक्तित्व का कोई प्रतिद्वंद्वी नहीं है, लेकिन उसके व्यक्तित्व का कोई प्रतिद्वंद्विता नहीं है।

[!पेन्सी-fr]
टेरे नेस्ट पेरिस में रहने के लिए यह एक आदर्श स्थान है।

[!सोचा-हाय]
पृथ्वी पर सबसे सुंदर व्यक्ति का स्वर्ग के सबसे कुरूप व्यक्ति से कोई मुकाबला नहीं है।

[!सोचें-zh]
दुनिया का सबसे सुंदर व्यक्ति स्वर्ग के सबसे बदसूरत व्यक्ति जितना अच्छा नहीं है।",
    zh_title: "bù pǐ pèi",
    zh_content: "# Thought: NO MATCH
[!Thought-en]
The Most Beautiful Person on Earth is NO MATCH for the Ugliest Person in Heaven.

[!Pensamiento-es]
La persona más bella de la Tierra NO ES RIVAL para la persona más fea del cielo.

[!Pensée-fr]
La personne la plus belle sur Terre n’est PAS à la hauteur de la personne la plus laide du ciel.

[!सोचा-hi]
पृथ्वी पर सबसे सुन्दर व्यक्ति का स्वर्ग के सबसे कुरूप व्यक्ति से कोई मुकाबला नहीं है।

[! sī kǎo -zh]
 shì shàng zuì měi lì de rén yě bǐ bù shàng tiān táng lǐ zuì chǒu lòu de rén 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NO MATCH" AND c.name = "content.NO MATCH"
MERGE (t)-[:HAS_CONTENT {name: "edge.NO MATCH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.NO MATCH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.BEAUTY->NO MATCH"}]->(child);
```

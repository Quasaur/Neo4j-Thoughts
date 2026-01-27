---
name: "passage.THE SOURCE OF WISDOM"
alias: "Passage: THE SOURCE OF WISDOM"
type: PASSAGE
parent: "topic.WISDOM"
en_content: "For the Lord gives wisdom;
From His mouth come knowledge and understanding.
He stores up sound wisdom for the upright;
He is a shield to those who walk in integrity,
Guarding the paths of justice,
And He watches over the way of His godly ones."
tags:
  - wisdom
  - gift
  - knowledge
  - understanding
  - integrity
neo4j: false
ptopic: "[[topic-WISDOM]]"
level: 3
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (b:PASSAGE
    {
     name: "passage.THE SOURCE OF WISDOM",
     alias: "Passage: THE SOURCE OF WISDOM", 
     parent: "topic.WISDOM", 
     tags: ["wisdom", "gift", "knowledge", "understanding", "integrity"], 
     source: "Proverbs 2:6-8",
     sortedsource: "Proverbs 02:06-08",
     biblelink: "(https://www.biblegateway.com/passage/?search=Deuteronomy%208%3A18&version=NASB)",
     level: 2});
// create multi-lingual content  
CREATE (c:CONTENT {
 name: "content.THE SOURCE OF WISDOM", 
 en_title: "The Source of Wisdom", 
 en_content: "For the Lord gives wisdom;
From His mouth come knowledge and understanding.
He stores up sound wisdom for the upright;
He is a shield to those who walk in integrity,
Guarding the paths of justice,
And He watches over the way of His godly ones.", 
 es_title: "La fuente de la sabiduría", 
 es_content: "Porque el Señor da la sabiduría;
De su boca provienen el conocimiento y el entendimiento.
Él atesora la sana sabiduría para los justos;
Es escudo para quienes andan con integridad,
Protegiendo los caminos de la justicia,
Y vela por el camino de sus fieles.", 
 fr_title: "La source de la sagesse", 
 fr_content: "Car l'Éternel donne la sagesse ;
De sa bouche proviennent la connaissance et l'intelligence.
Il réserve une sagesse précieuse aux hommes droits ;
Il est un bouclier pour ceux qui marchent dans l'intégrité,
Protégeant les sentiers de la justice,
Et il veille sur la voie de ses fidèles.", 
 hi_title: "बुद्धि का स्रोत",
 hi_content: "क्योंकि प्रभु ही बुद्धि देते हैं;
उनके मुख से ज्ञान और समझ निकलती है।
वह सीधे लोगों के लिए सच्ची बुद्धि जमा करके रखते हैं;
जो लोग ईमानदारी से चलते हैं, वह उनके लिए ढाल हैं,
न्याय के रास्तों की रक्षा करते हैं,
और वह अपने पवित्र लोगों के रास्ते की निगरानी करते हैं।",
 zh_title: "Zhìhuì de yuánquán", 
 zh_content: "yīnwèi yēhéhuá cìyǔ zhìhuì;
zhīshì hé wùxìng dōu chūzì tā de kǒu.
Tā wèi zhèngzhí rén jīcún zhēn zhìhuì;
tā zuò xíngwéi zhèngzhí zhī rén de dùnpái,
shǒuhù zhèngyì de dàolù,
tā yě kàngù jìngqián zhī rén de dàolù."});
// link content to node
MATCH (b:PASSAGE)
MATCH (c:CONTENT)
WHERE b.name = "passage.THE SOURCE OF WISDOM" AND c.name = "content.THE SOURCE OF WISDOM"
MERGE (b)-[:HAS_CONTENT {name: "p.edge.WISDOM->THE SOURCE OF WISDOM"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MATCH (child:PASSAGE {name: "passage.THE SOURCE OF WISDOM"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.WISDOM->THE SOURCE OF WISDOM"}]->(child)
RETURN *;

```

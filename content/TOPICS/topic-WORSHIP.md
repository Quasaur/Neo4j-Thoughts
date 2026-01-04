---
name: topic.WORSHIP
alias: "Topic: Obeisance"
type: TOPIC
parent: topic.CREATION
tags:
- worship
- devotion
- humility
- adoration
- reverence
neo4j: true
level: 3
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC {
	    name: "topic.WORSHIP",
		alias: "Topic: Obeisance", 
		parent: "topic.CREATION", 
		tags: ["worship", "devotion", "humility", "adoration", "reverence"], 
		notes: "",
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.WORSHIP", 
	en_title: "WORSHIP", 
	en_content: "To honor or show reverence for as The Divine Being; to regard with great or extravagant respect, honor, or devotion; to perform or take part in worship or an act of worship (i.e., falling on one's knees or face in humility and obeisance).", 
	es_title: "Adoración", 
	es_content: "Honrar o mostrar reverencia a un Ser Divino; considerarlo con gran o extravagante respeto, honor o devoción; realizar o participar en un culto o un acto de adoración (es decir, caer de rodillas o sobre el rostro en señal de humildad y reverencia).", 
	fr_title: "Adoration", 
	fr_content: "Honorer ou témoigner de la révérence envers l'Être Divin ; considérer avec un respect, un honneur ou une dévotion grands ou extravagants ; accomplir ou prendre part à un culte ou à un acte d'adoration (c'est-à-dire tomber à genoux ou face contre terre en signe d'humilité et d'obéissance).", 
	hi_title: "पूजा", 
	hi_content: "ईश्वरीय सत्ता के रूप में सम्मान या श्रद्धा प्रकट करना; अत्यधिक या असाधारण सम्मान, आदर या भक्ति के साथ सम्मान करना; पूजा या पूजा के किसी कार्य में भाग लेना या करना (अर्थात, विनम्रता और प्रणाम में घुटनों या चेहरे के बल गिरना)।", 
	zh_title: "Chóngbài", 
	zh_content: "zūnchóng huò chóngjìng shénmíng; yǐ jí dà de huò guòfèn de jìngyì, róngyù huò qiánchéng duìdài; jìnxíng huò cānyù chóngbài huò chóngbài xíngwéi (jí guì xià huò fǔfú zài dì, biǎoshì qiānbēi hé jìngyì)."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.WORSHIP" AND d.name = "desc.WORSHIP"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.WORSHIP"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.CREATION" AND child.name = "topic.WORSHIP"
MERGE (parent)-[:HAS_CHILD {name: "edge.CREATION->WORSHIP"}]->(child)
RETURN *;

```

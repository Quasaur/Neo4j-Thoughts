---
name: topic.HOLINESS
alias: "Topic: God's Worth"
type: TOPIC
parent: "topic.THE GODHEAD"
tags:
- sacred
- sacrosanct
- godliness
- piety
- virtue
neo4j: true
ptopic: "[[topic-THE]]"
level: 2
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.HOLINESS",
		alias: "Topic: God's Worth", 
		parent: "topic.THE GODHEAD", 
		tags: ["sacred", "sacrosanct", "godliness", "piety", "virtue"], 
		notes: "",
		level: 2});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.HOLINESS", 
	en_title: "HOLINESS", 
	en_content: "The quality or state of being holy; a Being (God) Who is exalted and worthy of complete devotion as One perfect in goodness and righteousness; a human devoted entirely to the Deity or the Work of the Deity; having a Divine quality; that object which is venerated as sacred.", 
	es_title: "SANTIDAD", 
	es_content: "La cualidad o estado de ser santo; un Ser (Dios) que es exaltado y digno de completa devoción como Uno perfecto en bondad y rectitud; un ser humano dedicado enteramente a la Deidad o a la Obra de la Deidad; que tiene una cualidad Divina; aquel objeto que se venera como sagrado.", 
	fr_title: "SAINTETÉ", 
	fr_content: "Qualité ou état de sainteté ; un Être (Dieu) exalté et digne d'une dévotion complète, parfait en bonté et en droiture ; un être humain entièrement dévoué à la Déité ou à l'Œuvre de la Déité ; possédant une qualité divine ; cet objet vénéré comme sacré.", 
	hi_title: "पवित्रता", 
	hi_content: "पवित्र होने का गुण या अवस्था; एक ऐसा प्राणी (ईश्वर) जो उत्तम है और जो अच्छाई और धार्मिकता में परिपूर्ण होने के कारण पूर्ण भक्ति का पात्र है; एक ऐसा मनुष्य जो पूरी तरह से देवता या देवता के कार्य के प्रति समर्पित है; जिसमें दिव्य गुण है; वह वस्तु जिसे पवित्र मानकर पूजा जाता है।", 
	zh_title: "Shèngjié", 
	zh_content: "shèngjié de pǐnzhí huò zhuàngtài; bèi zūnchóng de cúnzài (shén), shì wánquán shànliáng hé zhèngyì de cúnzài, zhídé wánquán de fèngxiàn; wánquán xiànshēn yú shén huò shén zhī gōngzuò de rénlèi; jùyǒu shénshèng de pǐnzhí; bèi zūnchóng wèi shénshèng de wùtǐ."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.HOLINESS" AND d.name = "desc.HOLINESS"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.Holiness"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.HOLINESS"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->HOLINESS"}]->(child)
RETURN *;

```

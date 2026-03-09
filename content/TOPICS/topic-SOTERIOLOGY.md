---
type: TOPIC
name: "topic.SOTERIOLOGY"
alias: "Topic: God's Redemptive Plan"
parent: "topic.THE GOSPEL"
en_content: "The branch of theology that studies the nature, purpose, and process of salvation—how it is achieved, how it is applied to humanity, and how it ultimately transforms both people and creation."
tags: ["salvation", "redemption", "atonement", "grace", "restoration"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 3
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.SOTERIOLOGY",
		alias: "Topic: God's Redemptive Plan", 
		parent: "topic.THE GOSPEL", 
		tags: ["salvation", "redemption", "atonement", "grace", "restoration"],
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.SOTERIOLOGY", 
	en_title: "Topic: God's Redemptive Plan", 
	en_content: "The branch of theology that studies the nature, purpose, and process of salvation—how it is achieved, how it is applied to humanity, and how it ultimately transforms both people and creation.", 
	es_title: "Tema: El plan redentor de Dios", 
	es_content: "La rama de la teología que estudia la naturaleza, el propósito y el proceso de la salvación: cómo se logra, cómo se aplica a la humanidad y cómo, en última instancia, transforma tanto a las personas como a la creación.", 
	fr_title: "Sujet : Le plan rédempteur de Dieu", 
	fr_content: "La branche de la théologie qui étudie la nature, le but et le processus du salut – comment il est accompli, comment il est appliqué à l'humanité et comment il transforme finalement les êtres humains et la création.", 
	hi_title: "विषय: ईश्वर की मुक्ति योजना", 
	hi_content: "धर्मशास्त्र की वह शाखा जो मुक्ति की प्रकृति, उद्देश्य और प्रक्रिया का अध्ययन करती है - यह कैसे प्राप्त होती है, इसे मानवता पर कैसे लागू किया जाता है, और यह अंततः लोगों और सृष्टि दोनों को कैसे बदल देती है।", 
	zh_title: "zhǔ tí : shén de jiù shú jì huà", 
	zh_content: "shénxué de yīgè fēnzhī, yánjiū jiùshú de běnzhí, mùdì hé guòchéng——jiùshú shì rúhé shíxiàn de, rúhé yìngyòng yú rénlèi, yǐjí tā zuìzhōng rúhé gǎibiàn rénlèi hé zhěnggè chuàngzào jiè."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.SOTERIOLOGY" AND d.name = "desc.SOTERIOLOGY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.SOTERIOLOGY"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GOSPEL" AND child.name = "topic.SOTERIOLOGY"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GOSPEL->SOTERIOLOGY"}]->(child);

```

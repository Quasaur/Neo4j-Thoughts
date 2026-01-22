---
name: "topic.HEALTH SCIENCES"
alias: "Topic: The Science of Human Health"
type: TOPIC
parent: topic.COSMOLOGY
en_content: "The interdisciplinary field that studies the human body, health, disease, and healthcare systems in order to prevent illness, improve well‑being, and deliver effective clinical and public‑health interventions."
tags:
- wellness
- disease
- care
- public_health
- interdisciplinary
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 5
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.HEALTH SCIENCES",
		alias: "Topic: The Science of Human Health", 
		parent: "topic.COSMOLOGY", 
		tags: ["wellness", "disease", "care", "public_health", "interdisciplinary"], 
		level: 5});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.HEALTH SCIENCES", 
	en_title: "Health Sciences", 
	en_content: "The interdisciplinary field that studies the human body, health, disease, and healthcare systems in order to prevent illness, improve well‑being, and deliver effective clinical and public‑health interventions.", 
	es_title: "Ciencias de la Salud",
	es_content: "Campo interdisciplinario que estudia el cuerpo humano, la salud, las enfermedades y los sistemas de atención médica con el fin de prevenir enfermedades, mejorar el bienestar y brindar intervenciones clínicas y de salud pública efectivas.", 
	fr_title: "Sciences de la santé", 
	fr_content: "Ce domaine interdisciplinaire étudie le corps humain, la santé, les maladies et les systèmes de santé afin de prévenir les maladies, d'améliorer le bien-être et de mettre en œuvre des interventions cliniques et de santé publique efficaces.", 
	hi_title: "स्वास्थ्य विज्ञान", 
	hi_content: "यह एक इंटरडिसिप्लिनरी फील्ड है जो बीमारी को रोकने, सेहत को बेहतर बनाने और असरदार क्लिनिकल और पब्लिक हेल्थ इंटरवेंशन देने के लिए इंसानी शरीर, स्वास्थ्य, बीमारी और हेल्थकेयर सिस्टम का अध्ययन करती है।", 
	zh_title: "Jiànkāng kēxué", 
	zh_content: "zhè shì yīgè kuà xuékē lǐngyù, yánjiū réntǐ, jiànkāng, jíbìng hé yīliáo bǎojiàn xìtǒng, zhǐ zài yùfáng jíbìng, gǎishàn jiànkāng zhuàngkuàng, bìng tígōng yǒuxiào de línchuáng hé gōnggòng wèishēng gānyù cuòshī."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.HEALTH SCIENCES" AND d.name = "desc.HEALTH SCIENCES"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.HEALTH SCIENCES"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "topic.HEALTH SCIENCES"
MERGE (parent)-[:HAS_CHILD {name: "edge.COSMOLOGY->HEALTH SCIENCES"}]->(child)
RETURN *;

```

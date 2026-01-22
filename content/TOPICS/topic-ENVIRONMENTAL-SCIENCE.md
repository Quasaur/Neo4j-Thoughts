---
name: "topic.ENVIRONMENTAL SCIENCE"
alias: "Topic: Earth's Natural Processes"
type: TOPIC
parent: "topic.NATURAL SCIENCES"
en_content: "The branch of the Natural Sciences that studies how the solid Earth, its water, its air, and its living organisms interact, and how these interconnected systems change over time."
tags:
- ecosystem
- resources
- climate
- cycle
- change
neo4j: true
ptopic: "[[topic-NATURAL-SCIENCES]]"
level: 6
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.ENVIRONMENTAL SCIENCE",
		alias: "Topic: Earth's Natural Processes", 
		parent: "topic.NATURAL SCIENCES", 
		tags: ["ecosystem", "resources", "climate", "cycle", "change"], 
		level: 6});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.ENVIRONMENTAL SCIENCE", 
	en_title: "Environmental Science", 
	en_content: "The branch of the Natural Sciences that studies how the solid Earth, its water, its air, and its living organisms interact, and how these interconnected systems change over time.", 
	es_title: "Ciencias Ambientales",
	es_content: "Rama de las Ciencias Naturales que estudia cómo interactúan la Tierra sólida, el agua, el aire y los organismos vivos, y cómo cambian estos sistemas interconectados con el tiempo.", 
	fr_title: "Sciences de l'environnement", 
	fr_content: "Branche des sciences naturelles qui étudie les interactions entre la Terre solide, son eau, son air et ses organismes vivants, et la manière dont ces systèmes interconnectés évoluent au fil du temps.", 
	hi_title: "पर्यावरण विज्ञान", 
	hi_content: "प्राकृतिक विज्ञान की वह शाखा जो यह अध्ययन करती है कि ठोस पृथ्वी, उसका पानी, उसकी हवा और उसके जीवित जीव कैसे एक-दूसरे से इंटरैक्ट करते हैं, और ये आपस में जुड़े सिस्टम समय के साथ कैसे बदलते हैं।", 
	zh_title: "Huánjìng kēxué", 
	zh_content: "zìrán kēxué de yīgè fēnzhī, yánjiū dìqiú de gùtǐ bùfèn, shuǐ, kōngqì jí qí shēngwù tǐ rúhé xiānghù zuòyòng, yǐjí zhèxiē xiānghù guānlián de xìtǒng rúhé suí shíjiān biànhuà."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.ENVIRONMENTAL SCIENCE" AND d.name = "desc.ENVIRONMENTAL SCIENCE"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ENVIRONMENTAL SCIENCE"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.NATURAL SCIENCES" AND child.name = "topic.ENVIRONMENTAL SCIENCE"
MERGE (parent)-[:HAS_CHILD {name: "edge.NATURAL SCIENCES->ENVIRONMENTAL SCIENCE"}]->(child)
RETURN *;

```

---
name: "topic.PHYSICS"
alias: "Topic: Physical Properties of Matter"
type: TOPIC
parent: "topic.NATURAL SCIENCES"
en_content: "The physical properties and composition of matter."
tags:
- matter
- energy
- force
- motion
- law
neo4j: true
ptopic: "[[topic-NATURAL-SCIENCES]]"
level: 6
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.PHYSICS",
		alias: "Topic: Physical Properties of Matter", 
		parent: "topic.NATURAL SCIENCES", 
		tags: ["matter", "energy", "force", "motion", "law"], 
		level: 6});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.PHYSICS", 
	en_title: "Physics", 
	en_content: "The physical properties and composition of matter.", 
	es_title: "Física",
	es_content: "Las propiedades físicas y la composición de la materia.", 
	fr_title: "Physique", 
	fr_content: "Les propriétés physiques et la composition de la matière.", 
	hi_title: "भौतिकी", 
	hi_content: "पदार्थ के भौतिक गुण और संरचना।", 
	zh_title: "Wùlǐ xué", 
	zh_content: "wùzhí de wùlǐ xìngzhì hé zǔchéng."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.PHYSICS" AND d.name = "desc.PHYSICS"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.PHYSICS"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.NATURAL SCIENCES" AND child.name = "topic.PHYSICS"
MERGE (parent)-[:HAS_CHILD {name: "edge.NATURAL SCIENCES->PHYSICS"}]->(child)
RETURN *;

```

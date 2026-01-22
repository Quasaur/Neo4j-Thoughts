---
name: "topic.NATURAL SCIENCES"
alias: "Topic: Matter & Energy"
type: TOPIC
parent: topic.COSMOLOGY
en_content: "Any of the sciences (such as physics, chemistry, or biology) that deal with matter, energy, and their interrelations and transformations or with objectively-measurable phenomena."
tags:
- matter
- astrophysics
- physics
- chemistry
- biology
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 5
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.NATURAL SCIENCES",
		alias: "Topic: Matter & Energy", 
		parent: "topic.COSMOLOGY", 
		tags: ["matter", "astrophysics", "physics", "chemistry", "biology
		"], 
		level: 5});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.NATURAL SCIENCES", 
	en_title: "Natural Sciences", 
	en_content: "Any of the sciences (such as physics, chemistry, or biology) that deal with matter, energy, and their interrelations and transformations or with objectively measurable phenomena.", 
	es_title: "Las ciencias naturales",
	es_content: "Cualquiera de las ciencias (como la física, la química o la biología) que se ocupan de la materia, la energía y sus interrelaciones y transformaciones, o de fenómenos objetivamente medibles.", 
	fr_title: "Les sciences naturelles", 
	fr_content: "Toute science (comme la physique, la chimie ou la biologie) qui traite de la matière, de l'énergie et de leurs interrelations et transformations, ou de phénomènes objectivement mesurables.", 
	hi_title: "प्राकृतिक विज्ञान", 
	hi_content: "कोई भी विज्ञान (जैसे भौतिकी, रसायन विज्ञान, या जीव विज्ञान) जो पदार्थ, ऊर्जा, और उनके आपसी संबंधों और बदलावों या वस्तुनिष्ठ रूप से मापने योग्य घटनाओं से संबंधित है।", 
	zh_title: "Zìrán kēxué", 
	zh_content: "zhǐ yánjiū wùzhí, néngliàng jí qí xiānghù guānxì hé zhuǎnhuà, huò yánjiū kèguān kě cèliáng xiànxiàng de rènhé kēxué (lìrú wùlǐ xué, huàxué huò shēngwù xué)."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.NATURAL SCIENCES" AND d.name = "desc.NATURAL SCIENCES"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.NATURAL SCIENCES"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "topic.NATURAL SCIENCES"
MERGE (parent)-[:HAS_CHILD {name: "edge.COSMOLOGY->NATURAL SCIENCES"}]->(child)
RETURN *;

```

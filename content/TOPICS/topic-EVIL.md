---
name: topic.EVIL
alias: "Topic: Malevolence"
type: TOPIC
parent: topic.MORALITY
tags:
- entitled
- privilege
- flesh
- pride
- right
neo4j: true
ptopic: "[[topic-MORALITY]]"
level: 4
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.EVIL",
		alias: "Topic: Malevolence", 
		parent: "topic.MORALITY", 
		tags: ["entitled", "privilege", "flesh", "pride", "right"], 
		notes: "",
		level: 4});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.EVIL", 
	en_title: "EVIL", 
	en_content: "The fact of suffering, misfortune, and wrongdoing; a cosmic wicked force; something or someone that brings sorrow, distress, or calamity; one that steals, kills and destroys; that angelic being which is the fountain of pride (Lucifer, Satan, the Devil)", 
	es_title: "Maldad", 
	es_content: "El hecho del sufrimiento, la desgracia y la maldad; una fuerza cósmica malvada; algo o alguien que trae tristeza, angustia o calamidad; alguien que roba, mata y destruye; ese ser angelical que es la fuente del orgullo (Lucifer, Satanás, el Diablo).", 
	fr_title: "Mal", 
	fr_content: "Le fait de souffrir, d'être malheureux ou de faire le mal ; une force cosmique maléfique ; quelque chose ou quelqu'un qui apporte chagrin, détresse ou calamité ; quelqu'un qui vole, tue et détruit ; cet être angélique source d'orgueil (Lucifer, Satan, le Diable).", 
	hi_title: "बुराई", 
	hi_content: "दुख, दुर्भाग्य और गलत कामों का तथ्य; एक ब्रह्मांडीय दुष्ट शक्ति; कोई चीज़ या व्यक्ति जो दुःख, संकट या विपत्ति लाता है; वह जो चोरी करता है, मारता है और नष्ट करता है; वह देवदूत जो घमंड का स्रोत है (लूसिफ़र, शैतान, शैतान)", 
	zh_title: "Xié'è", 
	zh_content: "zhǐ kǔnàn, bùxìng hé bùfǎ xíngwéi; yǔzhòu xié'è lìliàng; dài lái bēishāng, tòngkǔ huò zāinàn de shìwù huò rén; tōuqiè, shālù hé pòhuài zhě; jiāo'ào zhī yuán de tiānshǐ (lù xīfǎ, sādàn, móguǐ)"});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.MORALITY' AND d.name = 'desc.EVIL'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.EVIL"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = 'topic.MORALITY' AND child.name = 'topic.EVIL'
MERGE (parent)-[:HAS_CHILD {name: "edge.MORALITY->EVIL"}]->(child)
RETURN *;

```

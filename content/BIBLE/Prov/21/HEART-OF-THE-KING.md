---
name: "passage.HEART OF THE KING"
alias: "Passage: The Son of Heaven"
type: PASSAGE
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- heart
- king
- divine_sovereignty
- water_streams
- free_will
neo4j: true
ptopic: "[[topic-DIVINE]]"
level: 2
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (b:PASSAGE
    {
	    name: "passage.HEART OF THE KING",
		alias: "Passage: The Son of Heaven", 
		parent: "topic.DIVINE SOVEREIGNTY", 
		tags: ["heart", "king", "divine_)soereignty", "water_streams", "free_will"], 
		source: "Proverbs 21:1",
		sortedsource: "Proverbs 21:01",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+21%3A1&version=NASB",
		notes: "",
		level: 2});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.HEART OF THE KING", 
	en_title: "HEART OF THE KING", 
	en_content: "The king’s heart is like channels of water in the Hand of the LORD; He turns it wherever He pleases.", 
	es_title: "CORAZÓN DEL REY", 
	es_content: "El corazón del rey es como canales de agua en la mano del Señor; Él lo inclina a donde quiere.", 
	fr_title: "LE CŒUR DU ROI", 
	fr_content: "Le cœur du roi est comme un courant d’eau dans la main de l’Éternel ; il le dirige où il veut.", 
	hi_title: "राजा का हृदय", 
	hi_content: "राजा का हृदय यहोवा के हाथ में जल की नालियों के समान है; वह उसे जिधर चाहता है उधर मोड़ देता है।", 
	zh_title: "Wáng de xīn", 
	zh_content: "wáng de xīn zài yēhéhuá shǒuzhōng hǎoxiàng gōuqú de shuǐ, tā kěyǐ suíyì liúzhuàn."});
// link content to node
MATCH (b:PASSAGE)
MATCH (c:CONTENT)
WHERE b.name = "passage.HEART OF THE KING" AND c.name = "content.HEART OF THE KING"
MERGE (b)-[:HAS_CONTENT {name: "b.edge.HEART OF THE KING"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:PASSAGE {name: "passage.HEART OF THE KING"})
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.THE GODHEAD->HEART OF THE KING"}]->(child)
RETURN *;

```

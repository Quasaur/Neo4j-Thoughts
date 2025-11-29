```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.CREATION",
		alias: "Topic: The Universe / Multiverse", 
		parent: "topic.THE GODHEAD", 
		tags: ["creatiion", "cosmos", "universe", "dominion", "kingdom"], 
		notes: "",
		level: 2});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.CREATION", 
	en_title: "CREATION", 
	en_content: "All beings, places and things that exist apart from The GODHEAD as a result of Divine Creation.", 
	es_title: "CREACIÓN", 
	es_content: "Todos los seres, lugares y cosas que existen aparte de La DEIDAD como resultado de la Creación Divina.", 
	fr_title: "CRÉATION", 
	fr_content: "Tous les êtres, lieux et choses qui existent en dehors de la DIVINITÉ, résultat de la Création Divine.", 
	hi_title: "सृष्टि", 
	hi_content: "ईश्वर के बाहर मौजूद सभी प्राणी, स्थान और चीज़ें ईश्वरीय सृष्टि का परिणाम हैं।", 
	zh_title: "hén xìng", 
	zh_content: "shén de cúnzài shì sānwèiyītǐ de."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.CREATION" AND d.name = "desc.CREATION"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.Creation"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.CREATION"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->CREATION"}]->(child)
RETURN *;

```
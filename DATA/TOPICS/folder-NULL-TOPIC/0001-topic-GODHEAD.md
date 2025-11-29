```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.THE GODHEAD",
		alias: "Topic: The GODHEAD", 
		parent: "NULL TOPIC", 
		tags: ["starting point", "level_one", "alpha", "omega", "the_one"], 
		notes: "NOTE: Implement multi-level topics; THE-GODHEAD being the only topic level 1.",
		level: 1});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.The GODHEAD", 
	en_title: "THE GODHEAD", 
	en_content: "The Being of God as existing in Three Persons.", 
	es_title: "La DEIDAD", 
	es_content: "El Ser de Dios existiendo en Tres Personas.", 
	fr_title: "La DIVINITÉ", 
	fr_content: "L'Être de Dieu existant en trois personnes.", 
	hi_title: "ईश्वरत्व", 
	hi_content: "ईश्वर का अस्तित्व तीन व्यक्तियों में विद्यमान है।", 
	zh_title: "Shén xìng", 
	zh_content: "shén de cúnzài shì sānwèiyītǐ de."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.THE GODHEAD" AND d.name = "desc.The GODHEAD"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.The GODHEAD"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "NULL TOPIC" AND child.name = "topic.THE GODHEAD"
MERGE (parent)-[:HAS_CHILD {name: "edge.NULL->THE GODHEAD"}]->(child)
RETURN *;

```
```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.THE HOLY SPIRIT",
		alias: "Thought: The Most High", 
		parent: "topic.THE GODHEAD", 
		tags: ["holy_spirit", "deity", "god", "fullness", "filling"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.THE HOLY SPIRIT", 
	en_title: "THE HOLY SPIRIT", 
	en_content: "The Holy Spirit is God, and all men must be filled with Him.", 
	es_title: "EL ESPÍRITU SANTO", 
	es_content: "El Espíritu Santo es Dios, y todos los hombres deben estar llenos de Él.", 
	fr_title: "LE SAINT-ESPRIT", 
	fr_content: "Le Saint-Esprit est Dieu, et tous les hommes doivent être remplis de Lui.", 
	hi_title: "पवित्र आत्मा", 
	hi_content: "पवित्र आत्मा ईश्वर है, और सभी मनुष्यों को उससे भरा होना चाहिए।", 
	zh_title: "Shènglíng", 
	zh_content: "shènglíng shì shén, suǒyǒu de rén dōu bìxū bèi tā chōngmǎn."});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE HOLY SPIRIT" AND c.name = "content.THE HOLY SPIRIT"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE HOLY SPIRIT"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.THE HOLY SPIRIT"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->THE HOLY SPIRIT"}]->(child)
RETURN *;

```
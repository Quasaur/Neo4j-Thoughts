```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.HUMANITY",
		alias: "Topic: Mankind", 
		parent: "topic.CREATION", 
		tags: ["adam", "huans", "mankind", "homosapiens", "likeness_of_god
		"], 
		notes: "",
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.HUMANITY", 
	en_title: "HUMANITY", 
	en_content: "Mankind, male and female, created in the Image and Likeness of The GODHEAD.", 
	es_title: "HUMANIDAD", 
	es_content: "La humanidad, hombre y mujer, creados a Imagen y Semejanza de la DEIDAD.", 
	fr_title: "L'HUMANITÉ", 
	fr_content: "L'humanité, homme et femme, a été créée à l'image et à la ressemblance de la DIVINITÉ.", 
	hi_title: "मानवता", 
	hi_content: "मानव जाति, नर और मादा, ईश्वर की छवि और समानता में बनाई गई है।", 
	zh_title: "Rénlèi", 
	zh_content: "rénlèi, wúlùn nánnǚ, dōu shì ànzhào shén de xíngxiàng hé yàngshì bèi chuàngzào de."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.HUMANITY" AND d.name = "desc.HUMANITY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.HUMANITY"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.CREATION" AND child.name = "topic.HUMANITY"
MERGE (parent)-[:HAS_CHILD {name: "edge.CREATION->HUMANITY"}]->(child)
RETURN *;

```
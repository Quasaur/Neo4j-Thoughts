```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.PROTECTION",
		alias: "Thought: Strong Tower", 
		parent: "topic.THE GODHEAD", 
		tags: ["holy_spirit", "spirit_of_truth", "standard", "defense", "jesus_christ"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.PROTECTION", 
	en_title: "PROTECTION", 
	en_content: "Without the Holy Spirit of Christ humanity has no defense against the Devil, those who rule the world or even our own lower natures.", 
	es_title: "PROTECCIÓN", 
	es_content: "Sin el Espíritu Santo de Cristo, la humanidad no tiene defensa contra el Diablo, contra aquellos que gobiernan el mundo o incluso contra nuestra propia naturaleza inferior.", 
	fr_title: "PROTECTION", 
	fr_content: "Sans le Saint-Esprit du Christ, l’humanité n’a aucune défense contre le Diable, contre ceux qui gouvernent le monde ou même contre notre propre nature inférieure.", 
	hi_title: "सुरक्षा", 
	hi_content: "मसीह की पवित्र आत्मा के बिना मानवता के पास शैतान, दुनिया पर शासन करने वालों या यहाँ तक कि हमारी अपनी निम्न प्रकृति के विरुद्ध कोई बचाव नहीं है।", 
	zh_title: "Bǎohù", 
	zh_content: "méiyǒu jīdū de shènglíng, rénlèi jiù wúfǎ dǐyù móguǐ, tǒngzhì shí jiè de rén, shènzhì wǒmen zìshēn de dījí běnxìng."});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PROTECTION" AND c.name = "content.PROTECTION"
MERGE (t)-[:HAS_CONTENT {name: "edge.PROTECTION"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.PROTECTION"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->PROTECTION"}]->(child)
RETURN *;

```
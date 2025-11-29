```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.MOTION",
		alias: "Thought: Movement", 
		parent: "topic.THE GODHEAD", 
		tags: ["rest", "sabbath", "peace", "contentment", "fullness"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.MOTION", 
	en_title: "MOTION", 
	en_content: "Everything that exists is MOVING…  
…except God. Even when He MOVES, God is at REST  
…GLORY!!!!!!!!!!!!!!!!!!!!", 
	es_title: "MOVIMIENTO", 
	es_content: "Todo lo que existe se mueve…
…excepto Dios. Incluso cuando se mueve, Dios está en reposo
…¡¡¡¡¡¡¡GLORIA!!!!!!!!!!!!!!!!!!!!", 
	fr_title: "MOUVEMENT", 
	fr_content: "Tout ce qui existe est en mouvement…
…sauf Dieu. Même lorsqu'il est en mouvement, Dieu est au repos.
…GLOIRE!!!!!!!!!!!!!!!!!!!!", 
	hi_title: "गति", 
	hi_content: "हर चीज़ जो अस्तित्व में है, गतिमान है…
सिवाय ईश्वर के। जब वह गति करता है, तब भी ईश्वर विश्राम में होता है
महिमा!!!!!!!!!!!!!!!!!!!!!", 
	zh_title: "Yùndòng", 
	zh_content: "yīqiè cúnzài de shìwù dōu zài yùndòng……
……chúle shàngdì. Jíshǐ tā yùndòng, shàngdì yě chǔyú jìngzhǐ zhuàngtài
……róngyào!!!!!!!!!!!!!"});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MOTION" AND c.name = "content.MOTION"
MERGE (t)-[:HAS_CONTENT {name: "edge.MOTION"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MOTION"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->MOTION"}]->(child)
RETURN *;

```
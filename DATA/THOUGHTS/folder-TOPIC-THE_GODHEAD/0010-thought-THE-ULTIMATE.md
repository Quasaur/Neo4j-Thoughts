```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.THE ULTIMATE",
		alias: "Thought: The Living God", 
		parent: "topic.THE GODHEAD", 
		tags: ["humanity", "self_worship", "god", "judgement", "accountablr"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.THE ULTIMATE", 
	en_title: "THE ULTIMATE", 
	en_content: "That which is Ultimate cannot be Ultimate unless 'it' (He) is also PERSONAL.", 
	es_title: "LO ÚLTIMO", 
	es_content: "Lo que es Último no puede ser Último a menos que 'eso' (Él) sea también PERSONAL.", 
	fr_title: "L'ULTIME", 
	fr_content: "Ce qui est Ultime ne peut être Ultime que si « cela » (Il) est aussi PERSONNEL.", 
	hi_title: "परम", 
	hi_content: "जो परम है वह परम नहीं हो सकता जब तक कि 'वह' (वह) भी व्यक्तिगत न हो।", 
	zh_title: "Zhōngjí", 
	zh_content: "chúfēi 'tā'(tā) yě jùyǒu wèi gé xìng, fǒuzé zhōngjí zhī wù bù kěnéng shì zhōngjí."});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE ULTIMATE" AND c.name = "content.THE ULTIMATE"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE ULTIMATE"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.THE ULTIMATE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->THE ULTIMATE"}]->(child)
RETURN *;

```
```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.THE ULTIMATE (2)",
		alias: "Thought: The Beginning and The End", 
		parent: "topic.THE GODHEAD", 
		tags: ["deity", "wrath", "judgement", "grace", "acquittal"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.THE ULTIMATE (2)", 
	en_title: "THE ULTIMATE (2)", 
	en_content: "Every human that has ever lived will soon face either the Greatest Terror (God's Wrath) or the Greatest Pleasure (God's Grace).", 
	es_title: "LO MÁXIMO (2)", 
	es_content: "Todo ser humano que haya vivido alguna vez pronto se enfrentará al Mayor Terror (la Ira de Dios) o al Mayor Placer (la Gracia de Dios).", 
	fr_title: "L'ULTIME (2)", 
	fr_content: "Tout être humain ayant jamais vécu sera bientôt confronté soit à la plus grande terreur (la colère de Dieu), soit au plus grand plaisir (la grâce de Dieu).", 
	hi_title: "परम (2)", 
	hi_content: "हर इंसान जो कभी भी जीवित रहा है, उसे जल्द ही या तो सबसे बड़े आतंक (ईश्वर का क्रोध) या सबसे बड़ी खुशी (ईश्वर की कृपा) का सामना करना पड़ेगा।", 
	zh_title: "Zhōngjí (2)", 
	zh_content: "měi gè céngjīng huóguò de rén, hěn kuài dūhuì miànlín zuìdà de kǒngjù (shàngdì de fènnù) huò zuìdà de kuàilè (shàngdì de ēndiǎn)."});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE ULTIMATE (2)" AND c.name = "content.THE ULTIMATE (2)"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE ULTIMATE (2)"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.THE ULTIMATE (2)"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->THE ULTIMATE (2)"}]->(child)
RETURN *;

```
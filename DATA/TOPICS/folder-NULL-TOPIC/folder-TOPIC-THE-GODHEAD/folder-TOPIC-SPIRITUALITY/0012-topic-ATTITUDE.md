```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.ATTITUDE",
		alias: "Topic: Spiritual Disposition", 
		parent: "topic.SPIRITUALITY", 
		tags: ["mentality", "disposition", "feeling", "spirit", "fruit"], 
		notes: "",
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.ATTITUDE", 
	en_title: "ATTITUDE", 
	en_content: "A feeling, emotion or mental position to a fact or state.", 
	es_title: "Actitud", 
	es_content: "Un sentimiento, emoción o posición mental ante un hecho o estado.", 
	fr_title: "Attitude", 
	fr_content: "Un sentiment, une émotion ou une position mentale face à un fait ou à un état.", 
	hi_title: "दृष्टिकोण", 
	hi_content: "किसी तथ्य या स्थिति के प्रति एक भावना, भाव या मानसिक स्थिति।", 
	zh_title: "Tàidù", 
	zh_content: "duì mǒu yī shìshí huò zhuàngtài de gǎnjué, qíngxù huò xīnlǐ lìchǎng."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.ATTITUDE" AND d.name = "desc.ATTITUDE"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ATTITUDE"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "topic.ATTITUDE"
MERGE (parent)-[:HAS_CHILD {name: "edge.CREATION->ATTITUDE"}]->(child)
RETURN *;

```
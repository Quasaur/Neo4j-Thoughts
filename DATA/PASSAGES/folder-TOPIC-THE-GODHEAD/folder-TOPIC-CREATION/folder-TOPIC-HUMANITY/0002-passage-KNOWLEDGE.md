```Cypher
//create the Passage with the same fields as a normal thought
CREATE (b:PASSAGE
    {
	    name: "passage.KNOWLEDGE",
		alias: "Passage: God's Existence as the Foundation of Education", 
		parent: "topic.HUMANITY", 
		tags: ["fear_of_the_lord", "beginning", "knowledge", "fools", "instruction"], 
		source: "Proverbs 1:7",
		sortedsource: "Proverbs 01:07",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A7&version=NASB",
		notes: "",
		level: 2});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.KNOWLEDGE", 
	en_title: "KNOWLEDGE", 
	en_content: "The fear of the LORD is the beginning of knowledge; fools despise wisdom and instruction.", 
	es_title: "CONOCIMIENTO", 
	es_content: "El temor del SEÑOR es el principio del conocimiento; los necios desprecian la sabiduría y la instrucción.", 
	fr_title: "CONNAISSANCE", 
	fr_content: "La crainte de l’Éternel est le commencement de la science ; les insensés méprisent la sagesse et l’instruction.", 
	hi_title: "ज्ञान", 
	hi_content: "प्रभु का भय ज्ञान की शुरुआत है; मूर्ख लोग ज्ञान और शिक्षा को तुच्छ समझते हैं।", 
	zh_title: "Zhīshì", 
	zh_content: "jìngwèi yēhéhuá shì zhīshì de kāiduān; yúwàng rén miǎoshì zhìhuì hé xùnhuì."});
// link content to node
MATCH (b:PASSAGE)
MATCH (c:CONTENT)
WHERE b.name = "passage.KNOWLEDGE" AND c.name = "content.KNOWLEDGE"
MERGE (b)-[:HAS_CONTENT {name: "b.edge.KNOWLEDGE"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:PASSAGE)
WHERE parent.name = "topic.HUMANITY" AND child.name = "passage.KNOWLEDGE"
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.THE GODHEAD->KNOWLEDGE"}]->(child)
RETURN *;

```
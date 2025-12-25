```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.IMPERSONAL GOD",
		alias: "Thought: The Genie God", 
		parent: "topic.THE GODHEAD", 
		tags: ["personal", "impersonal", "self_aware", "god", "sentience"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.IMPERSONAL GOD", 
	en_title: "IMPERSONAL GOD", 
	en_content: "An impersonal god is not God at all; that is why the God of the Hebrews named Himself 'I AM'", 
	es_title: "DIOS IMPERSONAL", 
	es_content: "Un dios impersonal no es Dios en absoluto; por eso el Dios de los hebreos se llamó a sí mismo 'YO SOY'.", 
	fr_title: "DIEU IMPERSONNEL", 
	fr_content: "Un dieu impersonnel n'est pas Dieu du tout ; c'est pourquoi le Dieu des Hébreux s'appelait « JE SUIS ».", 
	hi_title: "अवैयक्तिक ईश्वर", 
	hi_content: "अवैयक्तिक ईश्वर बिल्कुल भी ईश्वर नहीं है; इसीलिए इब्रानियों के ईश्वर ने अपना नाम 'मैं हूँ' रखा।", 
	zh_title: "Fēi réngéhuà de shén", 
	zh_content: "fēi réngéhuà de shén gēnběn bùshì shén; zhè jiùshì wèishéme xī bó lái rén de shén zìchēng wèi 'wǒ shì'"});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IMPERSONAL GOD" AND c.name = "content.IMPERSONAL GOD"
MERGE (t)-[:HAS_CONTENT {name: "edge.IMPERSONAL GOD"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.IMPERSONAL GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->IMPERSONAL GOD"}]->(child)
RETURN *;

```
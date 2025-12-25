```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.EGO",
		alias: "Thought: The Greatness of God", 
		parent: "topic.THE GODHEAD", 
		tags: ["god", "sun", "earth", "myself", "humility"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.EGO", 
	en_title: "EGO", 
	en_content: "The Earth is 3.5 million times bigger than me...  
...the Sun is a million times bigger than the Earth...  
...that means the Sun is 176 SEPTILLION (176 followed by 24 zeros) times larger than myself...  
...GOD is great...I am pathetic.", 
	es_title: "YO MISMO", 
	es_content: "La Tierra es 3,5 millones de veces más grande que yo…
…el Sol es un millón de veces más grande que la Tierra…
…eso significa que el Sol es 176 SEPTILLONES (176 seguido de 24 ceros) de veces más grande que yo…
…DIOS es grande… soy patético.", 
	fr_title: "MOI-MÊME", 
	fr_content: "La Terre est 3,5 millions de fois plus grande que moi…
...le Soleil est un million de fois plus grand que la Terre…
...ce qui veut dire que le Soleil est 176 SEPTILLIONS (176 suivi de 24 zéros) fois plus grand que moi…
...DIEU est grand…Je suis pathétique.", 
	hi_title: "मैं खुद", 
	hi_content: "पृथ्वी मुझसे 3.5 मिलियन गुना बड़ी है...
सूर्य पृथ्वी से दस लाख गुना बड़ा है...
इसका मतलब है कि सूर्य मुझसे 176 सेप्टिलियन (176 के बाद 24 शून्य) गुना बड़ा है...
ईश्वर महान है...मैं दयनीय हूँ।", 
	zh_title: "Zìwǒ", 
	zh_content: "dìqiú bǐ wǒ dà 350 wàn bèi……
……tàiyáng bǐ dìqiú dà 100 wàn bèi……
……zhè yìwèizhe tàiyáng bǐ wǒ dà 176 de 7 cì fāng bèi (176 hòumiàn gēnzhe 24 gè líng)……
……shàngdì zhēn wěidà……wǒ zhēn kělián."});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EGO" AND c.name = "content.EGO"
MERGE (t)-[:HAS_CONTENT {name: "edge.EGO"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.EGO"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->EGO"}]->(child)
RETURN *;

```
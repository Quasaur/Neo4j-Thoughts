```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE
    {
	    name: "quote.GOD IS GOOD",
		alias: "Quote: The Goodness of God", 
		parent: "topic.THE GODHEAD", 
		tags: ["goodness", "divine", "god", "good", "great"], 
		source: "The Traveler's Oasis, Book One",
		booklink: "https://www.amazon.com/Travelers-Oasis-Book-One-ebook/dp/B00Y43B2OC",
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.GOD IS GOOD", 
	en_title: "GOD IS GOOD", 
	en_content: "All of the gravest injustices committed by humanity against its own would not even be remembered in the Presence of the Divine Goodness.", 
	es_title: "Dios es bueno.", 
	es_content: "Dios es tan bueno que la pesadez (de la palabra hebrea que significa 'grandeza') de su bondad supera con creces cualquier maldad que pudiera haber experimentado en cualquier momento.", 
	fr_title: "Dieu est bon.", 
	fr_content: "Dieu est si bon que la « lourdeur » (du mot hébreu qui signifie « grandeur ») de sa bonté dépasse de loin toute « méchanceté » que j’aurais pu éprouver pendant un certain temps.", 
	hi_title: "ईश्वर अच्छा है।", 
	hi_content: "मईश्वर इतना अच्छा है कि उसकी अच्छाई का 'भारीपन' ('महानता' के लिए हिब्रू शब्द से) किसी भी 'बुराई' से कहीं अधिक है जिसे मैंने कभी भी किसी भी समय के लिए अनुभव किया हो।", 
	zh_title: "Shàngdì shì réncí de.", 
	zh_content: "Shàngdì rúcǐ réncí, tā de réncí zhī 'zhòng'(xī bó lái yǔ zhòngyì wèi 'wěidà') yuǎn yuǎn chāoguòle wǒ chángqí yǐlái suǒ jīnglì de rènhé 'è'."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = "quote.GOD IS GOOD" AND c.name = "content.GOD IS GOOD"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.GOD IS GOOD"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "quote.GOD IS GOOD"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GODHEAD->GOD IS GOOD"}]->(child)
RETURN *;

```
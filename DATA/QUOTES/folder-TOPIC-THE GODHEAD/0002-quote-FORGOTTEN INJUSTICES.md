```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE
    {
	    name: "quote.FORGOTTEN INJUSTICES",
		alias: "Quote: Not Worthy to be Compared", 
		parent: "topic.THE GODHEAD", 
		tags: ["goodness", "divine", "injustice", "forgotten", "presence"], 
		source: "The Traveler's Oasis, Book One",
		booklink: "https://www.amazon.com/Travelers-Oasis-Book-One-ebook/dp/B00Y43B2OC",
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.FORGFOTTEN INJUSTICES", 
	en_title: "FORGOTTEN INJUSTICES", 
	en_content: "All of the gravest injustices committed by humanity against its own would not even be remembered in the Presence of the Divine Goodness.", 
	es_title: "INJUSTICIAS OLVIDADAS", 
	es_content: "Todas las más graves injusticias cometidas por la humanidad contra sí misma ni siquiera serían recordadas ante la Presencia de la Bondad Divina.", 
	fr_title: "INJUSTICES OUBLIÉES", 
	fr_content: "Toutes les injustices les plus graves commises par l’humanité envers les siens ne seraient même pas rappelées en présence de la Bonté Divine.", 
	hi_title: "भूले हुए अन्याय", 
	hi_content: "मानवता द्वारा अपने ही लोगों के विरुद्ध किए गए सभी गंभीर अन्याय ईश्वरीय अच्छाई की उपस्थिति में याद भी नहीं किए जाएँगे।", 
	zh_title: "Bèi yíwàng de bùgōng", 
	zh_content: "rénlèi duì zìjǐ fàn xià de suǒyǒu zuì yánzhòng de bùgōng, zài shénshèng shànliáng de miànqián dōu bù huì bèi jì qǐ."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = "quote.FORGOTTEN INJUSTICES" AND c.name = "content.FORGOTTEN INJUSTICES"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FORGOTTEN INJUSTICES"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "quote.FORGOTTEN INJUSTICES"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GODHEAD->FORGOTTEN INJUSTICES"}]->(child)
RETURN *;

```
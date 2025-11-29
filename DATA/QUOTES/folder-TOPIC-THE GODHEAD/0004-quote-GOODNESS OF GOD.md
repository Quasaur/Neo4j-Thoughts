```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE
    {
	    name: "quote.GOODNESS OF GOD",
		alias: "Quote: The Supreme Goodness of God", 
		parent: "topic.THE GODHEAD", 
		tags: ["goodness", "horrors", "god", "demons", "transcendent"], 
		source: "The Traveler's Oasis, Book One",
		booklink: "https://www.amazon.com/Travelers-Oasis-Book-One-ebook/dp/B00Y43B2OC",
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.GOODNESS OF GOD", 
	en_title: "GOODNESS OF GOD", 
	en_content: "None of the darkest horrors concocted by the most evil demonic force can ever have a chance against the Goodness of God.", 
	es_title: "Bondad de Dios", 
	es_content: "Bondad de Dios
Ninguno de los horrores más oscuros inventados por la fuerza demoníaca más maligna puede tener alguna posibilidad contra la Bondad de Dios.", 
	fr_title: "La bonté de Dieu", 
	fr_content: "Aucune des horreurs les plus sombres concoctées par la force démoniaque la plus maléfique ne peut avoir la moindre chance contre la bonté de Dieu.", 
	hi_title: "ईश्वर की अच्छाई", 
	hi_content: "सबसे बुरी राक्षसी शक्ति द्वारा रची गई सबसे भयावह भयावहता कभी भी ईश्वर की अच्छाई के सामने टिक नहीं सकती।", 
	zh_title: "Shàngdì dì měidé", 
	zh_content: "zuì xié'è de èmó lìliàng suǒ zhìzào de zuì hēi'àn de kǒngbù, zài shàngdì dì měidé miànqián háo wú shèngsuàn."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = "quote.GOODNESS OF GOD" AND c.name = "content.GOODNESS OF GOD"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.GOODNESS OF GOD"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "quote.GOODNESS OF GOD"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GODHEAD->GOODNESS OF GOD"}]->(child)
RETURN *;

```
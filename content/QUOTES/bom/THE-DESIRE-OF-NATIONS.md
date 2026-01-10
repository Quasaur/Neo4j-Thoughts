---
name: "quote.THE DESIRE OF NATIONS"
alias: "Quote: Christ - the Fulfillment of All Desire"
type: QUOTE
parent: topic.WORSHIP
tags:
- ruler
- jesuschrist
- desire
- nations
- the_pearl
neo4j: true
ptopic: "[[topic-WORSHIP]]"
level: 2
---

```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE {
	    name: "quote.THE DESIRE OF NATIONS",
		alias: "Quote: Christ - the Fulfillment of All Desire", 
		parent: "topic.WORSHIP", 
		tags: ["ruler", "desire", "nations", "jesus_christ", "the_pearl"], 
		source: "The Basics and More: A Year's Sermons",
		booklink: "https://www.amazon.com/Basics-More-Years-Sermons-ebook/dp/B00XLMBDR8",
		notes: "",
		level: 2});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.THE DESIRE OF NATIONS",
	ctype: 2, // 1=thought; 2=quote; 3=passage
	en_title: "THE DESIRE OF NATIONS", 
	en_content: "The rich young ruler believed that Jesus had what he wanted, but he didn't know that Jesus was what he wanted.", 
	es_title: "El Deseado de las Naciones", 
	es_content: "El joven rico creía que Jesús tenía lo que quería, pero no sabía que Jesús era lo que él quería.", 
	fr_title: "Le désir des nations", 
	fr_content: "Le jeune homme riche croyait que Jésus avait ce qu'il voulait, mais il ne savait pas que Jésus était ce qu'il voulait.", 
	hi_title: "राष्ट्रों की अभिलाषा",
	hi_content: "धनी युवा शासक का मानना था कि यीशु के पास वह सब है जो वह चाहता था, लेकिन वह यह नहीं जानता था कि यीशु ही वह है जो वह चाहता था।",
	zh_title: "Lièguó de yuànwàng",
	zh_content: "zhè wèi niánqīng fùyǒu de guān xiāngxìn yēsū yǒngyǒu tā xiǎng yào de dōngxī, dàn tā bù zhīdào yēsū jiùshì tā xiǎng yào de dōngxī."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = 'quote.THE DESIRE OF NATIONS' AND c.name = 'content.THE DESIRE OF NATIONS'
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE DESIRE OF NATIONS"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = 'topic.WORSHIP' AND child.name = 'quote.THE DESIRE OF NATIONS'
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.WORSHIP->THE DESIRE OF NATIONS"}]->(child)
RETURN *;

```

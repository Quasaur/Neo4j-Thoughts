---
type: QUOTE
name: "quote.DESIRE OF NATIONS"
alias: "Quote: Christ the Fulfillment of All Desire"
parent: "topic.WORSHIP"
source: "The Basics and More: A Year's Sermons"
en_content: "The rich young ruler believed that Jesus had what he wanted, but he didn't know that Jesus was what he wanted."
tags: ["ruler", "jesus_christ", "desire", "nations", "the_pearl"]
ptopic: "[[topic-WORSHIP]]"
level: 2
neo4j: true
verified: true
---

```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE {     name: "quote.DESIRE OF NATIONS",
  alias: "Quote: Christ the Fulfillment of All Desire", 
  parent: "topic.WORSHIP", 
  tags: ["ruler", "jesus_christ", "desire", "nations", "the_pearl"], 
  source: "The Basics and More: A Year's Sermons",
  booklink: "https://www.amazon.com/Basics-More-Years-Sermons-ebook/dp/B00XLMBDR8",
  level: 2
 });
// create multi-lingual content  
CREATE (c:CONTENT {
 name: "content.DESIRE OF NATIONS",
 ctype: "QUOTE",
 en_title: "Quote: Christ the Fulfillment of All Desire", 
 en_content: "The rich young ruler believed that Jesus had what he wanted, but he didn't know that Jesus was what he wanted.", 
 es_title: "Cita: Cristo el cumplimiento de todo deseo", 
 es_content: "El joven rico creía que Jesús tenía lo que quería, pero no sabía que Jesús era lo que él quería.", 
 fr_title: "Citation : Le Christ, l'accomplissement de tous les désirs", 
 fr_content: "Le jeune homme riche croyait que Jésus avait ce qu'il voulait, mais il ne savait pas que Jésus était ce qu'il voulait.", 
 hi_title: "उद्धरण: मसीह सभी इच्छाओं की पूर्ति करते हैं",
 hi_content: "धनी युवा शासक का मानना था कि यीशु के पास वह सब है जो वह चाहता था, लेकिन वह यह नहीं जानता था कि यीशु ही वह है जो वह चाहता था।",
 zh_title: "yǐn yán : jī dū shì yī qiè yuàn wàng de shí xiàn",
 zh_content: "zhè wèi niánqīng fùyǒu de guān xiāngxìn yēsū yǒngyǒu tā xiǎng yào de dōngxī, dàn tā bù zhīdào yēsū jiùshì tā xiǎng yào de dōngxī."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = 'quote.DESIRE OF NATIONS' AND c.name = 'content.DESIRE OF NATIONS'
MERGE (q)-[:HAS_CONTENT {name: "q.edge.DESIRE OF NATIONS"}]->(c);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = 'topic.WORSHIP' AND child.name = 'quote.DESIRE OF NATIONS'
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.WORSHIP->DESIRE OF NATIONS"}]->(child);

```

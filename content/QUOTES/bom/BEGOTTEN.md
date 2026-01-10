---
name: quote.BEGOTTEN
alias: "Quote: God's Only Son"
type: QUOTE
parent: "topic.THE GOSPEL"
tags:
- adam
- first
- last
- jesuschrist
- begotten
neo4j: true
ptopic: "[[topic-THE]]"
level: 2
---

```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE {
	    name: "quote.BEGOTTEN",
		alias: "Quote: God's Only Son", 
		parent: "topic.THE GOSPEL", 
		tags: ["adam", "first", "last", "jrdud_christ", "begotten"], 
		source: "The Basics and More: A Year's Sermons",
		booklink: "https://www.amazon.com/Basics-More-Years-Sermons-ebook/dp/B00XLMBDR8",
		notes: "",
		level: 2});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.BEGOTTEN",
	ctype: 2, // 1=thought; 2=quote; 3=passage
	en_title: "BEGOTTEN", 
	en_content: "PLEASE UNDERSTAND: the First Adam was CREATED; the Last Adam is BEGOTTEN!!!  
That's why Jesus is called God's 'Only-Begotten' Son.", 
	es_title: "Engendrado", 
	es_content: "POR FAVOR, ENTIENDA: el Primer Adán fue CREADO; ¡el Último Adán es ENGENDRADO!
Por eso a Jesús se le llama el Hijo Unigénito de Dios.", 
	fr_title: "Engendré", 
	fr_content: "VEUILLEZ COMPRENDRE : le premier Adam a été CRÉÉ ; le dernier Adam est ENGENDÉ !
C’est pourquoi Jésus est appelé le Fils unique de Dieu.", 
	hi_title: "जन्मा",
	hi_content: "कृपया समझें: पहला आदम सृजा गया था; अंतिम आदम जन्मा है!!!
इसलिए यीशु को परमेश्वर का 'एकलौता' पुत्र कहा जाता है।",
	zh_title: "Shòu shēng",
	zh_content: "qǐng lǐjiě: Dì yī gè yàdāng shì bèi zào de; mòhòu de yàdāng shì shòu shēng de!!!
Yīncǐ, yēsū bèi chēng wéi shàngdì de “dúshēngzǐ”."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = 'quote.BEGOTTEN' AND c.name = 'content.BEGOTTEN'
MERGE (q)-[:HAS_CONTENT {name: "q.edge.BEGOTTEN"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = 'topic.THE GOSPEL' AND child.name = 'quote.BEGOTTEN'
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GOSPEL->BEGOTTEN"}]->(child)
RETURN *;

```

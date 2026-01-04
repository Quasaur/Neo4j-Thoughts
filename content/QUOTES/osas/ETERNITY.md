---
name: quote.ETERNITY
alias: "Quote: The Transcendent God"
type: QUOTE
parent: "topic.THE GODHEAD"
tags:
- god
- eternity
- beginningless
- endless
- transcendence
neo4j: true
level: 1
---

```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE
    {
	    name: "quote.ETERNITY",
		alias: "Quote: The Transcendent God", 
		parent: "topic.THE GODHEAD", 
		tags: ["god", "eternity", "beginningless", "endless", "transcendence"], 
		source: "Once Saved, Always Saved: The Assurance of Our Father's LOVE",
		booklink: "https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68",
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.ETERNITY", 
	en_title: "ETERNITY", 
	en_content: "With the word 'Eternity' we acknowledge (at least intellectually) that God has no beginning, which creates all kinds of problems for tiny minds like ours.", 
	es_title: "ETERNIDADMISMO", 
	es_content: "Con la palabra 'Eternidad' reconocemos (al menos intelectualmente) que Dios no tiene principio, lo cual crea todo tipo de problemas para mentes diminutas como la nuestra.", 
	fr_title: "ÉTERNITÉ", 
	fr_content: "Avec le mot « Éternité », nous reconnaissons (du moins intellectuellement) que Dieu n'a pas de commencement, ce qui crée toutes sortes de problèmes pour des esprits aussi petits que le nôtre.", 
	hi_title: "अनंत काल", 
	hi_content: "'अनंत काल' शब्द से हम स्वीकार करते हैं (कम से कम बौद्धिक रूप से) कि ईश्वर की कोई शुरुआत नहीं है, जो हमारे जैसे छोटे दिमागों के लिए सभी प्रकार की समस्याएं पैदा करता है।", 
	zh_title: "Yǒnghéng", 
	zh_content: "'yǒnghéng' yī cí yìwèizhe (zhìshǎo zài lǐzhì shàng) shàngdì wú shǐ, zhè gěi wǒmen zhèxiē miǎoxiǎo de xīnlíng dài láile gè zhǒng gè yàng de wèntí."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = "quote.ETERNITY" AND c.name = "content.ETERNITY"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ETERNITY"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "quote.ETERNITY"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GODHEAD->ETERNITY"}]->(child)
RETURN *;

```

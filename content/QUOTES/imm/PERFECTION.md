---
name: quote.PERFECTION
alias: "Quote: Perfection's Necessity"
type: QUOTE
parent: "topic.THE GODHEAD"
tags:
- imperfection
- perfection
- god
- existence
- duality
neo4j: true
ptopic: "[[topic-THE]]"
level: 1
---

```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE
    {
	    name: "quote.PERFECTION",
		alias: "Quote: Perfection's Necessity", 
		parent: "topic.THE GODHEAD", 
		tags: ["imperfection", "perfection", "god", "existence", "duality"], 
		source: "IMMMUNITY to the Lake of Fire: A No-Nonsense Guide",
		booklink: "https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J",
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.PERFECTION", 
	en_title: "PERFECTION", 
	en_content: "Be it ever so ubiquitous, the existence of imperfection does not prove that Perfection does not exist! Rather, the recognition of imperfection, by the very name with which we label it, is proof that, deep in the human spirit, the truth of Perfection is both extant and, at a very deep level, assumed even by those who dishonestly claim that It doesn’t exist. IF PERFECTION DOES NOT EXIST, NEITHER DOES IMPERFECTION; you can’t logically have one without the other!", 
	es_title: "Perfección", 
	es_content: "Por muy omnipresente que sea, la existencia de la imperfección no prueba que la perfección no exista. Más bien, reconocer la imperfección, por el mismo nombre con el que la llamamos, prueba que, en lo más profundo del espíritu humano, la verdad de la perfección existe y, a un nivel muy profundo, es asumida incluso por quienes afirman deshonestamente que no existe. Si la perfección no existe, la imperfección tampoco; ¡no es posible tener una sin la otra!", 
	fr_title: "Perfection", 
	fr_content: "Aussi omniprésente soit-elle, l'existence de l'imperfection ne prouve pas que la Perfection n'existe pas ! Au contraire, la reconnaissance de l'imperfection, par le nom même dont nous la désignons, prouve qu'au plus profond de l'esprit humain, la vérité de la Perfection existe et, à un niveau très profond, est assumée même par ceux qui prétendent malhonnêtement qu'elle n'existe pas. SI LA PERFECTION N'EXISTE PAS, L'IMPERFECTION NON PLUS ; l'une ne peut logiquement pas aller sans l'autre !", 
	hi_title: "पूर्णता", 
	hi_content: "चाहे वह सर्वव्यापी ही क्यों न हो, अपूर्णता का अस्तित्व यह सिद्ध नहीं करता कि पूर्णता का अस्तित्व ही नहीं है! बल्कि, अपूर्णता की पहचान, जिस नाम से हम उसे पुकारते हैं, वह इस बात का प्रमाण है कि, मानव आत्मा की गहराई में, पूर्णता का सत्य विद्यमान है और, बहुत गहरे स्तर पर, उन लोगों द्वारा भी ग्रहण किया जाता है जो बेईमानी से दावा करते हैं कि इसका अस्तित्व ही नहीं है। यदि पूर्णता का अस्तित्व नहीं है, तो अपूर्णता का भी नहीं; तार्किक रूप से एक के बिना दूसरा संभव नहीं है!", 
	zh_title: "Wánměi", 
	zh_content: "jǐnguǎn bù wánměi wú chù bùzài, dàn tā de cúnzài bìng bùnéng zhèngmíng wánměi bù cúnzài! Xiāngfǎn, wǒmen yòng bù wánměi zhège míngchēng lái dìngyì tā, qiàqià zhèngmíngliǎo zài rénlèi jīngshén shēn chù, wánměi de zhēnlǐ bùjǐn cúnzài, érqiě zài shēn céngcì shàng, jíshǐ shì nàxiē bù chéngshí dì shēngchēng wánměi bù cúnzài de rén, yě chéngrènle tā de cúnzài. Rúguǒ wánměi bù cúnzài, nàme bù wánměi yě tóngyàng bù cúnzài; cóng luójí shàng jiǎng, liǎng zhě quē yī bùkě!"});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = "quote.PERFECTION" AND c.name = "content.PERFECTION"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.PERFECTION"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "quote.PERFECTION"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GODHEAD->PERFECTION"}]->(child)
RETURN *;

```

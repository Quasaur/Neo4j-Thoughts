```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE {
	    name: "quote.WORKS",
		alias: "Quote: It Stands Alone", 
		parent: "topic.RELIGION", 
		tags: ["religion", "gospel", "truth", "works", "the_cross"], 
		source: "The Basics and More: A Year's Sermons",
		booklink: "https://www.amazon.com/Basics-More-Years-Sermons-ebook/dp/B00XLMBDR8",
		notes: "",
		level: 4});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.WORKS",
	ctype: 2, // 1=thought; 2=quote; 3=passage
	en_title: "WORKS", 
	en_content: "This is one of the most conveincing proofs of the Truth of Christianity: every other religion on the planet Earth is a religion of righteousness by works. That is why the Cross of Christ is considered foolish by the world.",
	es_title: "Obras", 
	es_content: "Esta es una de las pruebas más contundentes de la verdad del cristianismo: todas las demás religiones del planeta Tierra son religiones de justicia por obras. Por eso, la cruz de Cristo es considerada una locura por el mundo.",
	fr_title: "Œuvres", 
	fr_content: "C'est l'une des preuves les plus convaincantes de la vérité du christianisme : toutes les autres religions sur la planète Terre sont des religions de justice par les œuvres. C'est pourquoi la Croix du Christ est considérée comme une folie par le monde.",
	hi_title: "काम",
	hi_content: "यह ईसाई धर्म की सच्चाई का सबसे पक्का सबूत है: धरती पर बाकी सभी धर्म कामों से नेकी का धर्म है। इसीलिए दुनिया में क्राइस्ट के क्रॉस को बेवकूफी माना जाता है।",
	zh_title: "Xíngwéi",
	zh_content: "zhè shì jīdūjiào zhēnlǐ zuì lìng rén xìnfú de zhèngjù zhī yī: Dìqiú shàng suǒyǒu qítā zōngjiào dōu shì kào xíngwéi chēng yì de zōngjiào. Zhèng yīn rúcǐ, jīdū de shízìjià cái bèi shìrén shì wéi yúzhuō."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = 'quote.WORKS' AND c.name = 'content.WORKS'
MERGE (q)-[:HAS_CONTENT {name: "q.edge.WORKS"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = 'topic.RELIGION' AND child.name = 'quote.WORKS'
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->WORKS"}]->(child)
RETURN *;

```
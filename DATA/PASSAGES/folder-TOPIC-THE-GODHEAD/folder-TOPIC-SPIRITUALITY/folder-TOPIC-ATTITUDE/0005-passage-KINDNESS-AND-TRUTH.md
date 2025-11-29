```Cypher
//create the Passage with the same fields as a normal thought
CREATE (p:PASSAGE
    {
	    name: "passage.KINDNESS AND TRUTH",
		alias: "Passage: The Keys to Favor and a Good Reputation", 
		parent: "topic.ATTITUDE", 
		tags: ["kindness", "truth", "favor", "reputation", "god"], 
		source: "Proverbs 3:3,4",
		sortedsource: "Proverbs 03:03,04",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+3%3A3-4&version=NASB",
		notes: "",
		level: 3});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.KINDNESS AND TRUTH", 
	en_title: "KINDNESS AND TRUTH", 
	en_content: "Do not let kindness and truth leave you;
Bind them around your neck,
Write them on the tablet of your heart.
So you will find favor and a good reputation
In the sight of God and man.", 
	es_title: "Bondad y verdad", 
	es_content: "No dejes que la bondad y la verdad te abandonen;
átalas a tu cuello,
escríbelas en la tabla de tu corazón.
Así hallarás favor y buena reputación
ante los ojos de Dios y de los hombres.", 
	fr_title: "Bonté et vérité", 
	fr_content: "Ne laisse pas la bonté et la vérité t'abandonner ;
Lien-les autour de ton cou,
Écris-les sur la tablette de ton cœur.
Ainsi tu trouveras grâce et bonne réputation
Aux yeux de Dieu et des hommes.", 
	hi_title: "दया और सच्चाई", 
	hi_content: "दया और सच्चाई को अपने से दूर न जाने देना;
इन्हें अपने गले में बाँध लेना,
इन्हें अपने हृदय की पटिया पर लिख लेना।
ताकि तुम परमेश्वर और मनुष्य की दृष्टि में अनुग्रह और अच्छी प्रतिष्ठा पा सको।", 
	zh_title: "Cí'ài yǔ chéngshí", 
	zh_content: "bùkě ràng cí'ài yǔ chéngshí líkāi nǐ;
yào xì zài nǐ de jǐngxiàng shàng,
kè zài nǐ de xīn bǎn shàng.
Zhèyàng, nǐ bì zài shén hé shìrén miànqián méng ēnhuì, dé měihǎo de míngshēng."});
// link content to node
MATCH (p:PASSAGE)
MATCH (c:CONTENT)
WHERE p.name = "passage.KINDESS AND TRUTH" AND c.name = "content.KINDESS AND TRUTH"
MERGE (p)-[:HAS_CONTENT {name: "p.edge.KINDESS AND TRUTH"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:PASSAGE)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "passage.KINDESS AND TRUTH"
MERGE (parent)-[:HAS_PASSAGE {name: "edge.ATTITUDE->KINDESS AND TRUTH"}]->(child)
RETURN *;

```
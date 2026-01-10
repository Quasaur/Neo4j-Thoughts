---
name: quote.HEAVENLY-FOOD
alias: "Quote: Spiritual Nourishment"
type: QUOTE
parent: topic.SPIRITUALITY
tags:
- fullness
- satisfaction
- nourishment
- heavenly_food
- bread_of_life
neo4j: true
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
---

```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE {
	    name: "quote.HEAVENLY-FOOD",
		alias: "Quote: Spiritual Nourishment", 
		parent: "topic.SPIRITUALITY", 
		tags: ["fullness", "satisfaction", "heavenly_food", "nourishment", "bread_of_life"], 
		source: "The Basics and More: A Year's Sermons",
		booklink: "https://www.amazon.com/Basics-More-Years-Sermons-ebook/dp/B00XLMBDR8",
		notes: "",
		level: 2});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.HEAVENLY-FOOD",
	ctype: 2, // 1=thought; 2=quote; 3=passage
	en_title: "HEAVENLY FOOD", 
	en_content: "We try to make these things nourish our spirits, because we have not learned to sit at the Table of Heaven and eat the Heavenly Food as consistently and habitually as we eat physical food!", 
	es_title: "Alimento Celestial", 
	es_content: "Intentamos que estas cosas alimenten nuestro espíritu, porque no hemos aprendido a sentarnos a la Mesa del Cielo y comer el Alimento Celestial con tanta constancia y habitualidad como comemos la comida física.",
	fr_title: "Nourriture Céleste", 
	fr_content: "Nous essayons de nourrir notre esprit par ces choses, car nous n'avons pas appris à nous asseoir à la Table du Ciel et à manger la Nourriture Céleste aussi régulièrement et régulièrement que nous mangeons de la nourriture physique !",
	hi_title: "स्वर्गीय भोजन",
	hi_content: "हम इन चीज़ों से अपनी आत्मा को पोषित करने की कोशिश करते हैं, क्योंकि हमने स्वर्ग की मेज़ पर बैठकर स्वर्गीय भोजन को उतनी नियमितता और आदतन खाना नहीं सीखा है जितना हम भौतिक भोजन खाते हैं!",
	zh_title: "Tiāntáng měishí",
	zh_content: "wǒmen shìtú yòng zhèxiē dōngxī zīyǎng wǒmen de jīngshén, yīnwèi wǒmen hái méiyǒu xuéhuì xiàng chī wùzhí shíwù yīyàng, zuò zài tiāntáng de cānzhuō páng, chíxù, xíguàn xìng dì xiǎngyòng tiāntáng měishí!"});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = 'quote.HEAVENLY-FOOD' AND c.name = 'content.HEAVENLY-FOOD'
MERGE (q)-[:HAS_CONTENT {name: "q.edge.HEAVENLY-FOOD"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = 'topic.SPIRITUALITY' AND child.name = 'quote.HEAVENLY-FOOD'
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.SPIRITUALITY->HEAVENLY-FOOD"}]->(child)
RETURN *;

```

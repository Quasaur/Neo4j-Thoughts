```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE
    {
	    name: "quote.MIRACLES (2)",
		alias: "Quote: Divine Miracles", 
		parent: "topic.THE GODHEAD", 
		tags: ["miracles", "divine", "reason", "logic", "discernment"], 
		source: "IMMMUNITY to the Lake of Fire: A No-Nonsense Guide",
		booklink: "https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J",
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.MIRACLES (2)", 
	en_title: "MIRACLES (2)", 
	en_content: "When the One True GOD performs a miracle, that miracle is entirely consistent with His overall Purpose and Agenda; which means that while Divine miracles transcend reason and logic, they do not contradict reason and logic…a distinction that is critical to discerning between the Finger of GOD and the lying wonders of Satan.", 
	es_title: "Milagros (2)", 
	es_content: "Cuando el Único Dios Verdadero realiza un milagro, ese milagro es totalmente coherente con Su Propósito y Agenda generales; lo que significa que, si bien los milagros Divinos trascienden la razón y la lógica, no las contradicen… una distinción fundamental para discernir entre el Dedo de Dios y las maravillas mentirosas de Satanás.", 
	fr_title: "Miracles (2)", 
	fr_content: "Lorsque le Seul Vrai DIEU accomplit un miracle, celui-ci est entièrement cohérent avec Son Dessein et Son Programme ; ce qui signifie que, si les miracles divins transcendent la raison et la logique, ils ne les contredisent pas… une distinction essentielle pour discerner entre le Doigt de DIEU et les prodiges mensongers de Satan.", 
	hi_title: "चमत्कार (2)", 
	hi_content: "जब एकमात्र सच्चा ईश्वर कोई चमत्कार करता है, तो वह चमत्कार उसके समग्र उद्देश्य और एजेंडे के साथ पूरी तरह से सुसंगत होता है; जिसका अर्थ है कि दिव्य चमत्कार तर्क और तर्क से परे होते हुए भी, तर्क और तर्क का खंडन नहीं करते... यह एक ऐसा अंतर है जो ईश्वर की उंगली और शैतान के झूठे चमत्कारों के बीच अंतर करने के लिए महत्वपूर्ण है।", 
	zh_title: "Qíjì (2)", 
	zh_content: "dāng dú yī zhēnshén xíng qíjì shí, gāi qíjì wánquán fúhé tā de zǒngtǐ mùdì hé yìchéng; zhè yìwèizhe, suīrán shénshèng qíjì chāoyuèle lǐxìng hé luójí, dàn tāmen bìng bù yǔ lǐxìng hé luójí xiāng máodùn……zhè yī qūbié duìyú biànbié shàngdì de shǒuzhǐ hé sādàn de huǎngyán qíjì zhì guān zhòngyào."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = "quote.MIRACLES (2)" AND c.name = "content.MIRACLES (2)"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.MIRACLES (2)"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "quote.MIRACLES (2)"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GODHEAD->MIRACLES (2)"}]->(child)
RETURN *;

```
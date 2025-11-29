```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.LOVE",
		alias: "Topic: God is Love", 
		parent: "topic.THE GODHEAD", 
		tags: ["divine", "love", "spirit", "affection", "cherish"], 
		notes: "",
		level: 2});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.LOVE", 
	en_title: "LOVE", 
	en_content: "A strong affection for another arising out of kinship or personal ties; attraction based on affection and tenderness; affection based on admiration, benevolence, or common interests; an assurance of affection; warm attachment, enthusiasm, or devotion; the object of attachment, devotion, or admiration.", 
	es_title: "AMOR", 
	es_content: "Un fuerte afecto por otra persona que surge del parentesco o de lazos personales; atracción basada en el afecto y la ternura; afecto basado en la admiración, la benevolencia o intereses comunes; una garantía de afecto; un cálido apego, entusiasmo o devoción; el objeto de apego, devoción o admiración.", 
	fr_title: "AMOUR", 
	fr_content: "AMOUR
Une forte affection pour autrui découlant de liens familiaux ou personnels ; une attirance fondée sur l’affection et la tendresse ; une affection fondée sur l’admiration, la bienveillance ou des intérêts communs ; une assurance d’affection ; un attachement chaleureux, de l’enthousiasme ou de la dévotion ; l’objet d’attachement, de dévotion ou d’admiration.", 
	hi_title: "पवित्रता", 
	hi_content: "किसी दूसरे के प्रति रिश्तेदारी या व्यक्तिगत संबंधों से उत्पन्न होने वाला गहरा स्नेह; स्नेह और कोमलता पर आधारित आकर्षण; प्रशंसा, परोपकार या सामान्य हितों पर आधारित स्नेह; स्नेह का आश्वासन; गर्मजोशी से भरा लगाव, उत्साह या भक्ति; लगाव, भक्ति या प्रशंसा की वस्तु।", 
	zh_title: "Ài", 
	zh_content: "yīn qīnshǔ guānxì huò gèrén guānxì ér duì tārén de qiángliè gǎnqíng; jīyú àimù hé wēnróu de xīyǐn; jīyú qīnpèi, réncí huò gòngtóng lìyì de gǎnqíng; gǎnqíng de bǎozhèng; rèliè de yīliàn, rèqíng huò zhōngchéng; yīliàn, zhōngchéng huò qīnpèi de duìxiàng."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.LOVE" AND d.name = "desc.LOVE"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.Love"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.LOVE"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->LOVE"}]->(child)
RETURN *;

```
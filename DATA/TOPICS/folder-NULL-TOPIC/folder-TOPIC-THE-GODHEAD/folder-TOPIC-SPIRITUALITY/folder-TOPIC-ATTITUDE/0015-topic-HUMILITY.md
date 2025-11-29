```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.HUMILITY",
		alias: "Topic: Lowliness of Heart", 
		parent: "topic.ATTITUDE", 
		tags: ["humble", "lowly", "service", "lowliness", "meekness"], 
		notes: "",
		level: 4});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.HUMILITY", 
	en_title: "HUMILITY", 
	en_content: "Not having or showing any feelings of superiority, self-assertiveness, or showiness.", 
	es_title: "Humildad", 
	es_content: "No tener ni mostrar sentimientos de superioridad, autoafirmación ni ostentación.", 
	fr_title: "Humilité", 
	fr_content: "Ne pas éprouver ni manifester de sentiments de supériorité, d'affirmation de soi ou d'ostentation.", 
	hi_title: "विनम्रता", 
	hi_content: "श्रेष्ठता, आत्म-दृढ़ता या दिखावे जैसी कोई भावना न रखना या प्रदर्शित न करना।", 
	zh_title: "Qiānxùn", 
	zh_content: "bù biǎoxiàn chū rènhé yōuyuè gǎn, zìfù gǎn huò xuànyào gǎn."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.HUMILITY' AND d.name = 'desc.HUMILITY'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.HUMILITY"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "topic.HUMILITY"
MERGE (parent)-[:HAS_CHILD {name: "edge.ATTITUDE->HUMILITY"}]->(child)
RETURN *;

```
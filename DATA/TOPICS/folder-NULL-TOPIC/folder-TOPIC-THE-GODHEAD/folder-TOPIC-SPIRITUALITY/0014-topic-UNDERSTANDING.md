```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.UNDERSTANDING",
		alias: "Topic: Comprehension", 
		parent: "topic.SPIRITUALITY", 
		tags: ["comprehension", "mental", "grasp", "ascertain", "agreement"], 
		notes: "",
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.UNDERSTANDING", 
	en_title: "UNDERSTANDING", 
	en_content: "A mental grasp of truth or an agreement between individuals or groups.", 
	es_title: "Comprensión", 
	es_content: "Una comprensión mental de la verdad o un acuerdo entre individuos o grupos.", 
	fr_title: "Compréhension", 
	fr_content: "Une compréhension mentale de la vérité ou un accord entre des individus ou des groupes.", 
	hi_title: "समझ", 
	hi_content: "सत्य की मानसिक समझ या व्यक्तियों या समूहों के बीच सहमति।", 
	zh_title: "Lǐjiě", 
	zh_content: "duì zhēnlǐ de xīnlǐ bǎwò, huò gèrén huò qúntǐ zhī jiān de gòngshì."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.UNDERSTANDING' AND d.name = 'desc.UNDERSTANDING'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.UNDERSTANDING"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = 'topic.SPIRITUALITY' AND child.name = 'topic.UNDERSTANDING'
MERGE (parent)-[:HAS_CHILD {name: "edge.SPIRITUALITY->UNDERSTANDING"}]->(child)
RETURN *;

```
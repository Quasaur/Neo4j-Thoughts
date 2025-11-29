```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.PSYCHOLOGY",
		alias: "Topic: The Science of Mind and Behavior", 
		parent: "topic.HUMANITY", 
		tags: ["soul", "psyche", "mind", "awareness", "consciousness"], 
		notes: "Possible Subtopics:
- Topic: Behavioral Psychology
- Topic: Clinical Psychology
- Topic: Cognitive Psychology
- Topic: Developmental Psychology
- Topic: Social Psychology",
		level: 4});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.PSYCHOLOGY", 
	en_title: "PSYCHOLOGY", 
	en_content: "The study of mind and behavior in relation to a particular field of knowledge or activity.", 
	es_title: "Psicología", 
	es_content: "El estudio de la mente y el comportamiento en relación con un campo particular de conocimiento o actividad.", 
	fr_title: "Psychologie", 
	fr_content: "L'étude de l'esprit et du comportement en relation avec un domaine particulier de connaissance ou d'activité.", 
	hi_title: "साइकोलॉजी",
	hi_content: "किसी खास ज्ञान या काम के क्षेत्र के संबंध में मन और व्यवहार का अध्ययन।",
	zh_title: "Xīnlǐ xué",
	zh_content: "yánjiū xīnlǐ hé xíngwéi yǔ tèdìng zhīshì lǐngyù huò huódòng zhī jiān guānxì de xuékē."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.PSYCHOLOGY' AND d.name = 'desc.PSYCHOLOGY'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.PSYCHOLOGY"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.HUMANITY" AND child.name = "topic.PSYCHOLOGY"
MERGE (parent)-[:HAS_CHILD {name: "edge.HUMANITY->PSYCHOLOGY"}]->(child)
RETURN *;

```
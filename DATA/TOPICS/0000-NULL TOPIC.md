```Cypher
//create the NULL TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "NULL TOPIC",
		alias: "Topic ZERO: THE NULL TOPIC", 
		parent: null, 
		tags: ["topic", "first", "prime", "root"], 
		notes: "",
		level: 0});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.NULL_TOPIC", 
	en_title: "Null Topic", 
	en_content: "This is the NULL TOPIC: the root of the Book of Thoughts graph database.", 
	es_title: "Tema Nulo", 
	es_content: "Este es el TEMA NULO: la raíz de la base de datos gráfica del Libro de Pensamientos.", 
	fr_title: "Thème racine", 
	fr_content: "Il s'agit du SUJET NULL : la racine de la base de données graphique du Livre des Pensées.", 
	hi_title: "मूल विषय", 
	hi_content: "यह शून्य विषय है: विचारों की पुस्तक ग्राफ डेटाबेस का मूल।", 
	zh_title: "Zhēnlǐ", 
	zh_content: "chāoyuè de gēnběn huò jīngshén xiànshí."});
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "NULL TOPIC" AND d.name = "desc.NULL_TOPIC"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.NULL_TOPIC"}]->(d)
RETURN *;
CREATE INDEX FOR (t:TOPIC) ON (t.name);
CREATE INDEX FOR (d:DESCRIPTION) ON (d.name);
```
```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.GOD-AWARENESS",
		alias: "Thought: The God Who is Here", 
		parent: "topic.THE GODHEAD", 
		tags: ["faith", "awareness", "self", "god", "worship"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.GOD-AWARENESS", 
	en_title: "GOD-AWARENESS", 
	en_content: "Self-awareness is the second most precious gift God has given us; the first is God-awareness!", 
	es_title: "CONCIENCIA DE DIOS", 
	es_content: "La autoconciencia es el segundo regalo más preciado que Dios nos ha dado; ¡el primero es la conciencia de Dios!", 
	fr_title: "LA CONSCIENCE DE DIEU", 
	fr_content: "La conscience de soi est le deuxième don le plus précieux que Dieu nous ait fait ; le premier est la conscience de Dieu !", 
	hi_title: "ईश्वर-जागरूकता", 
	hi_content: "आत्म-जागरूकता ईश्वर द्वारा हमें दिया गया दूसरा सबसे कीमती उपहार है; पहला है ईश्वर-जागरूकता!", 
	zh_title: "Shén shí", 
	zh_content: "zìwǒ yìshí shì shàngdì cìyǔ wǒmen de dì èr zhēnguì de lǐwù; dì yī zhēnguì de lǐwù shì shén shí!"});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD-AWARENESS" AND c.name = "content.GOD-AWARENESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.GOD-AWARENESS"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD-AWARENESS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->GOD-AWARENESS"}]->(child)
RETURN *;

```
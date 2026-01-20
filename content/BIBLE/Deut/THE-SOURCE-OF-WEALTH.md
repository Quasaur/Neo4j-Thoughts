---
name: "passage.THE SOURCE OF WEALTH"
alias: "Passage: God--the Source of Abundance!"
type: PASSAGE
parent: topic.WEALTH
tags:
- wealth
- gain
- god
- source
- power
neo4j: true
ptopic: "[[topic-WEALTH]]"
level: 3
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (b:PASSAGE
    {
	    name: "passage.THE SOURCE OF WEALTH",
		alias: "Passage: God--the Source of Abundance!", 
		parent: "topic.WEALTH", 
		tags: ["wealth", "gain", "god", "source", "power"], 
		source: "Deuteronomy 8:18",
		sortedsource: "Deuteronomy 08:18",
		biblelink: "https://www.biblegateway.com/passage/?search=Deuteronomy%208%3A18&version=NASB",
		notes: "",
		level: 2});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.THE SOURCE OF WEALTH", 
	en_title: "THE SOURCE OF WEALTH", 
	en_content: "But you are to remember the LORD your God, for it is He Who is giving you power to make wealth, in order to confirm His Covenant which He swore to your fathers, as it is this day.", 
	es_title: "La Fuente de la Riqueza", 
	es_content: "Pero acuérdate del Señor tu Dios, porque Él te da el poder para hacer las riquezas, a fin de confirmar su pacto que juró a tus padres, como en este día.", 
	fr_title: "La source des richesses", 
	fr_content: "Mais vous vous souviendrez de l'Éternel, votre Dieu, car c'est lui qui vous donne la force de vous enrichir, afin de confirmer son alliance qu'il a jurée à vos pères, comme elle l'est aujourd'hui.", 
	hi_title: "धन का स्रोत", 
	hi_content: "परन्तु तुम्हें अपने परमेश्वर यहोवा को स्मरण रखना है, क्योंकि वही तुम्हें धन कमाने की शक्ति दे रहा है, ताकि वह अपनी उस वाचा को पूरा करे जो उसने तुम्हारे पूर्वजों से शपथ खाकर बाँधी थी, जैसा कि आज है।", 
	zh_title: "Cáifù zhī yuán", 
	zh_content: "dàn nǐmen yào jìniàn yēhéhuá nǐmen de shén, yīn wéi dé cáifù de lìliàng shì tā gěi nǐmen de, wèi yào jiāndìng tā xiàng nǐmen zǔxiān qǐshì suǒ lì de yuē, xiàng jīnrì yīyàng."});
// link content to node
MATCH (b:PASSAGE)
MATCH (c:CONTENT)
WHERE b.name = "passage.THE SOURCE OF WEALTH" AND c.name = "content.THE SOURCE OF WEALTH"
MERGE (b)-[:HAS_CONTENT {name: "b.edge.THE SOURCE OF WEALTH"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC {name: "topic.WEALTH"})
MATCH (child:PASSAGE {name: "passage.THE SOURCE OF WEALTH"})
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.WEALTH->THE SOURCE OF WEALTH"}]->(child)
RETURN *;

```

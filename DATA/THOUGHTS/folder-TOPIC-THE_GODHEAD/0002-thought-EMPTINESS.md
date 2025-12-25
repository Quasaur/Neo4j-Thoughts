```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.EMPTINESS",
		alias: "Thought: The Void Within", 
		parent: "topic.THE GODHEAD", 
		tags: ["emptiness", "void", "hunger", "addiction", "spirituality"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.EMPTINESS", 
	en_title: "EMPTINESS", 
	en_content: "It’s why we eat when we’re not hungry.  
It’s why we watch hours of mindless television and play with ouija boards and horoscopes.  
It’s why we pursue one addiction after another, and there’s only One Cure that will fill that black hole in the core of our being: The Lord Jesus Christ.  
How insane it is, then, to attend Church for years and NEVER meet Jesus!!!", 
	es_title: "VACÍO", 
	es_content: "Por eso comemos cuando no tenemos hambre.
Por eso vemos horas de televisión sin sentido y jugamos con tablas de ouija y horóscopos.
Por eso nos aferramos a una adicción tras otra, y solo hay una cura que llenará ese vacío en lo más profundo de nuestro ser: El Señor Jesucristo.
¡Qué locura es, entonces, ir a la iglesia durante años y no conocer jamás a Jesús!", 
	fr_title: "VIDE", 
	fr_content: "C'est pourquoi nous mangeons sans avoir faim.
C'est pourquoi nous regardons la télévision pendant des heures et jouons avec des planches Ouija et des horoscopes.
C'est pourquoi nous nous lançons dans une addiction après l'autre, et il n'existe qu'un seul remède pour combler ce vide au plus profond de notre être : le Seigneur Jésus-Christ.
Quelle folie, alors, de fréquenter l'église pendant des années sans JAMAIS rencontrer Jésus !", 
	hi_title: "खालीपन", 
	hi_content: "यही कारण है कि हम तब भी खाते हैं जब हमें भूख नहीं होती।
यही कारण है कि हम घंटों बिना सोचे-समझे टीवी देखते हैं और ओइजा बोर्ड और राशिफल के साथ खेलते हैं।
यही कारण है कि हम एक के बाद एक लत में पड़ जाते हैं, और केवल एक ही इलाज है जो हमारे अस्तित्व के मूल में उस काले छेद को भर सकता है: प्रभु यीशु मसीह।
तो, सालों तक चर्च में जाना और कभी यीशु से न मिलना कितना पागलपन है!!!", 
	zh_title: "Kōngxū",
	zh_content: "zhè jiùshì wèishéme wǒmen bù è de shíhòu yě huì chī dōngxī.
Zhè jiùshì wèishéme wǒmen huì liánxù jǐ gè xiǎoshí kàn wúliáo de diànshì jiémù, wán tōng líng bǎn hé xīngzuò yùnshì.
Zhè jiùshì wèishéme wǒmen huì yīgè jiē yīgè de chénmí yú mǒu gè shìwù, ér zhǐyǒu yī zhǒng jiě yào cáinéng tiánbǔ wǒmen nèixīn shēn chǔ de hēidòng: Zhǔ yēsū jīdū.
Nàme, duōnián lái yīzhí qù jiàotáng què cóng wèi jiànguò yēsū, zhè shì duōme fēngkuáng a!!!"});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EMPTINESS" AND c.name = "content.EMPTINESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.EMPTINESS"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.EMPTINESS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->EMPTINESS"}]->(child)
RETURN *;

```
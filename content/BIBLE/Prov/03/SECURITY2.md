---
name: "passage.SECURITY (2)"
alias: "Passage: Wisdom and Discretion"
type: PASSAGE
parent: topic.WISDOM
tags:
- discretion
- wisdom
- secure
- life
- confidence
neo4j: true
ptopic: "[[topic-WISDOM]]"
level: 3
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (p:PASSAGE {
	    name: "passage.SECURITY (2)",
		alias: "Passage: Wisdom and Discretion", 
		parent: "topic.WISDOM", 
		tags: ["discretion", "wisdom", "secure", "life", "confidence"], 
		source: "Proverbs 3:21-26",
		sortedsource: "Proverbs 03:21-26",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%203%3A21-26&version=ESV",
		notes: "",
		level: 3});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.SECURITY (2)",
	ctype: 3, // 1=thought; 2=quote; 3=passage
	en_title: "SECURITY (2)", 
	en_content: "My son, do not lose sight of these—  
keep sound wisdom and discretion,  
and they will be life for your soul  
and adornment for your neck.  
Then you will walk on your way securely,  
and your foot will not stumble.  
If you lie down, you will not be afraid;  
when you lie down, your sleep will be sweet.  
Do not be afraid of sudden terror  
or of the ruin of the wicked, when it comes, for the LORD will be your confidence  
and will keep your foot from being caught.", 
	es_title: "Seguridad (2)", 
	es_content: "Hijo mío, no pierdas de vista estas cosas:
mantén la sana prudencia y la discreción,
y serán vida para tu alma
y adorno para tu cuello.
Así andarás seguro por tu camino,
y tu pie no tropezará.
Si te acuestas, no tendrás miedo;
cuando te acuestes, tu sueño será dulce.
No temas el terror repentino
ni la ruina de los malvados cuando llegue, porque el SEÑOR será tu confianza
y guardará tu pie de ser atrapado.", 
	fr_title: "Sécurité (2)",
	fr_content: "Mon fils, ne perds pas ces choses de vue :
garde la sagesse et la réflexion,
et elles seront la vie de ton âme
et la parure de ton cou.
Alors tu marcheras en sécurité sur ton chemin,
et ton pied ne trébuchera pas.
Si tu te couches, tu n’auras pas peur ;
après t’être couché, ton sommeil sera doux.
Ne crains pas une terreur soudaine
ni la ruine des méchants, quand elle viendra, car l’Éternel sera ta confiance
et préservera ton pied de toute embûche.", 
	hi_title: "सुरक्षा (2)",
	hi_content: "हे मेरे पुत्र, इन बातों को नज़रअंदाज़ मत कर—
सद्बुद्धि और विवेक बनाए रख,
और ये तेरे प्राण के लिए जीवन और तेरे गले का श्रृंगार ठहरेंगे।
तब तू अपने मार्ग पर निडर चलेगा,
और तेरा पाँव ठोकर नहीं खाएगा।
यदि तू लेट जाए, तो तुझे भय नहीं होगा;
जब तू लेटेगा, तब तुझे मीठी नींद आएगी।
अचानक आने वाले भय से मत डर
या दुष्टों के विनाश से मत डर, क्योंकि यहोवा तेरा सहारा होगा
और तेरे पाँव को फँसने से बचाएगा।", 
	zh_title: "Ānquán gǎn (2)",
	zh_content: "wǒ er, bùkě wàngjì zhèxiē, yào jǐn shǒu zhēn zhìhuì hé móulüè,
zhèxiē bì zuò nǐ línghún de shēngmìng, hé nǐ jǐngxiàng de zhuāngshì.
Zhèyàng, nǐ biàn néng ānrán xíngzǒu,
nǐ de jiǎo yě bù zhì diédǎo.
Nǐ tǎng xià, bì bù jùpà; nǐ tǎng xià, shuì dé xiāngtián.
Bùyào hàipà tū lái de jīngkǒng,
yě bùyào hàipà èrén de huǐmiè líndào. Yīnwèi yēhéhuá shì nǐ suǒ yǐkào de,
tā bì bǎoshǒu nǐ de jiǎo bù bèi bàn dào."});
// link content to node
MATCH (p:PASSAGE)
MATCH (c:CONTENT)
WHERE p.name = 'passage.SECURITY (2)' AND c.name = 'content.SECURITY (2)'
MERGE (p)-[:HAS_CONTENT {name: "p.edge.SECURITY (2)"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:PASSAGE)
WHERE parent.name = 'topic.WISDOM' AND child.name = 'passage.SECURITY (2)'
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.WISDOM->SECURITY (2)"}]->(child)
RETURN *;

```

---
type: PASSAGE
name: "passage.UNJUST GAIN"
alias: "Passage: Cheating is Deadly"
parent: "topic.WEALTH"
sortedsource: "Proverbs 01:16-19"
en_content: "For their feet run to evil, And they are quick to shed blood. Indeed, it is useless to spread the baited net In the sight of any bird; But they lie in wait for their own blood; They ambush their own lives. Such are the ways of everyone who makes unjust gain; It takes away the life of its possessors."
tags: ["gain", "greed", "unjust", "death", "just"]
ptopic: "[[topic-WEALTH]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'p' and 'c' as variables to keep them in memory
CREATE (p:PASSAGE {
    name: "passage.UNJUST GAIN",
    parent: "topic.WEALTH",
		alias: "Passage: Cheating is Deadly", 
		tags: ["gain", "greed", "unjust", "death", "just"], 
		source: "Proverbs 1:16-19",
		sortedsource: "Proverbs 01:16-19",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%201%3A16-19&version=NASB",
		level: 3
})

CREATE (c:CONTENT {
	name: "content.UNJUST GAIN",
	ctype: "PASSAGE",
	en_title: "Passaage: Unjust Gain", 
	en_content: "For their feet run to evil,
	And they are quick to shed blood.
	Indeed, it is useless to spread the baited net
	In the sight of any bird;
	But they lie in wait for their own blood;
	They ambush their own lives.
	Such are the ways of everyone who makes unjust gain;
	It takes away the life of its possessors.", 
	es_title: "Pasaje: Hacer trampa es mortal",
	es_content: "Porque sus pies corren hacia el mal,
	Y se apresuran a derramar sangre.
	De hecho, es inútil tender la red cebada
	A la vista de cualquier pájaro;
	Pero acechan su propia sangre;
	Ellos tienden una emboscada a sus propias vidas.
	Así es el proceder de todo aquel que obtiene ganancia injusta;
	Quita la vida a sus poseedores.", 
	fr_title: "Passage : La tricherie est mortelle", 
	fr_content: "Car leurs pieds courent vers le mal,
	Et ils sont prompts à verser le sang.
	En effet, il est inutile de déployer le filet appâté 
	À la vue de n'importe quel oiseau ;
	Mais ils guettent leur propre sang ;
	Ils tendent une embuscade à leur propre vie.
	Telles sont les voies de quiconque réalise un gain injuste ;
	Cela ôte la vie à ses propriétaires.", 
	hi_title: "परिच्छेद: धोखा देना घातक है", 
	hi_content: "क्योंकि उनके पांव बुराई की ओर दौड़ते हैं,
	और वे खून बहाने में तत्पर हैं।
	दरअसल, जाल फैलाना बेकार है
	किसी भी पक्षी की दृष्टि में;
	परन्तु वे अपने ही खून के घात में बैठे रहते हैं;
	वे अपने ही जीवन पर घात लगाते हैं।
	अन्यायपूर्ण लाभ कमाने वाले प्रत्येक व्यक्ति की चाल ऐसी ही होती है;
	यह अपने धारकों का जीवन छीन लेता है।", 
	zh_title: "duàn luò : zuò bì shì zhì mìng de", 
	zh_content: "yīn wèi tā men de jiǎo bēn xiàng xié è , 
	ér qiě tā men hěn kuài jiù huì liú xiě . 
	què shí , sā xià yòu ěr wǎng shì méi yǒu yòng de zài rèn hé niǎo lèi de shì xiàn zhōng ; 
	dàn tā men què mái fú zhe děng dài zì jǐ de xiān xuè ; 
	tā men mái fú le zì jǐ de shēng mìng . 
	zhè jiù shì měi gè móu qǔ bù zhèng dāng lì yì de rén de zuò fǎ ; 
	tā duó zǒu le tā de yōng yǒu zhě de shēng mìng ."
})

// 2. Link Content to Passage using the variables 'p' and 'c'
MERGE (p)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.UNJUST GAIN"

// 3. Pass 'p' forward, find the Parent Topic, and link them
WITH p
MATCH (parent:TOPIC {name: "topic.WEALTH"})
MERGE (parent)-[r2:HAS_PASSAGE]->(p)
ON CREATE SET r2.name = "p.edge.WEALTH->UNJUST GAIN"
RETURN p, parent;
```

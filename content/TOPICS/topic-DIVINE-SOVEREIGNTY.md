---
name: "topic.DIVINE SOVEREIGNTY"
alias: "Topic: Predestination"
type: TOPIC
parent: "topic.THE GODHEAD"
tags:
- sovereignty
- lordship
- determinism
- absolute
- volition
neo4j: true
level: 2
---

```Cypher
//create the NULL with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.DIVINE SOVEREIGNTY",
		alias: "Topic: Predestination", 
		parent: "topic.THE GODHEAD", 
		tags: ["sovereignty", "lordship", "determinism", "absolute", "volition"], 
		notes: "",
		level: 2});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.DIVINE SOVEREIGNTY", 
	en_title: "DIVINE SOVEREIGNTY", 
	en_content: "The theological concept that God has absolute control over all things, meaning everything that happens in the universe occurs according to His plan and will, signifying His supreme authority and power over creation; essentially, God is the ultimate ruler with complete dominion over all aspects of existence.", 
	es_title: "SOBERANÍA DIVINA", 
	es_content: "El concepto teológico de que Dios tiene control absoluto sobre todas las cosas, lo que significa que todo lo que sucede en el universo ocurre según su plan y voluntad, lo que significa su suprema autoridad y poder sobre la creación; esencialmente, Dios es el gobernante supremo con dominio completo sobre todos los aspectos de la existencia.", 
	fr_title: "SOUVERAINETÉ DIVINE", 
	fr_content: "Concept théologique selon lequel Dieu exerce un contrôle absolu sur toutes choses, ce qui signifie que tout ce qui se passe dans l'univers se produit selon son plan et sa volonté, témoignant de son autorité et de son pouvoir suprêmes sur la création. Essentiellement, Dieu est le souverain ultime, régnant entièrement sur tous les aspects de l'existence.", 
	hi_title: "ईश्वरीय संप्रभुता", 
	hi_content: "धार्मिक अवधारणा यह है कि ईश्वर का सभी चीज़ों पर पूर्ण नियंत्रण है, जिसका अर्थ है कि ब्रह्मांड में जो कुछ भी होता है वह उसकी योजना और इच्छा के अनुसार होता है, जो सृष्टि पर उसके सर्वोच्च अधिकार और शक्ति को दर्शाता है; अनिवार्य रूप से, ईश्वर अस्तित्व के सभी पहलुओं पर पूर्ण प्रभुत्व रखने वाला अंतिम शासक है।", 
	zh_title: "Shénshèng zhǔquán", 
	zh_content: "shénxué gàiniàn rènwéi, shàngdì duì wànwù yǒngyǒu juéduì de zhǎngkòng quán, yǔzhòu zhōng fāshēng de yīqiè dōu ànzhào tā de jìhuà hé zhǐyì jìnxíng, zhāngxiǎnle tā duì wànwù de zuìgāo quánwēi hàn lìliàng; běnzhí shàng, shàngdì shì zhōngjí tǒngzhì zhě, wánquán tǒnglǐng wànwù."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.DIVINE SOVEREIGNTY" AND d.name = "desc.DIVINE SOVEREIGNTY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.Divine Sovereignty"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.DIVINE SOVEREIGNTY"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->DIVINE SOVEREIGNTY"}]->(child)
RETURN *;

```
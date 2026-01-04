---
name: "passage.HONOR GOD"
alias: "Passage: Add Offerings and Charity to your Budget"
type: PASSAGE
parent: topic.WEALTH
tags:
- god
- wealth
- firstfruits
- plenty
- overflow
neo4j: true
level: 3
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (b:PASSAGE
    {
	    name: "passage.HONOR GOD",
		alias: "Passage: Add Offerings and Charity to your Budget", 
		parent: "topic.WEALTH", 
		tags: ["god", "wealth", "firstfruits", "plenty", "overflow"], 
		source: "Proverbs 3:9,10",
		sortedsource: "Proverbs 03:09,10",
		biblelink: "https://www.biblegateway.com/passage/?search=proverbs+3%3A9-10&version=NASB",
		notes: "",
		level: 2});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.HONOR GOD", 
	en_title: "HONOR GOD", 
	en_content: "Honor the LORD from your wealth,  
And from the first of all your produce;  
Then your barns will be filled with plenty,  
And your vats will overflow with new wine.", 
	es_title: "Honra a Dios", 
	es_content: "Honra al SEÑOR con tus riquezas,
y con las primicias de todos tus frutos;
entonces tus graneros se llenarán con abundancia,
y tus lagares rebosarán de mosto.", 
	fr_title: "Honore Dieu", 
	fr_content: "Honore l'Éternel avec tes biens,
et avec les prémices de tous tes revenus ;
alors tes greniers seront remplis d'abondance,
et tes cuves regorgeront de moût.", 
	hi_title: "परमेश्वर का आदर करो", 
	hi_content: "अपने धन से यहोवा का आदर करो,
और अपनी सारी उपज की पहली उपज से;
तब तुम्हारे खत्ते बहुतायत से भर जाएँगे,
और तुम्हारे कुण्ड नए दाखमधु से उमड़ेंगे।", 
	zh_title: "Zūnchóng shàngdì", 
	zh_content: "nǐ yào yòng nǐ de cáifù,
hé yīqiè chū shú de tǔchǎn, zūnchóng yēhéhuá;
zhèyàng, nǐ de cāngfáng bì chōngmǎn yǒuyú,
nǐ de jiǔ zhà bì yíng yì xīnjiǔ."});
// link content to node
MATCH (b:PASSAGE)
MATCH (c:CONTENT)
WHERE b.name = "passage.HONOR GOD" AND c.name = "content.HONOR GOD"
MERGE (b)-[:HAS_CONTENT {name: "b.edge.HONOR GOD"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:PASSAGE)
WHERE parent.name = "topic.WEALTH" AND child.name = "passage.HONOR GOD"
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.THE GODHEAD->HONOR GOD"}]->(child)
RETURN *;

```

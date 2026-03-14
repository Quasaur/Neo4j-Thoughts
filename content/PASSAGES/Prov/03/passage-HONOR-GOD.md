---
type: PASSAGE
name: "passage.HONOR GOD"
alias: "Passage: Add Offerings and Charity to your Budget"
parent: "topic.WEALTH"
en_content: |
  Honor the LORD from your wealth,
  And from the first of all your produce;  
  Then your barns will be filled with plenty,  
  And your vats will overflow with new wine."
tags: ["god", "wealth", "firstfruits", "plenty", "overflow"]
ptopic: "[[topic-WEALTH]]"
level: 3
neo4j: true
verified: false
---
```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.HONOR GOD",
    parent: "topic.WEALTH",
		alias: "Passage: Add Offerings and Charity to your Budget", 
		tags: ["god", "wealth", "firstfruits", "plenty", "overflow"], 
		source: "Proverbs 3:9,10",
		sortedsource: "Proverbs 03:09,10",
		biblelink: "https://www.biblegateway.com/passage/?search=proverbs+3%3A9-10&version=NASB",
		level: 3
})

CREATE (c:CONTENT {
    
    
	name: "content.HONOR GOD", 
	ctype: "PASSAGE",
	en_title: "Honor God", 
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
nǐ de jiǔ zhà bì yíng yì xīnjiǔ."

})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.HONOR GOD"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.WEALTH"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.WEALTH->HONOR GOD"
RETURN b, parent;
```

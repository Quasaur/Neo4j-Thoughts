---
type: PASSAGE
name: "passage.OBLIGATION"
alias: "Passage: Obligation"
parent: "topic.MORALITY"
sortedsource: "Proverbs 03:27-28"
en_content: "Do not withhold good from those to whom it is due, When it is in your power to do it. Do not say to your neighbor, 'Go, and come back, And tomorrow I will give it to you, When you have it with you."
tags: ["obligation", "due", "now", "bills", "morality"]
ptopic: "[[topic-MORALITY]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.OBLIGATION",
    parent: "topic.MORALITY",
    alias: "Passage: Obligation",
    tags: ["obligation", "due", "now", "bills", "morality"],
    source: "Proverbs 3:27,28",
    sortedsource: "Proverbs 03:27-28",
    biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%203%3A27-28&version=ESV",
    level: 3
})

CREATE (c:CONTENT {
    name: "content.OBLIGATION",
    ctype: "PASSAGE",
    en_title: "Passage: Obligation",
    en_content: "Do not withhold good from those to whom it is due,  
	When it is in your power to do it.  
	Do not say to your neighbor, 'Go, and come back,  
	And tomorrow I will give it to you,",
 es_title: "Pasaje: Obligación",
 es_content: "No niegues el bien a quien es debido, 
	Cuando esté en tu mano hacerlo. 
	No digas a tu prójimo: 'Ve y vuelve,'
	Y mañana te lo daré,
	Cuando lo tengas contigo.",
 fr_title: "Passage : Obligation",
 fr_content: "Ne refusez pas le bien à celui à qui il est dû, 
	Quand il est en votre pouvoir de le faire. 
	Ne dis pas à ton prochain : « Va et reviens, 
	Et demain je te le donnerai,",
 hi_title: "परिच्छेद: दायित्व",
 hi_content: "उन लोगों से भलाई न रोको जिनका यह हक़ है, 
	जब ऐसा करना आपके वश में हो। 
	अपने पड़ोसी से यह न कहना, 'जाओ, और लौट आओ, 
	और कल मैं इसे तुम्हें दे दूंगा,
	जब यह आपके पास हो.",
 zh_title: "duàn luò : yì wù",
 zh_content: "bú yào jù jué xiàng nà xiē yīng dé de rén tí gōng hǎo chù , dāng nǐ yǒu néng lì zuò dào zhè yì diǎn shí . bú yào duì nǐ de lín jū shuō :‘ zǒu ba , huí lái ba , míng tiān wǒ huì bǎ tā gěi nǐ , dāng nǐ yōng yǒu tā de shí hòu ."
})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.OBLIGATION"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.MORALITY->OBLIGATION"
RETURN b, parent;
```

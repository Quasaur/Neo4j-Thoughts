---
type: PASSAGE
name: "passage.THE SOURCE OF WEALTH"
alias: "Passage: God - The Source of Abundance!"
parent: "topic.WEALTH"
sortedsource: "Deuteronomy 08:18"
en_content: "But you are to remember the LORD your God, for it is He Who is giving you power to make wealth, in order to confirm His Covenant which He swore to your fathers, as it is this day."
tags: ["wealth", "gain", "god", "source", "power"]
ptopic: "[[topic-WEALTH]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.THE SOURCE OF WEALTH",
    parent: "topic.WEALTH",
  alias: "Passage: God - The Source of Abundance!", 
  tags: ["wealth", "gain", "god", "source", "power"], 
  source: "Deuteronomy 8:18",
  sortedsource: "Deuteronomy 08:18",
  biblelink: "https://www.biblegateway.com/passage/?search=Deuteronomy%208%3A18&version=NASB",
  level: 3
})

CREATE (c:CONTENT {
	name: "content.THE SOURCE OF WEALTH", 
	 ctype: "PASSAGE",
	 en_title: "Passage: God - The Source of Abundance!", 
	 en_content: "But you are to remember the LORD your God, for it is He Who is giving you power to make wealth, in order to confirm His Covenant which He swore to your fathers, as it is this day.", 
	 es_title: "Pasaje: Dios: ¡la fuente de la abundancia!",
	 es_content: "Pero acuérdate del Señor tu Dios, porque Él te da el poder para hacer las riquezas, a fin de confirmar su pacto que juró a tus padres, como en este día.", 
	 fr_title: "Passage : Dieu - La Source de l'Abondance !",
	 fr_content: "Mais vous vous souviendrez de l'Éternel, votre Dieu, car c'est lui qui vous donne la force de vous enrichir, afin de confirmer son alliance qu'il a jurée à vos pères, comme elle l'est aujourd'hui.", 
	 hi_title: "परिच्छेद: ईश्वर - प्रचुरता का स्रोत!",
	 hi_content: "परन्तु तुम्हें अपने परमेश्वर यहोवा को स्मरण रखना है, क्योंकि वही तुम्हें धन कमाने की शक्ति दे रहा है, ताकि वह अपनी उस वाचा को पूरा करे जो उसने तुम्हारे पूर्वजों से शपथ खाकर बाँधी थी, जैसा कि आज है।", 
	 zh_title: "jīng wén : shén -- fēng shèng de yuán quán !",
	 zh_content: "dàn nǐmen yào jìniàn yēhéhuá nǐmen de shén, yīn wéi dé cáifù de lìliàng shì tā gěi nǐmen de, wèi yào jiāndìng tā xiàng nǐmen zǔxiān qǐshì suǒ lì de yuē, xiàng jīnrì yīyàng."
})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.THE SOURCE OF WEALTH"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.WEALTH"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.WEALTH->THE SOURCE OF WEALTH"
RETURN b, parent;
```

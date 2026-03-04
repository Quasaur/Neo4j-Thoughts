---
type: THOUGHT
name: "thought.NOBODY"
alias: "Thought: Nobody"
parent: "topic.EVIL"
tags: ["depravity", "religion", "apostasy", "spirituality", "hell"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.NOBODY",
    alias: "Thought: Nobody",
    parent: "topic.EVIL",
    tags: ["depravity", "religion", "apostasy", "spirituality", "hell"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NOBODY",
    ctype: "THOUGHT",
    en_title: "Nobody",
 es_title: "NADIE",
 fr_title: "PERSONNE",
 hi_title: "कोई नहीं",
 zh_title: "wú rén",
    en_content: "",
 es_content: "Nadie quiere ir al infierno… ni al cielo. 
Es decir: aparte de la Gracia del Señor Jesucristo, mientras cualquier alma haría todo lo que esté en su poder (religión) para escapar del Lago de Fuego, ninguna alma tiene innatamente apetito (Fe) alguno por un DIOS Santo.",
 fr_content: "Personne ne veut aller en enfer… ou au paradis. 
C'est-à-dire : en dehors de la Grâce du Seigneur Jésus-Christ, alors que toute âme ferait tout ce qui est en son pouvoir (religion) pour échapper à l'étang de feu, aucune âme n'a innée un quelconque appétit (foi) pour un DIEU Saint.",
 hi_content: "कोई भी नरक या स्वर्ग नहीं जाना चाहता। 
कहने का तात्पर्य यह है: प्रभु यीशु मसीह की कृपा के अलावा, जबकि कोई भी आत्मा आग की झील से बचने के लिए अपनी शक्ति (धर्म) में सब कुछ करेगी, किसी भी आत्मा में पवित्र ईश्वर के लिए स्वाभाविक रूप से कोई भूख (विश्वास) नहीं होती है।",
 zh_content: "méi yǒu rén xiǎng qù dì yù …… huò tiān táng 。 
 yě jiù shì shuō ： chú le zhǔ yē sū jī dū de ēn diǎn ， suī rán rèn hé líng hún dū huì jié jìn quán lì （ zōng jiào ） táo lí huǒ hú ， dàn méi yǒu rèn hé líng hún tiān shēng duì shèng jié de shàng dì yǒu rèn hé xìng qù （ xìn yǎng ）。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOBODY" AND c.name = "content.NOBODY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.NOBODY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.NOBODY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->NOBODY"}]->(child);
```
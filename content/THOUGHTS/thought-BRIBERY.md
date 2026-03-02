---
type: THOUGHT
name: "thought.BRIBERY"
alias: "Thought: Bribery"
parent: "topic.EVIL"
tags: ["lobbying", "uscongress", "bribery", "justice", "oligarchy"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.BRIBERY",
    alias: "Thought: Bribery",
    parent: "topic.EVIL",
    tags: ["lobbying", "uscongress", "bribery", "justice", "oligarchy"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.BRIBERY",
    ctype: "THOUGHT",
    en_title: "Bribery",
 es_title: "Soborno",
 fr_title: "Corruption",
 hi_title: "रिश्वत",
 zh_title: "shòu huì",
    en_content: "",
 es_content: "En Estados Unidos, GASTAR DINERO es una forma de libertad de expresión protegida por la Constitución; 
por lo tanto, el SOBORNO (lobby), un pecado a los ojos de Dios, es legal en los Estados Unidos.
PD. 26:9-10; 1 Sam. 8:3; Amós 5:12; Deut. 16:29; Ex. 23:8; Prov. 17:23.",
 fr_content: "En Amérique, DÉPENSER L’ARGENT est une forme de liberté d’expression protégée par la Constitution ; 
par conséquent, la CORRUPTION (lobbying), un péché aux yeux de Dieu, est légale aux États-Unis.
Ps. 26:9-10 ; 1 Sam. 8:3 ; Amos 5:12 ; Deut. 16h29 ; Ex. 23:8 ; Prov. 17h23.",
 hi_content: "अमेरिका में पैसा खर्च करना संविधान द्वारा संरक्षित अभिव्यक्ति की स्वतंत्रता का एक रूप है; 
इसलिए रिश्वत (लॉबिंग), भगवान की दृष्टि में एक पाप, संयुक्त राज्य अमेरिका में कानूनी है।
पी.एस. 26:9-10; 1 सैम. 8:3; आमोस 5:12; Deut. 16:29; पूर्व। 23:8; प्रोव. 17:23.",
 zh_content: "zài měi guó ， huā qián shì yán lùn zì yóu de yī zhǒng xíng shì ， shòu xiàn fǎ bǎo hù ； 
 yīn cǐ ， huì lù （ yóu shuì ） zài shàng dì kàn lái shì yī zhǒng zuì guò ， dàn zài měi guó què shì hé fǎ de 。
 shī 。 26:9-10； 1  sà mǔ . 8:3; ā mó sī shū  5:12； shēn mìng jì 。 16:29； qián rèn 。 23:8； shěng 。 17:23。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BRIBERY" AND c.name = "content.BRIBERY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.BRIBERY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.BRIBERY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->BRIBERY"}]->(child);
```
---
type: THOUGHT
name: "thought.ANTI SEMITISM"
alias: "Thought: Anti-semitism"
parent: "topic.PSYCHOLOGY"
en_content: |
  # Thought: ANTI-SEMITISM
  It is IMPOSSIBLE to truly love The Lord Jesus Christ and simultaneously hate the Jew. GOD NEVER told any Christian to persecute or punish the Jew; nor would GOD condone any white Christian oppressing, marginalizing or murdering the black man.
tags: ["antisemitism", "antinegro", "antijew", "antiblack", "jesus_christ"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ANTI SEMITISM",
    alias: "Thought: Anti-semitism",
    parent: "topic.PSYCHOLOGY",
    tags: ["antisemitism", "antinegro", "antijew", "antiblack", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANTI SEMITISM",
    ctype: "THOUGHT",
    en_title: "Anti-semitism",
    en_content: "# Thought: ANTI-SEMITISM
It is IMPOSSIBLE to truly love The Lord Jesus Christ and simultaneously hate the Jew. GOD NEVER told any Christian to persecute or punish the Jew; nor would GOD condone any white Christian oppressing, marginalizing or murdering the black man.",
    es_title: "ANTISEMITISMO",
    es_content: "# Pensamiento: ANTISEMITISMO
Es IMPOSIBLE amar verdaderamente al Señor Jesucristo y al mismo tiempo odiar al judío. DIOS NUNCA le dijo a ningún cristiano que persiguiera o castigara al judío; ni DIOS toleraría que ningún cristiano blanco oprima, margine o asesine al hombre negro.",
    fr_title: "ANTISÉMITISME",
    fr_content: "# Pensée : ANTI-SÉMITISME
Il est IMPOSSIBLE d’aimer vraiment le Seigneur Jésus-Christ et en même temps de haïr les Juifs. DIEU n'a JAMAIS dit à aucun chrétien de persécuter ou de punir les Juifs ; DIEU ne tolérerait pas non plus qu’un chrétien blanc opprime, marginalise ou assassine l’homme noir.",
    hi_title: "यहूदी विरोधी भावना",
    hi_content: "# विचार: यहूदी विरोधी भावना
प्रभु यीशु मसीह से सच्चा प्यार करना और साथ ही यहूदी से नफरत करना असंभव है। परमेश्वर ने कभी भी किसी ईसाई को यहूदी पर अत्याचार करने या दंडित करने के लिए नहीं कहा; न ही ईश्वर किसी श्वेत ईसाई को काले आदमी पर अत्याचार करने, हाशिए पर धकेलने या उसकी हत्या करने से मना करेगा।",
    zh_title: "fǎn yóu tài zhǔ yì",
    zh_content: "#  sī xiǎng ： fǎn yóu tài zhǔ yì 
 zhēn zhèng ài zhǔ yē sū jī dū de tóng shí yòu hèn yóu tài rén shì bù kě néng de 。 shàng dì cóng wèi gào sù rèn hé jī dū tú pò hài huò chéng fá yóu tài rén ； shàng dì yě bú huì kuān shù rèn hé bái rén jī dū tú yā pò 、 biān yuán huà huò móu shā hēi rén 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ANTI SEMITISM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->ANTI SEMITISM"
RETURN t, parent;
```

---
name: "thought.ANTI_SEMITISM"
alias: "Thought: ANTI-SEMITISM"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- antisemitism
- antinegro
- antijew
- antiblack
- jesuschrist
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ANTI_SEMITISM",
    alias: "Thought: ANTI-SEMITISM",
    parent: "topic.PSYCHOLOGY",
    tags: ["antisemitism", "antinegro", "antijew", "antiblack", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANTI_SEMITISM",
    en_title: "ANTI-SEMITISM",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANTI_SEMITISM" AND c.name = "content.ANTI_SEMITISM"
MERGE (t)-[:HAS_CONTENT {name: "edge.ANTI_SEMITISM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.ANTI_SEMITISM"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->ANTI_SEMITISM"}]->(child);
```

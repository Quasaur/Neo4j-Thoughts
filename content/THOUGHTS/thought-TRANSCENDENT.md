---
type: THOUGHT
name: "thought.TRANSCENDENT"
alias: "Thought: Transcendent"
parent: "topic.GRACE"
tags: ["pure", "untainted", "deliverance", "glorification", "jesus_christ"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TRANSCENDENT",
    alias: "Thought: Transcendent",
    parent: "topic.GRACE",
    tags: ["pure", "untainted", "deliverance", "glorification", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TRANSCENDENT",
    ctype: "THOUGHT",
    en_title: "Transcendent",
 es_title: "TRASCENDENTE",
 fr_title: "TRANSCENDANT",
 hi_title: "उत्कृष्ट",
 zh_title: "chāo yuè",
    en_content: "",
 es_content: "Lo que hace que DIOS sea tan invaluable, tan precioso y tan digno de asombro y adoración… no es solo Su inmunidad a la corrupción: ¡¡¡ÉL PUEDE INFECTAR LA CORRUPCIÓN CON SANTIDAD, haciendo que la corrupción misma sea INCORRUPTIBLE!!!!!!",
 fr_content: "Ce qui rend DIEU si inestimable, si précieux et si digne de respect et d'adoration… n'est pas seulement Son immunité contre la corruption : IL PEUT INFECTER LA CORRUPTION DE SAINTETÉ, rendant la corruption elle-même INCORRUPTIBLE !!!!!!",
 hi_content: "जो चीज़ ईश्वर को इतना अमूल्य, इतना मूल्यवान और विस्मय और पूजा के योग्य बनाती है... वह न केवल भ्रष्टाचार के प्रति उसकी प्रतिरक्षा है: वह भ्रष्टाचार को पवित्रता से संक्रमित कर सकता है, भ्रष्टाचार को स्वयं अविनाशी बना सकता है!!!!!!",
 zh_content: "shén zhī suǒ yǐ rú cǐ wú jià 、 rú cǐ bǎo guì 、 rú cǐ zhí de jìng wèi hé chóng bài …… bù jǐn shì yīn wèi tā duì fǔ bài jù yǒu miǎn yì lì ： tā kě yǐ yòng shèng jié gǎn rǎn fǔ bài ， shǐ fǔ bài běn shēn biàn dé bù xiǔ ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRANSCENDENT" AND c.name = "content.TRANSCENDENT"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.TRANSCENDENT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.TRANSCENDENT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->TRANSCENDENT"}]->(child);
```
---
type: THOUGHT
name: "thought.LOVE"
alias: "Thought: Love"
parent: "topic.LOVE"
tags: ["love", "spirit", "attitude", "selfless", "generosity"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LOVE",
    alias: "Thought: Love",
    parent: "topic.LOVE",
    tags: ["love", "spirit", "attitude", "selfless", "generosity"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOVE",
    ctype: "THOUGHT",
    en_title: "Love",
 es_title: "AMAR",
 fr_title: "AMOUR",
 hi_title: "प्यार",
 zh_title: "ài",
    en_content: "",
 es_content: "El amor es mucho más que un simple sentimiento... ¡Es una decisión de tratar a alguien tan bien o mejor de lo que te tratas a ti mismo!",
 fr_content: "L'amour est bien plus qu'un simple sentiment... C'est une décision de traiter quelqu'un aussi bien, voire mieux, que vous-même !",
 hi_content: "प्यार महज़ एक एहसास से कहीं ज़्यादा है...यह किसी के साथ उतना ही अच्छा या उससे बेहतर व्यवहार करने का निर्णय है जितना आप अपने साथ करते हैं!",
 zh_content: "ài bù jǐn jǐn shì yī zhǒng gǎn jué …… tā shì yí gè jué dìng ， duì dài mǒu rén jiù xiàng duì dài zì jǐ yī yàng hǎo ， shèn zhì gèng hǎo ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVE" AND c.name = "content.LOVE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.LOVE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LOVE" AND child.name = "thought.LOVE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.LOVE->LOVE"}]->(child);
```
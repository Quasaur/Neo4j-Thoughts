---
type: THOUGHT
name: "thought.LOVE2"
alias: "Thought: LOVE 2"
parent: "topic.LOVE"
tags: ["love", "sacrificial", "give", "selfless", "cause"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LOVE2",
    alias: "Thought: LOVE 2",
    parent: "topic.LOVE",
    tags: ["love", "sacrificial", "give", "selfless", "cause"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOVE2",
    ctype: "THOUGHT",
    en_title: "LOVE 2",
 es_title: "AMOR 2",
 fr_title: "AMOUR 2",
 hi_title: "प्यार 2",
 zh_title: "ài 2",
    en_content: "",
 es_content: "¿Qué te impulsa a entregarte a una causa más grande que tú? AMAR.",
 fr_content: "Qu’est-ce qui vous pousse à vous consacrer à une cause plus grande que vous ? AMOUR.",
 hi_content: "कौन सी चीज़ आपको अपने आप को अपने से बड़े उद्देश्य के लिए समर्पित करने के लिए प्रेरित करती है? प्यार।",
 zh_content: "shì shén me qū shǐ nǐ quán shēn xīn tóu rù dào bǐ nǐ gèng wěi dà de shì yè zhōng ？ ài 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVE2" AND c.name = "content.LOVE2"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.LOVE2"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LOVE" AND child.name = "thought.LOVE2"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.LOVE->LOVE2"}]->(child);
```
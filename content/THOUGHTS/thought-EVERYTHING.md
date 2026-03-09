---
type: THOUGHT
name: "thought.EVERYTHING"
alias: "Thought: Everything"
parent: "topic.CREATION"
tags: ["god", "creator", "all", "kingdom", "cosmos"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.EVERYTHING",
    alias: "Thought: Everything",
    parent: "topic.CREATION",
    tags: ["god", "creator", "all", "kingdom", "cosmos"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EVERYTHING",
    ctype: "THOUGHT",
    en_title: "Everything",
 es_title: "TODO",
 fr_title: "TOUT",
 hi_title: "सब कुछ",
 zh_title: "yī qiè",
    en_content: "",
 es_content: "¡Fue el Acto supremo de Humildad para Dios, que no necesita nada, para crearlo todo!",
 fr_content: "C'était l'acte suprême d'humilité pour Dieu, qui n'a besoin de rien, pour tout créer !",
 hi_content: "यह ईश्वर के लिए विनम्रता का सर्वोच्च कार्य था, जिसे सब कुछ बनाने के लिए किसी चीज़ की आवश्यकता नहीं है!",
 zh_content: "zhè shì shàng dì zuì gāo de qiān bēi xíng wéi ， tā bù xū yào rèn hé dōng xī ， jiù chuàng zào le yī qiè ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVERYTHING" AND c.name = "content.EVERYTHING"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.EVERYTHING"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.EVERYTHING"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.CREATION->EVERYTHING"}]->(child);
```
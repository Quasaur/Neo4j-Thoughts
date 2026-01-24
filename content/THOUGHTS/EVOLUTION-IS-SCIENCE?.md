---
name: "thought.EVOLUTION_IS_SCIENCE?"
alias: "Thought: EVOLUTION IS SCIENCE?"
type: THOUGHT
parent: topic.RELIGION
tags:
- evolution
- science
- religion
- evidence
- faith
neo4j: true
ptopic: "[[topic-RELIGION]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.EVOLUTION_IS_SCIENCE?",
    alias: "Thought: EVOLUTION IS SCIENCE?",
    parent: "topic.RELIGION",
    tags: ["evolution", "science", "religion", "evidence", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVOLUTION_IS_SCIENCE?",
    en_title: "EVOLUTION IS SCIENCE?",
    en_content: "To equate science and evolution (considering the MOUNTAIN of evidence against evolution) would be premature, I think!",
    es_title: "¿LA EVOLUCIÓN ES CIENCIA?",
    es_content: "¡Creo que equiparar ciencia y evolución (teniendo en cuenta la MONTAÑA de evidencia contra la evolución) sería prematuro!",
    fr_title: "L'ÉVOLUTION EST-ELLE SCIENCE ?",
    fr_content: "Assumer science et évolution (compte tenu de la MONTAGNE de preuves contre l’évolution) serait prématuré, je pense !",
    hi_title: "विकास विज्ञान है?",
    hi_content: "मुझे लगता है कि विज्ञान और विकास को समान मानना ​​(विकास के विरुद्ध साक्ष्य के पहाड़ पर विचार करना) जल्दबाजी होगी!",
    zh_title: "jìn huà lùn shì kē xué ma ？",
    zh_content: "wǒ rèn wéi ， jiāng kē xué yǔ jìn huà lùn děng tóng qǐ lái （ kǎo lǜ dào fǎn duì jìn huà lùn de dà liàng zhèng jù ） hái wéi shí guò zǎo ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVOLUTION_IS_SCIENCE?" AND c.name = "content.EVOLUTION_IS_SCIENCE?"
MERGE (t)-[:HAS_CONTENT {name: "edge.EVOLUTION_IS_SCIENCE?"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.EVOLUTION_IS_SCIENCE?"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.RELIGION->EVOLUTION_IS_SCIENCE?"}]->(child);
```

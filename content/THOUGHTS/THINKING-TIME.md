---
name: "thought.THINKING_TIME"
alias: "Thought: THINKING TIME"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- thinking
- time
- focus
- priorities
- god
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THINKING_TIME",
    alias: "Thought: THINKING TIME",
    parent: "topic.PSYCHOLOGY",
    tags: ["thinking", "time", "focus", "priorities", "god"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THINKING_TIME",
    en_title: "THINKING TIME",
    en_content: "God spends 100% of His Time thinking about us...how much time do we spend thinking about Him?",
    es_title: "TIEMPO PARA PENSAR",
    es_content: "Dios pasa el 100% de Su Tiempo pensando en nosotros... ¿cuánto tiempo pasamos nosotros pensando en Él?",
    fr_title: "TEMPS DE RÉFLEXION",
    fr_content: "Dieu passe 100 % de son temps à penser à nous... combien de temps passons-nous à penser à lui ?",
    hi_title: "सोचने का समय",
    hi_content: "भगवान अपना 100% समय हमारे बारे में सोचने में बिताते हैं... हम उनके बारे में सोचने में कितना समय बिताते हैं?",
    zh_title: "sī kǎo shí jiān",
    zh_content: "shàng dì yòng  100%  de shí jiān sī kǎo wǒ men …… wǒ men huā le duō shǎo shí jiān sī kǎo tā ？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THINKING_TIME" AND c.name = "content.THINKING_TIME"
MERGE (t)-[:HAS_CONTENT {name: "edge.THINKING_TIME"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.THINKING_TIME"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->THINKING_TIME"}]->(child);
```

---
name: "thought.SHOVING SUGAR BODY"
alias: "Thought: Shoving Sugar Body"
type: THOUGHT
en_content: "We keep shoving sugar into a body that itself manufactures sugar and then wonder why we get diabetes!"
parent: "topic.MORALITY"
tags:
- sugar
- health
- body
- diabetes
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.SHOVING SUGAR BODY",
    alias: "Thought: Shoving Sugar Body",
    parent: "topic.MORALITY",
    tags: ['sugar', 'health', 'body', 'diabetes', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SHOVING SUGAR BODY",
    en_title: "Shoving Sugar Body",
    en_content: "We keep shoving sugar into a body that itself manufactures sugar and then wonder why we get diabetes!",
    es_title: "Empujando Azúcar al Cuerpo",
    es_content: "¡Seguimos empujando azúcar a un cuerpo que él mismo manufactura azúcar y luego nos preguntamos por qué contraemos diabetes!",
    fr_title: "Bourrer le Corps de Sucre",
    fr_content: "Nous continuons à bourrer de sucre un corps qui fabrique lui-même du sucre, puis nous nous demandons pourquoi nous attrapons le diabète !",
    hi_title: "शरीर में चीनी ठूंसना",
    hi_content: "हम एक ऐसे शरीर में चीनी ठूंसते रहते हैं जो खुद ही चीनी बनाता है और फिर आश्चर्य करते हैं कि हमें मधुमेह क्यों हो जाता है!",
    zh_title: "Wang Shenti Li Sai Tang",
    zh_content: "Women bu duan wang yi ge ben shen jiu neng zhi zao tang de shenti li sai tang, ran hou you qi guai wei shenme women de le tang niao bing!"
});

MATCH (t:THOUGHT {name: "thought.SHOVING SUGAR BODY"})
MATCH (c:CONTENT {name: "content.SHOVING SUGAR BODY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHOVING SUGAR BODY" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.SHOVING SUGAR BODY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SHOVING SUGAR BODY" }]->(child);
```

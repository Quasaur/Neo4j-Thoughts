---
type: THOUGHT
name: "thought.GIANT BALL OF ROCK"
alias: "Thought: Giant Ball Of Rock"
parent: "topic.CREATION"
en_content: "We are living on a GIANT BALL OF ROCK...God is great!"
tags: ["creation", "earth", "perspective", "power", "majesty"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2011b)
CREATE (t:THOUGHT {    name: "thought.GIANT BALL OF ROCK",
    alias: "Thought: Giant Ball Of Rock",
    parent: "topic.CREATION",
    tags: ['creation', 'earth', 'perspective', 'power', 'majesty'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.GIANT BALL OF ROCK",
    ctype: "THOUGHT",
    en_title: "Giant Ball Of Dirt",
    en_content: "We are living on a GIANT BALL OF ROCK...God is great!",
    es_title: "Bola Gigante de Tierra",
    es_content: "Estamos viviendo en una BOLA GIGANTE DE TIERRA...¡Dios es grande!",
    fr_title: "Boule Géante de Terre",
    fr_content: "Nous vivons sur une BOULE GÉANTE DE TERRE...Dieu est grand!",
    hi_title: "मिट्टी का विशाल गोला",
    hi_content: "हम मिट्टी के एक विशाल गोले पर रह रहे हैं...भगवान महान हैं!",
    zh_title: "Ju Da De Tu Qiu",
    zh_content: "Wo men sheng huo zai yi ge JU DA DE TU QIU shang...Shang Di shi wei da de!"
});

MATCH (t:THOUGHT {name: "thought.GIANT BALL OF ROCK"})
MATCH (c:CONTENT {name: "content.GIANT BALL OF ROCK"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GIANT BALL OF DIRT" }]->(c);

MATCH (parent:TOPIC {name: "topic.CREATION"})
MATCH (child:THOUGHT {name: "thought.GIANT BALL OF ROCK"})
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION->GIANT BALL OF ROCK" }]->(child);
```

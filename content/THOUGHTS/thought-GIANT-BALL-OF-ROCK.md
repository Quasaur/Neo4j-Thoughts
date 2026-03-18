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
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GIANT BALL OF ROCK",
    alias: "Thought: Giant Ball Of Rock",
    parent: "topic.CREATION",
    tags: ['creation', 'earth', 'perspective', 'power', 'majesty'],
    level: 2
});

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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GIANT BALL OF ROCK"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->GIANT BALL OF ROCK"
RETURN t, parent;
```

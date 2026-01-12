---
name: "thought.GIANT BALL OF DIRT"
alias: "Thought: Giant Ball Of Dirt"
type: THOUGHT
en_content: "We are living on a GIANT BALL OF DIRT...God is great!"
parent: "topic.CREATION"
tags:
- creation
- earth
- perspective
- power
- majesty
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.GIANT BALL OF DIRT",
    alias: "Thought: Giant Ball Of Dirt",
    parent: "topic.CREATION",
    tags: ['creation', 'earth', 'perspective', 'power', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GIANT BALL OF DIRT",
    en_title: "Giant Ball Of Dirt",
    en_content: "We are living on a GIANT BALL OF DIRT...God is great!",
    es_title: "Bola Gigante de Tierra",
    es_content: "Estamos viviendo en una BOLA GIGANTE DE TIERRA...¡Dios es grande!",
    fr_title: "Boule Géante de Terre",
    fr_content: "Nous vivons sur une BOULE GÉANTE DE TERRE...Dieu est grand!",
    hi_title: "मिट्टी का विशाल गोला",
    hi_content: "हम मिट्टी के एक विशाल गोले पर रह रहे हैं...भगवान महान हैं!",
    zh_title: "Ju Da De Tu Qiu",
    zh_content: "Wo men sheng huo zai yi ge JU DA DE TU QIU shang...Shang Di shi wei da de!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GIANT BALL OF DIRT" AND c.name = "content.GIANT BALL OF DIRT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GIANT BALL OF DIRT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.GIANT BALL OF DIRT"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >GIANT BALL OF DIRT" }]->(child);
```

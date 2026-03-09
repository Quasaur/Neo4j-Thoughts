---
type: THOUGHT
name: "thought.EARTH SPEED SPACE"
alias: "Thought: Earth Speed Space"
parent: "topic.ASTROPHYSICS"
en_content: "The Earth is tearing thru space at over 667,000 MPH, and we're not dead ...God is great!"
tags: ["creation", "science", "earth", "speed", "majesty"]
ptopic: "topic-ASTROPHYSICS"
level: 5
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2011c)
CREATE (t:THOUGHT {    name: "thought.EARTH SPEED SPACE",
    alias: "Thought: Earth Speed Space",
    parent: "topic.ASTROPHYSICS",
    tags: ['creation', 'science', 'earth', 'speed', 'majesty'],
    level: 5});

CREATE (c:CONTENT {
    name: "content.EARTH SPEED SPACE",
    ctype: "THOUGHT",
    en_title: "Thought: Earth Speed Space",
    en_content: "The Earth is tearing thru space at over 667,000 MPH, and we're not dead ...God is great!",
    es_title: "Pensamiento: Tierra Velocidad Espacio",
    es_content: "La Tierra está desgarrando el espacio a más de 667,000 MPH, y no estamos muertos... ¡Dios es grande!",
    fr_title: "Pensée : Terre Vitesse Espace",
    fr_content: "La Terre fonce à travers l'espace à plus de 667 000 MPH, et nous ne sommes pas morts... Dieu est grand !",
    hi_title: "विचार: पृथ्वी गति अंतरिक्ष",
    hi_content: "पृथ्वी अंतरिक्ष में 667,000 MPH से अधिक गति से दौड़ रही है, और हम मरे नहीं हैं... भगवान महान है!",
    zh_title: "sī xiǎng : dì qiú sù dù kōng jiān",
    zh_content: "Di qiu zheng yi chao guo 667,000 MPH de su du chuan yue tai kong, er wo men mei you si... Shang di shi wei da de!"
});

MATCH (t:THOUGHT {name: "thought.EARTH SPEED SPACE"})
MATCH (c:CONTENT {name: "content.EARTH SPEED SPACE"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.EARTH SPEED SPACE" }]->(c);

MATCH (parent:TOPIC {name: "topic.ASTROPHYSICS"})
MATCH (child:THOUGHT {name: "thought.EARTH SPEED SPACE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.ASTROPHYSICS->EARTH SPEED SPACE" }]->(child);
```

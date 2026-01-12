---
name: "thought.EARTH SPEED SPACE"
alias: "Thought: Earth Speed Space"
type: THOUGHT
en_content: "The Earth is tearing thru space at over 667,000 MPH, and we're not dead ...God is great!"
parent: "topic.CREATION"
tags:
- creation
- science
- earth
- speed
- majesty
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2011c)
CREATE (t:THOUGHT {
    name: "thought.EARTH SPEED SPACE",
    alias: "Thought: Earth Speed Space",
    parent: "topic.CREATION",
    tags: ['creation', 'science', 'earth', 'speed', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EARTH SPEED SPACE",
    en_title: "Earth Speed Space",
    en_content: "The Earth is tearing thru space at over 667,000 MPH, and we're not dead ...God is great!",
    es_title: "Velocidad Terrestre Espacial",
    es_content: "La Tierra está desgarrando el espacio a más de 667,000 MPH, y no estamos muertos... ¡Dios es grande!",
    fr_title: "Vitesse Terrestre Spatiale",
    fr_content: "La Terre fonce à travers l'espace à plus de 667 000 MPH, et nous ne sommes pas morts... Dieu est grand !",
    hi_title: "पृथ्वी गति अंतरिक्ष",
    hi_content: "पृथ्वी अंतरिक्ष में 667,000 MPH से अधिक गति से दौड़ रही है, और हम मरे नहीं हैं... भगवान महान है!",
    zh_title: "Di Qiu Su Du Kong Jian",
    zh_content: "Di qiu zheng yi chao guo 667,000 MPH de su du chuan yue tai kong, er wo men mei you si... Shang di shi wei da de!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EARTH SPEED SPACE" AND c.name = "content.EARTH SPEED SPACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EARTH SPEED SPACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.EARTH SPEED SPACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >EARTH SPEED SPACE" }]->(child);
```

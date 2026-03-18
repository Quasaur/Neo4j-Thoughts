---
type: THOUGHT
name: "thought.OBLIVION"
alias: "Thought: Oblivion"
parent: "topic.HISTORY"
en_content: |
  # OBLIVION
  The Lord Jesus said that humanity would be driven to the edge of extinction before He returns…and Jesus never lies."
tags: ["apocalypse", "ele", "extinction", "oblivion", "thelastday"]
ptopic: "[[topic-HISTORY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "\"thought.OBLIVION\"",
    alias: "Thought: Oblivion",
    parent: "\"topic.HISTORY\"",
    tags: ["apocalypse", "ele", "extinction", "oblivion", "thelastday"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.OBLIVION",
    ctype: "THOUGHT",
    en_title: "Oblivion",
    en_content: "# OBLIVION
The Lord Jesus said that humanity would be driven to the edge of extinction before He returns…and Jesus never lies.",
    es_title: "OLVIDO",
    es_content: "#OLVIDO
El Señor Jesús dijo que la humanidad estaría al borde de la extinción antes de que Él regrese... y Jesús nunca miente.",
    fr_title: "OUBLI",
    fr_content: "# OBLIVION
Le Seigneur Jésus a dit que l’humanité serait conduite au bord de l’extinction avant son retour… et Jésus ne ment jamais.",
    hi_title: "विस्मरण",
    hi_content: "# विस्मृति
प्रभु यीशु ने कहा था कि उनके लौटने से पहले मानवता विलुप्त होने के कगार पर पहुंच जाएगी... और यीशु कभी झूठ नहीं बोलते।",
    zh_title: "yí wàng",
    zh_content: "#  yí wàng 
 zhǔ yē sū shuō ， zài tā zài lái zhī qián ， rén lèi jiāng bèi bī dào miè jué de biān yuán …… yē sū cóng lái bù shuō huǎng 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.'"thought.OBLIVION"'"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HISTORY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HISTORY->OBLIVION"thought.OBLIVION"'"
RETURN t, parent;
```

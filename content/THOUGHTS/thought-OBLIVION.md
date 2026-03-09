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
CREATE (t:THOUGHT {
    name: '"thought.OBLIVION"',
    alias: "Thought: Oblivion",
    parent: '"topic.HISTORY"',
    tags: ["apocalypse", "ele", "extinction", "oblivion", "thelastday"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.OBLIVION",
    ctype: "THOUGHT",
    en_title: "Oblivion",
 es_title: "OLVIDO",
 fr_title: "OUBLI",
 hi_title: "विस्मरण",
 zh_title: "yí wàng",
    en_content: "# OBLIVION
The Lord Jesus said that humanity would be driven to the edge of extinction before He returns…and Jesus never lies.",
 es_content: "#OLVIDO
El Señor Jesús dijo que la humanidad estaría al borde de la extinción antes de que Él regrese... y Jesús nunca miente.",
 fr_content: "# OBLIVION
Le Seigneur Jésus a dit que l’humanité serait conduite au bord de l’extinction avant son retour… et Jésus ne ment jamais.",
 hi_content: "# विस्मृति
प्रभु यीशु ने कहा था कि उनके लौटने से पहले मानवता विलुप्त होने के कगार पर पहुंच जाएगी... और यीशु कभी झूठ नहीं बोलते।",
 zh_content: "#  yí wàng 
 zhǔ yē sū shuō ， zài tā zài lái zhī qián ， rén lèi jiāng bèi bī dào miè jué de biān yuán …… yē sū cóng lái bù shuō huǎng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = '"thought.OBLIVION"' AND c.name = "content.OBLIVION"
MERGE (t)-[:HAS_CONTENT {name: "edge.OBLIVION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = '"topic.HISTORY"' AND child.name = '"thought.OBLIVION"'
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HISTORY->OBLIVION"}]->(child);
```
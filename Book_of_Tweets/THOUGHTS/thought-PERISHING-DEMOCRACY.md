---
type: THOUGHT
name: "thought.PERISHING DEMOCRACY"
alias: "Thought: Perishing Democracy"
parent: "topic.MORALITY"
en_content: "Government of, by and for the People is perishing from the Earth!"
tags: ["government", "democracy", "perishing", "society", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2013b)
CREATE (t:THOUGHT {    name: "thought.PERISHING DEMOCRACY",
    alias: "Thought: Perishing Democracy",
    parent: "topic.MORALITY",
    tags: ['government', 'democracy', 'perishing', 'society', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.PERISHING DEMOCRACY",
    ctype: "THOUGHT",
    en_title: "Perishing Democracy",
    en_content: "Government of, by and for the People is perishing from the Earth!",
    es_title: "Democracia que Perece",
    es_content: "¡El gobierno del pueblo, por el pueblo y para el pueblo está pereciendo de la Tierra!",
    fr_title: "Démocratie qui Périt",
    fr_content: "Le gouvernement du peuple, par le peuple et pour le peuple disparaît de la Terre !",
    hi_title: "नष्ट होती लोकतंत्र",
    hi_content: "जनता की, जनता के द्वारा और जनता के लिए सरकार पृथ्वी से नष्ट हो रही है!",
    zh_title: "Xiaoshi de Minzhu",
    zh_content: "Min you, min zhi, min xiang de zhengfu zheng zai cong diqiu shang xiaoshi!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PERISHING DEMOCRACY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->PERISHING DEMOCRACY"
RETURN t, parent;
```

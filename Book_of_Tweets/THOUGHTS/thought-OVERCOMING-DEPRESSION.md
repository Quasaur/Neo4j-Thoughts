---
type: THOUGHT
name: "thought.OVERCOMING DEPRESSION"
alias: "Thought: Overcoming Depression"
parent: "topic.PSYCHOLOGY"
en_content: "Long after the point when Depression ceases to be a memory...I will still be here."
tags: ["depression", "healing", "persistence", "psychology", "hope"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2011a)
CREATE (t:THOUGHT {    name: "thought.OVERCOMING DEPRESSION",
    alias: "Thought: Overcoming Depression",
    parent: "topic.PSYCHOLOGY",
    tags: ['depression', 'healing', 'persistence', 'psychology', 'hope'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.OVERCOMING DEPRESSION",
    ctype: "THOUGHT",
    en_title: "Overcoming Depression",
    en_content: "Long after the point when Depression ceases to be a memory...I will still be here.",
    es_title: "Venciendo la Depresión",
    es_content: "Mucho después del momento cuando la Depresión deje de ser un recuerdo...yo todavía estaré aquí.",
    fr_title: "Surmonter la Dépression",
    fr_content: "Bien après le moment où la Dépression cessera d'être un souvenir...je serai encore là.",
    hi_title: "अवसाद पर विजय",
    hi_content: "जब अवसाद एक स्मृति भी नहीं रह जाएगा, उसके बहुत समय बाद भी...मैं अभी भी यहाँ होऊंगा।",
    zh_title: "Kèfú Yìyùzhèng",
    zh_content: "Dāng Yìyùzhèng bù zài shì huíyì hěn jiǔ zhīhòu...wǒ réng jiāng zài zhèlǐ."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.OVERCOMING DEPRESSION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->OVERCOMING DEPRESSION"
RETURN t, parent;
```

---
name: "thought.OVERCOMING DEPRESSION"
alias: "Thought: Overcoming Depression"
type: THOUGHT
en_content: "Long after the point when Depression ceases to be a memory...I will still be here."
parent: "topic.PSYCHOLOGY"
tags:
- depression
- healing
- persistence
- psychology
- hope
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2011a)
CREATE (t:THOUGHT {
    name: "thought.OVERCOMING DEPRESSION",
    alias: "Thought: Overcoming Depression",
    parent: "topic.PSYCHOLOGY",
    tags: ['depression', 'healing', 'persistence', 'psychology', 'hope'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.OVERCOMING DEPRESSION",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.OVERCOMING DEPRESSION" AND c.name = "content.OVERCOMING DEPRESSION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OVERCOMING DEPRESSION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.OVERCOMING DEPRESSION"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >OVERCOMING DEPRESSION" }]->(child);
```

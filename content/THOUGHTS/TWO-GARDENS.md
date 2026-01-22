---
name: "thought.TWO GARDENS"
alias: "Thought: Two Gardens"
type: THOUGHT
en_content: "In the Bible there are 2 gardens. In the 1st garden are 2 trees; in the 2nd garden is only 1 tree. What happened to the 2nd tree?"
parent: "topic.SOTERIOLOGY"
tags:
- bible
- creation
- eden
- paradise
- symbolism
level: 3
neo4j: true
ptopic: "[[topic-SOTERIOLOGY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Feb-2011)
CREATE (t:THOUGHT {
    name: "thought.TWO GARDENS",
    alias: "Thought: Two Gardens",
    parent: "topic.STOERIOLOGY",
    tags: ['bible', 'creation', 'eden', 'paradise', 'symbolism'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TWO GARDENS",
    en_title: "Two Gardens",
    en_content: "In the Bible there are 2 gardens. In the 1st garden are 2 trees; in the 2nd garden is only 1 tree. What happened to the 2nd tree?",
    es_title: "Dos Jardines",
    es_content: "En la Biblia hay 2 jardines. En el primer jardín hay 2 árboles; en el segundo jardín hay solo 1 árbol. ¿Qué pasó con el segundo árbol?",
    fr_title: "Deux Jardins",
    fr_content: "Dans la Bible il y a 2 jardins. Dans le 1er jardin il y a 2 arbres ; dans le 2ème jardin il n'y a qu'1 arbre. Qu'est-il arrivé au 2ème arbre ?",
    hi_title: "दो बगीचे",
    hi_content: "बाइबल में 2 बगीचे हैं। पहले बगीचे में 2 पेड़ हैं; दूसरे बगीचे में केवल 1 पेड़ है। दूसरे पेड़ का क्या हुआ?",
    zh_title: "Liǎng gè yuánzi",
    zh_content: "Zài Shèngjīng zhōng yǒu 2 gè yuánzi. Zài dì 1 gè yuánzi lǐ yǒu 2 kē shù; zài dì 2 gè yuánzi lǐ zhǐyǒu 1 kē shù. Dì 2 kē shù fāshēng le shénme?"
});

MATCH (t:THOUGHT {name: "thought.TWO GARDENS"})
MATCH (c:CONTENT {name: "content.TWO GARDENS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.TWO GARDENS" }]->(c);

MATCH (parent:TOPIC {name: "topic.SOTERIOLOGY"})
MATCH (child:THOUGHT {name: "thought.TWO GARDENS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SOTERIOLOGY->TWO GARDENS" }]->(child);
```

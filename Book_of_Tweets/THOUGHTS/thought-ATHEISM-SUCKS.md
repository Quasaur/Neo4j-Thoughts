---
type: THOUGHT
name: "thought.ATHEISM SUCKS"
alias: "Thought: Atheism Sucks"
parent: "topic.PHILOSOPHY"
en_content: "The problem with believing you're a thing is that you'll start treating other people as things. Atheism sucks!"
tags: ["atheism", "philosophy", "humanity", "truth", "skepticism"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013d)
CREATE (t:THOUGHT {    name: "thought.ATHEISM SUCKS",
    alias: "Thought: Atheism Sucks",
    parent: "topic.PHILOSOPHY",
    tags: ['atheism', 'philosophy', 'humanity', 'truth', 'skepticism'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.ATHEISM SUCKS",
    ctype: "THOUGHT",
    en_title: "Atheism Sucks",
    en_content: "The problem with believing you're a thing is that you'll start treating other people as things. Atheism sucks!",
    es_title: "El Ateísmo Apesta",
    es_content: "El problema de creer que eres una cosa es que empezarás a tratar a otras personas como cosas. ¡El ateísmo apesta!",
    fr_title: "L'Athéisme Craint",
    fr_content: "Le problème de croire que vous êtes une chose, c'est que vous commencerez à traiter les autres comme des choses. L'athéisme craint !",
    hi_title: "नास्तिकता घृणित है",
    hi_content: "यह मानने की समस्या कि आप एक वस्तु हैं, यह है कि आप अन्य लोगों को वस्तुओं के रूप में मानना शुरू कर देंगे। नास्तिकता घृणित है!",
    zh_title: "Wúshénlùn zāogāo",
    zh_content: "Xiāngxìn zìjǐ shì yīgè wùtǐ de wèntí zàiyú, nǐ huì kāishǐ bǎ qítā rén dàngzuò wùtǐ. Wúshénlùn zāogāo tòule!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ATHEISM SUCKS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->ATHEISM SUCKS"
RETURN t, parent;
```

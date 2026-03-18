---
type: THOUGHT
name: "thought.TREATING JUDAS ISCARIOT"
alias: "Thought: Treating Judas Iscariot"
parent: "topic.THE GODHEAD"
en_content: "Do you think Jesus treated Judas Iscariot differently from the rest of the disciples?"
tags: ["judas", "jesus", "treatment", "disciples"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Dec-2013)
CREATE (t:THOUGHT {    name: "thought.TREATING JUDAS ISCARIOT",
    alias: "Thought: Treating Judas Iscariot",
    parent: "topic.THE GODHEAD",
    tags: ['judas', 'jesus', 'treatment', 'disciples'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.TREATING JUDAS ISCARIOT",
    ctype: "THOUGHT",
    en_title: "Treating Judas Iscariot",
    en_content: "Do you think Jesus treated Judas Iscariot differently from the rest of the disciples?",
    es_title: "El Trato a Judas Iscariote",
    es_content: "¿Crees que Jesús trató a Judas Iscariote de manera diferente al resto de los discípulos?",
    fr_title: "Le Traitement de Judas Iscariote",
    fr_content: "Pensez-vous que Jésus a traité Judas Iscariote différemment du reste des disciples ?",
    hi_title: "यहूदा इस्करियोती के साथ व्यवहार",
    hi_content: "क्या आपको लगता है कि यीशु ने यहूदा इस्करियोती के साथ बाकी चेलों से अलग व्यवहार किया था?",
    zh_title: "Duì Yóudà Jiālüèrén de Duìdài",
    zh_content: "Nǐ rènwéi Yēsū duì Yóudà Jiālüèrén de duìdài yǔ qítā méntú yǒu suǒ bùtóng ma?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TREATING JUDAS ISCARIOT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->TREATING JUDAS ISCARIOT"
RETURN t, parent;
```

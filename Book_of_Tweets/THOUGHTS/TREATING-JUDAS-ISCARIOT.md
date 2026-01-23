---
name: "thought.TREATING JUDAS ISCARIOT"
alias: "Thought: Treating Judas Iscariot"
type: THOUGHT
en_content: "Do you think Jesus treated Judas Iscariot differently from the rest of the disciples?"
parent: "topic.THE GODHEAD"
tags:
- judas
- jesus
- treatment
- disciples
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.TREATING JUDAS ISCARIOT",
    alias: "Thought: Treating Judas Iscariot",
    parent: "topic.THE GODHEAD",
    tags: ['judas', 'jesus', 'treatment', 'disciples'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.TREATING JUDAS ISCARIOT",
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

MATCH (t:THOUGHT {name: "thought.TREATING JUDAS ISCARIOT"})
MATCH (c:CONTENT {name: "content.TREATING JUDAS ISCARIOT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.TREATING JUDAS ISCARIOT" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.TREATING JUDAS ISCARIOT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >TREATING JUDAS ISCARIOT" }]->(child);
```

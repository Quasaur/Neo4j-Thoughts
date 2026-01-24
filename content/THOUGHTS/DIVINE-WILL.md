---
name: "thought.DIVINE WILL"
alias: "Thought: Sovereignty of God's Will"
type: THOUGHT
tags:
- sovereignty
- gods_will
- omnipotence
- authority
- providence
en_content: "Do you really believe that God has EVER done something He didn't want to do?"
parent: "topic.DIVINE SOVEREIGNTY"
level: 2
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
---

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {
    name: "thought.DIVINE WILL",
    alias: "Thought: DIVINE WILL",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ["sovereignty", "gods_will", "omnipotence", "authority", "providence"],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DIVINE WILL",
    en_title: "DIVINE WILL",
    en_content: "Do you really believe that God has EVER done something He didn't want to do?",
    es_title: "VOLUNTAD DIVINA",
    es_content: "¿De verdad crees que Dios ha hecho ALGUNA VEZ algo que no quería hacer?",
    fr_title: "VOLONTÉ DIVINE",
    fr_content: "Croyez-vous vraiment que Dieu a JAMAIS fait quelque chose qu'il ne voulait pas faire ?",
    hi_title: "ईश्वरीय इच्छा",
    hi_content: "क्या आप वास्तव में मानते हैं कि ईश्वर ने कभी भी ऐसा कुछ किया है जो वह नहीं करना चाहता था?",
    zh_title: "shén dì yì zhì",
    zh_content: "nǐ zhēn de xiāng xìn shàng dì céng jīng zhuò guò tā bù xiǎng zhuò de shì ma ？"
});

MATCH (t:THOUGHT {name: "thought.DIVINE WILL"})
MATCH (c:CONTENT {name: "content.DIVINE WILL"})
MERGE (t)-[:HAS_CONTENT {name: "edge.DIVINE WILL"}]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.DIVINE WILL"})
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE SOVEREIGNTY->DIVINE WILL"}]->(child);
```

---
type: THOUGHT
name: "thought.TWITTER TO HEAVEN"
alias: "Thought: Twitter To Heaven"
parent: "topic.SPIRITUALITY"
en_content: "If I could, I'd take my Twitter followers to Heaven with me."
tags: ["heaven", "desire", "compassion", "followers", "eternity"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Oct-2011b)
CREATE (t:THOUGHT {    name: "thought.TWITTER TO HEAVEN",
    alias: "Thought: Twitter To Heaven",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'desire', 'compassion', 'followers', 'eternity'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.TWITTER TO HEAVEN",
    ctype: "THOUGHT",
    en_title: "Twitter To Heaven",
    en_content: "If I could, I'd take my Twitter followers to Heaven with me.",
    es_title: "Twitter al Cielo",
    es_content: "Si pudiera, llevaría a mis seguidores de Twitter al Cielo conmigo.",
    fr_title: "Twitter vers le Paradis",
    fr_content: "Si je le pouvais, j'emmènerais mes abonnés Twitter au Paradis avec moi.",
    hi_title: "ट्विटर से स्वर्ग तक",
    hi_content: "यदि मैं कर सकूं, तो अपने ट्विटर अनुयायियों को अपने साथ स्वर्ग ले जाऊं।",
    zh_title: "Tuī tè dào tiāntáng",
    zh_content: "Rúguǒ kěyǐ de huà, wǒ xiǎng dài zhe wǒ de Tuī tè fěnsī yīqǐ qù tiāntáng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TWITTER TO HEAVEN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->TWITTER TO HEAVEN"
RETURN t, parent;
```

---
name: "thought.TWITTER TO HEAVEN"
alias: "Thought: Twitter To Heaven"
type: THOUGHT
en_content: "If I could, I'd take my Twitter followers to Heaven with me."
parent: "topic.SPIRITUALITY"
tags:
- heaven
- desire
- compassion
- followers
- eternity
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.TWITTER TO HEAVEN",
    alias: "Thought: Twitter To Heaven",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'desire', 'compassion', 'followers', 'eternity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TWITTER TO HEAVEN",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TWITTER TO HEAVEN" AND c.name = "content.TWITTER TO HEAVEN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TWITTER TO HEAVEN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.TWITTER TO HEAVEN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >TWITTER TO HEAVEN" }]->(child);
```

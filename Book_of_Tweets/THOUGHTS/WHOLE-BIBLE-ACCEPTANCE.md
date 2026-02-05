---
name: "thought.WHOLE BIBLE ACCEPTANCE"
alias: "Thought: Whole Bible Acceptance"
type: THOUGHT
en_content: "We should accept the whole Bible, or none of it; otherwise we distort its message."
parent: "topic.TRUTH"
tags:
- bible
- truth
- distortion
- message
- authority
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Apr-2013)
CREATE (t:THOUGHT {
    name: "thought.WHOLE BIBLE ACCEPTANCE",
    alias: "Thought: Whole Bible Acceptance",
    parent: "topic.TRUTH",
    tags: ['bible', 'truth', 'distortion', 'message', 'authority'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WHOLE BIBLE ACCEPTANCE",
    en_title: "Whole Bible Acceptance",
    en_content: "We should accept the whole Bible, or none of it; otherwise we distort its message.",
    es_title: "Aceptación Completa de la Biblia",
    es_content: "Debemos aceptar toda la Biblia, o nada de ella; de lo contrario, distorsionamos su mensaje.",
    fr_title: "Acceptation Complète de la Bible",
    fr_content: "Nous devons accepter toute la Bible, ou rien d'elle ; sinon nous déformons son message.",
    hi_title: "संपूर्ण बाइबिल की स्वीकृति",
    hi_content: "हमें पूरी बाइबिल को स्वीकार करना चाहिए, या उसमें से कुछ भी नहीं; अन्यथा हम इसके संदेश को विकृत कर देते हैं।",
    zh_title: "Jiēshòu quánbù shèngjīng  jiē shòu quán bù shèng jīng",
    zh_content: "Wǒmen yīnggāi jiēshòu zhěngběn shèngjīng, huò yīdiǎn yě bù jiēshòu; fǒuzé wǒmen jiù wāiqū le tā de xìnxī.  wǒ men yīng gāi jiē shòu zhěng běn shèng jīng ， huò yì diǎn yě bù jiē shòu ； fǒu zé wǒ men jiù wāi qū le tā de xìn xī 。"
});

MATCH (t:THOUGHT {name: "thought.WHOLE BIBLE ACCEPTANCE"})
MATCH (c:CONTENT {name: "content.WHOLE BIBLE ACCEPTANCE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.WHOLE BIBLE ACCEPTANCE" }]->(c);

MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:THOUGHT {name: "thought.WHOLE BIBLE ACCEPTANCE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH->WHOLE BIBLE ACCEPTANCE" }]->(child);
```

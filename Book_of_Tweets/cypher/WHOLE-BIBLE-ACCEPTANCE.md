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
    zh_title: "Jiēshòu quánbù shèngjīng 接受全部圣经",
    zh_content: "Wǒmen yīnggāi jiēshòu zhěngběn shèngjīng, huò yīdiǎn yě bù jiēshòu; fǒuzé wǒmen jiù wāiqū le tā de xìnxī. 我们应该接受整本圣经，或一点也不接受；否则我们就歪曲了它的信息。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WHOLE BIBLE ACCEPTANCE" AND c.name = "content.WHOLE BIBLE ACCEPTANCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WHOLE BIBLE ACCEPTANCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.WHOLE BIBLE ACCEPTANCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >WHOLE BIBLE ACCEPTANCE" }]->(child);
```

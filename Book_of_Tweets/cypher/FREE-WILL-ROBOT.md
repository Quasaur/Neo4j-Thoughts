---
name: "thought.FREE WILL ROBOT"
alias: "Thought: Free Will Robot"
type: THOUGHT
en_content: "If you WERE a robot...HOW WOULD YOU KNOW your will wasn't free?"
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- freewill
- consciousness
- robot
- truth
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.FREE WILL ROBOT",
    alias: "Thought: Free Will Robot",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'freewill', 'consciousness', 'robot', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FREE WILL ROBOT",
    en_title: "Free Will Robot",
    en_content: "If you WERE a robot...HOW WOULD YOU KNOW your will wasn't free?",
    es_title: "Robot de Libre Albedrío",
    es_content: "Si FUERAS un robot...¿CÓMO SABRÍAS que tu voluntad no es libre?",
    fr_title: "Robot du Libre Arbitre",
    fr_content: "Si tu ÉTAIS un robot...COMMENT SAURAIS-TU que ta volonté n'est pas libre ?",
    hi_title: "स्वतंत्र इच्छा रोबोट",
    hi_content: "यदि तुम एक रोबोट होते...तो तुम कैसे जानते कि तुम्हारी इच्छा स्वतंत्र नहीं है?",
    zh_title: "Zì Yóu Yì Zhì Jī Qì Rén",
    zh_content: "Rú guǒ nǐ SHÌ yī gè jī qì rén...nǐ RÚHÉ zhī dào nǐ de yì zhì bù shì zì yóu de?"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FREE WILL ROBOT" AND c.name = "content.FREE WILL ROBOT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FREE WILL ROBOT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.FREE WILL ROBOT"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >FREE WILL ROBOT" }]->(child);
```

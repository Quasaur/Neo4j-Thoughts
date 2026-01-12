---
name: "thought.REJOICING IN OTHERS"
alias: "Thought: Rejoicing In Others"
type: THOUGHT
en_content: I rejoice in the achievements God accomplished in you as though He had accomplished them in me.
parent: topic.LOVE
tags:
  - joy
  - character
  - comparison
  - attitude
  - success
level: 3
neo4j: true
ptopic: "[[topic-LOVE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Dec-2011b)
CREATE (t:THOUGHT {
    name: "thought.REJOICING IN OTHERS",
    alias: "Thought: Rejoicing In Others",
    parent: "topic.ATTITUDE",
    tags: ['joy', 'character', 'comparison', 'attitude', 'success'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.REJOICING IN OTHERS",
    en_title: "Rejoicing In Others",
    en_content: "I rejoice in the achievements God accomplished in you as though He had accomplished them in me.",
    es_title: "Regocijándose en Otros",
    es_content: "Me regocijo en los logros que Dios realizó en ti como si los hubiera realizado en mí.",
    fr_title: "Se Réjouir en Autrui",
    fr_content: "Je me réjouis des accomplissements que Dieu a réalisés en toi comme s'Il les avait accomplis en moi.",
    hi_title: "दूसरों में आनंदित होना",
    hi_content: "मैं उन उपलब्धियों में आनंदित होता हूँ जो परमेश्वर ने तुम में पूर्ण की हैं, जैसे कि उसने उन्हें मुझ में पूर्ण किया हो।",
    zh_title: "Zài Tārén Zhōng Xǐlè",
    zh_content: "Wǒ wèi Shàngdì zài nǐ shēnshang suǒ chéngjiù de shìqíng ér xǐlè, jiù hǎoxiàng Tā zài wǒ shēnshang chéngjiù le zhèxiē shìqíng yīyàng."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REJOICING IN OTHERS" AND c.name = "content.REJOICING IN OTHERS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REJOICING IN OTHERS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.REJOICING IN OTHERS"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >REJOICING IN OTHERS" }]->(child);
```

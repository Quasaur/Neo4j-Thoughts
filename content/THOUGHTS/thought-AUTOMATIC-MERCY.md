---
type: THOUGHT
name: "thought.AUTOMATIC MERCY"
alias: "Thought: Authomatic Mercy"
parent: "topic.ATTITUDE"
en_content: "God’s love for sinners doesn’t negate His utter hatred of sin. Mercy is neither owed nor deserved and should NEVER be presumed."
tags: ["spirituality", "mercy", "hatred", "gospel", "life"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.AUTOMATIC MERCY",
    alias: "Thought: Authomatic Mercy",
    parent: "topic.ATTITUDE",
    tags: ["spirituality", "mercy", "hatred", "gospel", "life"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AUTOMATIC MERCY",
    ctype: "THOUGHT",
    en_title: "Authomatic Mercy",
    en_content: "God’s love for sinners doesn’t negate His utter hatred of sin. Mercy is neither owed nor deserved and should NEVER be presumed.",
    es_title: "MISERICORDIA AUTOMATICA",
    es_content: "El amor de Dios por los pecadores no niega su odio total hacia el pecado. La misericordia no se debe ni se merece y NUNCA se debe presumir.",
    fr_title: "MISÉRICORDE AUTOMATIQUE",
    fr_content: "L’amour de Dieu pour les pécheurs ne nie pas sa haine totale du péché. La miséricorde n’est ni due ni méritée et ne doit JAMAIS être présumée.",
    hi_title: "स्वचालित दया",
    hi_content: "पापियों के प्रति परमेश्वर का प्रेम पाप के प्रति उसकी पूर्ण घृणा को नकारता नहीं है। दया न तो देय है और न ही इसके योग्य है और इसकी कल्पना कभी नहीं की जानी चाहिए।",
    zh_title: "zì dòng cí bēi",
    zh_content: "shén duì zuì rén de ài bìng bù néng dǐ xiāo tā duì zuì de chè dǐ zēng hèn 。 lián mǐn jì bù zhí dé yě bù yīng dé ， bìng qiě yǒng yuǎn bù yīng gāi bèi jiǎ dìng 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.AUTOMATIC MERCY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->AUTOMATIC MERCY"
RETURN t, parent;
```

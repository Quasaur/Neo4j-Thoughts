---
name: "thought.AUTOMATIC_MERCY"
alias: "Thought: AUTHOMATIC MERCY"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- spirituality
- mercy
- hatred
- gospel
- life
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.AUTOMATIC_MERCY",
    alias: "Thought: AUTHOMATIC MERCY",
    parent: "topic.ATTITUDE",
    tags: ["spirituality", "mercy", "hatred", "gospel", "life"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AUTOMATIC_MERCY",
    en_title: "AUTHOMATIC MERCY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AUTOMATIC_MERCY" AND c.name = "content.AUTOMATIC_MERCY"
MERGE (t)-[:HAS_CONTENT {name: "edge.AUTOMATIC_MERCY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.AUTOMATIC_MERCY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->AUTOMATIC_MERCY"}]->(child);
```

---
type: THOUGHT
name: "thought.VOLITION5"
alias: "Thought: FIFTH VOLITION"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["freedom", "volition", "free_will", "ignorance", "flatearth"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.VOLITION5",
    alias: "Thought: FIFTH VOLITION",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "free_will", "ignorance", "flatearth"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION5",
    ctype: "THOUGHT",
    en_title: "FIFTH VOLITION",
 es_title: "QUINTA VOLICIÓN",
 fr_title: "CINQUIÈME VOLITION",
 hi_title: "पांचवी इच्छा",
 zh_title: "dì wǔ zhì yuàn",
    en_content: "",
 es_content: "Durante cientos de años existió una TIERRA PLANA en Europa por culpa de la IGNORANCIA; Lo mismo ocurre con el LIBRE ALBEDRÍO.",
 fr_content: "Pendant des centaines d’années, une TERRE PLATE a existé en Europe à cause de l’IGNORANCE ; il en est de même avec le LIBRE ARBITRE.",
 hi_content: "अज्ञानता के कारण यूरोप में सैकड़ों वर्षों तक चपटी पृथ्वी अस्तित्व में रही; स्वतंत्र इच्छा के साथ भी ऐसा ही है।",
 zh_content: "yóu yú wú zhī ， ōu zhōu shù bǎi nián lái yì zhí cún zài dì píng lùn 。 zì yóu yì zhì yě shì rú cǐ 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION5" AND c.name = "content.VOLITION5"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.VOLITION5"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION5"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->VOLITION5"}]->(child);
```
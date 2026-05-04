---
type: THOUGHT
name: "thought.GRATITUDE"
alias: "Thought: Gratitude"
parent: "topic.ATTITUDE"
en_content: "The last few months have been very challenging...but it's better than being dead (LOL)!"
tags: ["thanksgiving", "humility", "decision", "mercy", "dead"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GRATITUDE",
    alias: "Thought: Gratitude",
    parent: "topic.ATTITUDE",
    tags: ["thanksgiving", "humility", "decision", "mercy", "dead"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRATITUDE",
    ctype: "THOUGHT",
    en_title: "Thought: Gratitude",
    en_content: "The last few months have been very challenging...but it's better than being dead (LOL)!",
    es_title: "Pensamiento: Gratitud",
    es_content: "Los últimos meses han sido muy desafiantes...¡pero es mejor que estar muerto (LOL)!",
    fr_title: "Pensée : gratitude",
    fr_content: "Les derniers mois ont été très difficiles...mais c'est mieux que d'être mort (MDR) !",
    hi_title: "विचार: कृतज्ञता",
    hi_content: "पिछले कुछ महीने बहुत चुनौतीपूर्ण रहे हैं...लेकिन यह मरने से भी बेहतर है (LOL)!",
    zh_title: "sī xiǎng : gǎn ēn",
    zh_content: "guò qù de jǐ gè yuè fēi cháng jù yǒu tiǎo zhàn xìng …… dàn zǒng bǐ sǐ le hǎo （ xiào ）！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GRATITUDE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->GRATITUDE"
RETURN t, parent;
```

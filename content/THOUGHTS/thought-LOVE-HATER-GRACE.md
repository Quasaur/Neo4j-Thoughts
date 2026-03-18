---
type: THOUGHT
name: "thought.LOVE HATER GRACE"
alias: "Thought: Love Hater Grace"
parent: "topic.GRACE"
en_content: "To love the one who loves you is pleasure. To love the one who ignores you is compassion. To love the one who hates you is Grace."
tags: ["love", "hater", "grace", "character", "compassion"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LOVE HATER GRACE",
    alias: "Thought: Love Hater Grace",
    parent: "topic.GRACE",
    tags: ['love', 'hater', 'grace', 'character', 'compassion'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LOVE HATER GRACE",
    ctype: "THOUGHT",
    en_title: "Love Hater Grace",
    en_content: "To love the one who loves you is pleasure. To love the one who ignores you is compassion. To love the one who hates you is Grace.",
    es_title: "Amor Aborrecedor Gracia",
    es_content: "Amar a quien te ama es placer. Amar a quien te ignora es compasión. Amar a quien te aborrece es Gracia.",
    fr_title: "Amour Haine Grâce",
    fr_content: "Aimer celui qui vous aime est un plaisir. Aimer celui qui vous ignore est compassion. Aimer celui qui vous hait est Grâce.",
    hi_title: "प्रेम द्वेषी अनुग्रह",
    hi_content: "जो आपसे प्रेम करता है उससे प्रेम करना आनंद है। जो आपको नज़रअंदाज़ करता है उससे प्रेम करना करुणा है। जो आपसे घृणा करता है उससे प्रेम करना अनुग्रह है।",
    zh_title: "Ài Hèn Ēn Diǎn",
    zh_content: "Ài nà ài nǐ de rén shì kuài lè. Ài nà hū lüè nǐ de rén shì cí bēi. Ài nà hèn nǐ de rén shì Ēn Diǎn."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOVE HATER GRACE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->LOVE HATER GRACE"
RETURN t, parent;
```

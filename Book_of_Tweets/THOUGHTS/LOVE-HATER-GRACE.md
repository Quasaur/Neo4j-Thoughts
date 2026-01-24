---
name: "thought.LOVE HATER GRACE"
alias: "Thought: Love Hater Grace"
type: THOUGHT
en_content: "To love the one who loves you is pleasure. To love the one who ignores you is compassion. To love the one who hates you is Grace."
parent: "topic.GRACE"
tags:
- love
- hater
- grace
- character
- compassion
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013e)
CREATE (t:THOUGHT {
    name: "thought.LOVE HATER GRACE",
    alias: "Thought: Love Hater Grace",
    parent: "topic.GRACE",
    tags: ['love', 'hater', 'grace', 'character', 'compassion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LOVE HATER GRACE",
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

MATCH (t:THOUGHT {name: "thought.LOVE HATER GRACE"})
MATCH (c:CONTENT {name: "content.LOVE HATER GRACE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVE HATER GRACE" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.LOVE HATER GRACE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE->LOVE HATER GRACE" }]->(child);
```

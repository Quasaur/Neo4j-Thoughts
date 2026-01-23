---
name: "thought.INVESTMENT IN CHURCH"
alias: "Thought: Investment In Church"
type: THOUGHT
en_content: "If you put something into your church, you'll ALWAYS get something out!"
parent: "topic.RELIGION"
tags:
- church
- investment
- return
- religion
- community
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013e)
CREATE (t:THOUGHT {
    name: "thought.INVESTMENT IN CHURCH",
    alias: "Thought: Investment In Church",
    parent: "topic.RELIGION",
    tags: ['church', 'investment', 'return', 'religion', 'community'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INVESTMENT IN CHURCH",
    en_title: "Investment In Church",
    en_content: "If you put something into your church, you'll ALWAYS get something out!",
    es_title: "Inversión en la Iglesia",
    es_content: "¡Si inviertes algo en tu iglesia, SIEMPRE recibirás algo a cambio!",
    fr_title: "Investissement dans l'Église",
    fr_content: "Si vous investissez quelque chose dans votre église, vous en retirerez TOUJOURS quelque chose !",
    hi_title: "चर्च में निवेश",
    hi_content: "यदि आप अपनी चर्च में कुछ निवेश करते हैं, तो आपको हमेशा कुछ न कुछ मिलेगा!",
    zh_title: "Zài Jiàohuì Zhōng De Tóuzī",
    zh_content: "Rúguǒ nǐ xiàng nǐ de jiàohuì tóurù shénme, nǐ zǒng huì dédào shénme huíbào!"
});

MATCH (t:THOUGHT {name: "thought.INVESTMENT IN CHURCH"})
MATCH (c:CONTENT {name: "content.INVESTMENT IN CHURCH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.INVESTMENT IN CHURCH" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.INVESTMENT IN CHURCH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >INVESTMENT IN CHURCH" }]->(child);
```

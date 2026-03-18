---
type: THOUGHT
name: "thought.CORRUPTION WITHOUT DEATH"
alias: "Thought: Corruption Without Death"
parent: "topic.HUMANITY"
en_content: "Watched movie \"In Time\"; without death, humanity would be even more hideously corrupt than it is now."
tags: ["death", "corruption", "humanity", "character", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012a)
CREATE (t:THOUGHT {    name: "thought.CORRUPTION WITHOUT DEATH",
    alias: "Thought: Corruption Without Death",
    parent: "topic.HUMANITY",
    tags: ['death', 'corruption', 'humanity', 'character', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CORRUPTION WITHOUT DEATH",
    ctype: "THOUGHT",
    en_title: "Corruption Without Death",
    en_content: "Watched movie \"In Time\"; without death, humanity would be even more hideously corrupt than it is now.",
    es_title: "Corrupción Sin Muerte",
    es_content: "Vi la película \"In Time\"; sin la muerte, la humanidad sería aún más horriblemente corrupta de lo que es ahora.",
    fr_title: "Corruption Sans Mort",
    fr_content: "J'ai regardé le film \"In Time\" ; sans la mort, l'humanité serait encore plus hideusement corrompue qu'elle ne l'est maintenant.",
    hi_title: "मौत के बिना भ्रष्टाचार",
    hi_content: "फिल्म \"In Time\" देखी; मौत के बिना, मानवता अब से भी अधिक भयानक रूप से भ्रष्ट होगी।",
    zh_title: "Méiyǒu Sǐwáng de Fǔbài",
    zh_content: "Kànle diànyǐng \"In Time\"; Méiyǒu sǐwáng, rénlèi huì bǐ xiànzài gèng kěpà de fǔbài."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CORRUPTION WITHOUT DEATH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->CORRUPTION WITHOUT DEATH"
RETURN t, parent;
```

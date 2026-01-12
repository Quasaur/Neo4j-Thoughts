---
name: "thought.CORRUPTION WITHOUT DEATH"
alias: "Thought: Corruption Without Death"
type: THOUGHT
en_content: "Watched movie \"In Time\"; without death, humanity would be even more hideously corrupt than it is now."
parent: "topic.HUMANITY"
tags:
- death
- corruption
- humanity
- character
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.CORRUPTION WITHOUT DEATH",
    alias: "Thought: Corruption Without Death",
    parent: "topic.HUMANITY",
    tags: ['death', 'corruption', 'humanity', 'character', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CORRUPTION WITHOUT DEATH",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CORRUPTION WITHOUT DEATH" AND c.name = "content.CORRUPTION WITHOUT DEATH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CORRUPTION WITHOUT DEATH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.CORRUPTION WITHOUT DEATH"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >CORRUPTION WITHOUT DEATH" }]->(child);
```

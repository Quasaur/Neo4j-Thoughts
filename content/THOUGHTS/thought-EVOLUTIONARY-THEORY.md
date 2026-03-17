---
type: THOUGHT
name: "thought.EVOLUTIONARY THEORY"
alias: "Thought: Evolutionary Theory"
parent: "topic.COSMOLOGY"
en_content: "Evolution is considered a theory (not a law) for a reason."
tags: ["evolution", "theory", "unlawful", "unproven", "unscientific"]
ptopic: "[[topic-COSMOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.EVOLUTIONARY THEORY",
    alias: "Thought: Evolutionary Theory",
    parent: "topic.COSMOLOGY",
    tags: ["evolution", "theory", "unlawful", "unproven", "unscientific"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVOLUTIONARY THEORY",
    ctype: "THOUGHT",
    en_title: "Evolutionary Theory",
    en_content: "Evolution is considered a theory (not a law) for a reason.",
    es_title: "TEORÍA EVOLUTIVA",
    es_content: "La evolución se considera una teoría (no una ley) por una razón.",
    fr_title: "THÉORIE ÉVOLUTIONNAIRE",
    fr_content: "L’évolution est considérée comme une théorie (et non une loi) pour une raison.",
    hi_title: "विकासवादी सिद्धांत",
    hi_content: "विकास को एक कारण से एक सिद्धांत (कानून नहीं) माना जाता है।",
    zh_title: "jìn huà lùn",
    zh_content: "jìn huà lùn bèi rèn wéi shì yī zhǒng lǐ lùn （ ér bú shì fǎ zé ） shì yǒu yuán yīn de 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EVOLUTIONARY THEORY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.COSMOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.COSMOLOGY->EVOLUTIONARY THEORY"
RETURN t, parent;
```

---
name: "thought.EVOLUTIONARY_THEORY"
alias: "Thought: EVOLUTIONARY THEORY"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- evolution
- theory
- unlawful
- unproven
- unscientific
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.EVOLUTIONARY_THEORY",
    alias: "Thought: EVOLUTIONARY THEORY",
    parent: "topic.COSMOLOGY",
    tags: ["evolution", "theory", "unlawful", "unproven", "unscientific"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVOLUTIONARY_THEORY",
    en_title: "EVOLUTIONARY THEORY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVOLUTIONARY_THEORY" AND c.name = "content.EVOLUTIONARY_THEORY"
MERGE (t)-[:HAS_CONTENT {name: "edge.EVOLUTIONARY_THEORY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.EVOLUTIONARY_THEORY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.COSMOLOGY->EVOLUTIONARY_THEORY"}]->(child);
```

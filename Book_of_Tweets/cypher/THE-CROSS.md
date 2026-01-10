---
name: "thought.THE CROSS"
alias: "Thought: The Cross"
type: THOUGHT
en_content: "The Cross is the Nexus of a Divine Science that never ceases to inform, renew and inspire awe, wonder, reverence and understanding."
parent: "topic.THE GOSPEL"
tags:
- the_cross
- divine_science
- awe_wonder
- redemption
- inspiration
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE CROSS",
    alias: "Thought: The Cross",
    parent: "topic.THE GOSPEL",
    tags: ["the_cross", "divine_science", "awe_wonder", "redemption", "inspiration"],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE CROSS",
    en_title: "Nexus of Science",
    en_content: "The Cross is the Nexus of a Divine Science that never ceases to inform, renew and inspire awe, wonder, reverence and understanding.",
    es_title: "Nexus de ciencia",
    es_content: "La Cruz es el Nexo de una Ciencia Divina que nunca deja de informar, renovar e inspirar asombro, maravilla, reverencia y entendimiento.",
    fr_title: "Nexus de science",
    fr_content: "La Croix est le Nexus d'une Science Divine qui ne cesse d'informer, de renouveler et d'inspirer l'effroi, l'émerveillement, la révérence et la compréhension.",
    hi_title: "vigyaan ka kendr",
    hi_content: "क्रॉस एक दिव्य विज्ञान का केंद्र है जो विस्मय, आश्चर्य, श्रद्धा और समझ को सूचित करने, नवीनीकृत करने और प्रेरित करने के लिए कभी नहीं रुकता है।",
    zh_title: "kè xué shū niǔ",
    zh_content: "shí zì jià shì shén shèng kè xué de shū niǔ, tā bú duàn de qǐ dí, gèng xīn bìng jī fā wèi jù, jīng tàn, qián jìng hé lǐ jiě."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE CROSS" AND c.name = "content.THE CROSS"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE CROSS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GOSPEL" AND child.name = "thought.THE CROSS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GOSPEL >THE CROSS"}]->(child);
```

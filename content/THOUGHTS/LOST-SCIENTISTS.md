---
name: "thought.LOST_SCIENTISTS"
alias: "Thought: LOST SCIENTISTS"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- science
- bigbang
- lost
- creatiion
- origin
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LOST_SCIENTISTS",
    alias: "Thought: LOST SCIENTISTS",
    parent: "topic.COSMOLOGY",
    tags: ["science", "bigbang", "lost", "creatiion", "origin"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LOST_SCIENTISTS",
    en_title: "LOST SCIENTISTS",
    en_content: "The truth is that scientists have had to admit that they're lost beyond the Big Bang.",
    es_title: "CIENTÍFICOS PERDIDOS",
    es_content: "La verdad es que los científicos han tenido que admitir que están perdidos más allá del Big Bang.",
    fr_title: "SCIENTIFIQUES PERDUS",
    fr_content: "La vérité est que les scientifiques ont dû admettre qu’ils sont perdus au-delà du Big Bang.",
    hi_title: "खोए हुए वैज्ञानिक",
    hi_content: "सच्चाई यह है कि वैज्ञानिकों को यह स्वीकार करना पड़ा है कि वे बिग बैंग से परे खो गए हैं।",
    zh_title: "mí shī de kē xué jiā",
    zh_content: "shì shí shì ， kē xué jiā men bù dé bù chéng rèn ， tā men zài dà bào zhà zhī hòu jiù mí shī le 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOST_SCIENTISTS" AND c.name = "content.LOST_SCIENTISTS"
MERGE (t)-[:HAS_CONTENT {name: "edge.LOST_SCIENTISTS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.LOST_SCIENTISTS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.COSMOLOGY->LOST_SCIENTISTS"}]->(child);
```

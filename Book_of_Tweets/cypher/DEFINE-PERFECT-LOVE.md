---
name: "thought.DEFINE PERFECT LOVE"
alias: "Thought: Define Perfect Love"
type: THOUGHT
en_content: "Love: the blurring of identity between two or more persons. The Love among the Members of The Godhead is such: to see One is to see All."
parent: "topic.PHILOSOPHY"
tags:
- love
- identity
- trinity
- philosophy
- unity
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.DEFINE PERFECT LOVE",
    alias: "Thought: Define Perfect Love",
    parent: "topic.PHILOSOPHY",
    tags: ['love', 'identity', 'trinity', 'philosophy', 'unity'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE PERFECT LOVE",
    en_title: "Define Perfect Love",
    en_content: "Love: the blurring of identity between two or more persons. The Love among the Members of The Godhead is such: to see One is to see All.",
    es_title: "Define el Amor Perfecto",
    es_content: "Amor: la difuminación de la identidad entre dos o más personas. El Amor entre los Miembros de la Trinidad es tal: ver a Uno es ver a Todos.",
    fr_title: "Définir l'Amour Parfait",
    fr_content: "Amour : le flou de l'identité entre deux ou plusieurs personnes. L'Amour parmi les Membres de la Trinité est tel : voir l'Un, c'est voir Tous.",
    hi_title: "सिद्ध प्रेम को परिभाषित करें",
    hi_content: "प्रेम: दो या अधिक व्यक्तियों के बीच पहचान का धुंधला होना। परमेश्वर के सदस्यों के बीच प्रेम ऐसा है: एक को देखना सभी को देखना है।",
    zh_title: "Dìng Yì Wán Měi De Ài",
    zh_content: "Ài: liǎng gè huò gèng duō rén zhī jiān shēn fèn de mó hu. Shén tǐ chéng yuán zhī jiān de ài jiù shì zhè yàng: kàn jiàn yī gè jiù shì kàn jiàn quán bù."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEFINE PERFECT LOVE" AND c.name = "content.DEFINE PERFECT LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE PERFECT LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.DEFINE PERFECT LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >DEFINE PERFECT LOVE" }]->(child);
```

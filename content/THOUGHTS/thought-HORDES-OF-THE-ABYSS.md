---
type: THOUGHT
name: "thought.HORDES OF THE ABYSS"
alias: "Thought: Hordes Of The Abyss"
parent: "topic.APOCALYPSE"
en_content: "Humanity will be visited by the hordes of the Abyss because that is what Humanity, by its deeds, asked for."
tags: ["abyss", "hordes", "deeds", "judgment", "evil"]
ptopic: "[[topic-APOCALYPSE]]"
level: 5
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013d)
CREATE (t:THOUGHT {
    name: "thought.HORDES OF THE ABYSS",
    alias: "Thought: Hordes Of The Abyss",
    parent: "topic.APOCALYPSE",
    tags: ['abyss', 'hordes', 'deeds', 'judgment', 'evil'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.HORDES OF THE ABYSS",
    ctype: "THOUGHT",
    en_title: "Thought: Hordes Of The Abyss",
    en_content: "Humanity will be visited by the hordes of the Abyss because that is what Humanity, by its deeds, asked for.",
    es_title: "Pensamiento: Hordas del Abismo",
    es_content: "La Humanidad será visitada por las hordas del Abismo porque eso es lo que la Humanidad, con sus hechos, pidió.",
    fr_title: "Pensée : Hordes des Abysses",
    fr_content: "L’humanité sera visitée par les hordes des Abysses car c’est ce que l’humanité, par ses actes, a demandé.",
    hi_title: "विचार: रसातल की भीड़",
    hi_content: "रसातल की भीड़ मानवता का दौरा करेगी क्योंकि मानवता ने अपने कर्मों से यही मांगा है।",
    zh_title: "sī xiǎng : shēn yuān bù luò",
    zh_content: "rén lèi jiāng shòu dào shēn yuān bù luò de bài fǎng , yīn wèi zhè shì rén lèi tōng guò qí xíng wéi suǒ yāo qiú de ."
});

MATCH (t:THOUGHT {name: "thought.HORDES OF THE ABYSS"})
MATCH (c:CONTENT {name: "content.HORDES OF THE ABYSS"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.HORDES OF THE ABYSS" }]->(c);

MATCH (parent:TOPIC {name: "topic.APOCALYPSE"})
MATCH (child:THOUGHT {name: "thought.HORDES OF THE ABYSS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.APOCALYPSE->HORDES OF THE ABYSS" }]->(child);
```

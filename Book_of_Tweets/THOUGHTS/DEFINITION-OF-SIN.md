---
name: "thought.DEFINITION OF SIN"
alias: "Thought: Delusion of Self"
type: THOUGHT
en_content: "What is sin? Suffering under the delusion that I'm on my own in this life."
parent: "topic.MORALITY"
tags:
- sin
- delusion
- self_reliance
- brokenness
- definition
level: 3
neo4j: false
ptopic: 
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DEFINITION OF SIN",
    alias: "Thought: Delusion of Self",
    parent: "topic.MORALITY",
    tags: ["sin", "delusion", "self_reliance", "brokenness", "definition"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINITION OF SIN",
    en_title: "Definition of Sin",
    en_content: "What is sin? Suffering under the delusion that I'm on my own in this life.",
    es_title: "Definición de pecado",
    es_content: "¿Qué es el pecado? Sufrir bajo la ilusión de que estoy por mi cuenta en esta vida.",
    fr_title: "Définition du péché",
    fr_content: "Qu'est-ce que le péché ? Souffrir de l'illusion que je suis seul dans cette vie.",
    hi_title: "paap kee paribhaasha",
    hi_content: "पाप क्या है? इस भ्रम में जीना कि मैं इस जीवन में अपने दम पर हूँ।",
    zh_title: "zuì de dìng yì",
    zh_content: "zuì shì shén me? zuì shì huàn xiǎng zhe zài zhè gè shēng mìng zhōng wǒ shì dù lì de yán."
});

MATCH (t:THOUGHT {name: "thought.DEFINITION OF SIN"})
MATCH (c:CONTENT {name: "content.DEFINITION OF SIN"})
MERGE (t)-[:HAS_CONTENT {name: "edge.DEFINITION OF SIN"}]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.DEFINITION OF SIN"})
MERGE (parent)-[:HAS_THOUGHT {name: "edge.MORALITY >DEFINITION OF SIN"}]->(child);
```

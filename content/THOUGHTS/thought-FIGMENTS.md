---
type: THOUGHT
name: "thought.FIGMENTS"
alias: "Thought: FIGMENTS"
parent: "topic.CREATION"
tags: ["imagination", "fables", "lessreal", "fictitious", "created"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FIGMENTS",
    alias: "Thought: FIGMENTS",
    parent: "topic.CREATION",
    tags: ["imagination", "fables", "lessreal", "fictitious", "created"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FIGMENTS",
    ctype: "THOUGHT",
    en_title: "FIGMENTS",
 es_title: "FIGMENTOS",
 fr_title: "FIGURES",
 hi_title: "चित्र",
 zh_title: "rén wù",
    en_content: "",
 es_content: "Todos somos producto de la Imaginación Divina... ¡y qué Imaginación!",
 fr_content: "Nous sommes tous le produit de l’imagination divine – et quelle imagination !",
 hi_content: "हम सभी दिव्य कल्पना की प्रतिमूर्ति हैं--और क्या कल्पना है!",
 zh_content: "wǒ men dōu shì shén shèng xiǎng xiàng lì de xū gòu —— zhè shì duō me měi miào de xiǎng xiàng lì a ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FIGMENTS" AND c.name = "content.FIGMENTS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FIGMENTS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.FIGMENTS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.CREATION->FIGMENTS"}]->(child);
```
---
type: THOUGHT
name: "thought.HAPPINESS"
alias: "Thought: Happiness"
parent: "topic.ATTITUDE"
tags: ["happy", "fulfilled", "satisfied", "delighted", "content"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HAPPINESS",
    alias: "Thought: Happiness",
    parent: "topic.ATTITUDE",
    tags: ["happy", "fulfilled", "satisfied", "delighted", "content"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HAPPINESS",
    ctype: "THOUGHT",
    en_title: "Happiness",
 es_title: "FELICIDAD",
 fr_title: "BONHEUR",
 hi_title: "ख़ुशी",
 zh_title: "xìng fú",
    en_content: "",
 es_content: "LA FELICIDAD no es producto de hacer lo que quieres...
...sino de hacer lo CORRECTO.",
 fr_content: "LE BONHEUR n'est pas le produit du fait de faire ce que l'on veut...
... mais de faire ce qui est BIEN.",
 hi_content: "ख़ुशी वह करने का परिणाम नहीं है जो आप चाहते हैं...
...लेकिन वही करना जो सही है।",
 zh_content: "xìng fú bú shì zuò nǐ xiǎng zuò de shì de jié guǒ ......
... ér shì zuò zhèng què de shì 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HAPPINESS" AND c.name = "content.HAPPINESS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.HAPPINESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HAPPINESS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->HAPPINESS"}]->(child);
```
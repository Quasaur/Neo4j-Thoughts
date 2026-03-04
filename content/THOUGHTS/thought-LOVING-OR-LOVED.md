---
type: THOUGHT
name: "thought.LOVING OR LOVED?"
alias: "Thought: Loving or Loved?"
parent: "topic.PSYCHOLOGY"
en_content: "So...which is better: loving God or being loved by God?"
tags: ["loving", "loved", "give", "receive", "preference"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LOVING OR LOVED?",
    alias: "Thought: Loving or Loved?",
    parent: "topic.PSYCHOLOGY",
    tags: ["loving", "loved", "give", "receive", "preference"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LOVING OR LOVED?",
    ctype: "THOUGHT",
    en_title: "Loving or Loved?",
    en_content: "So...which is better: loving God or being loved by God?",
    es_title: "¿AMAR O AMAR?",
    es_content: "Entonces... ¿qué es mejor: amar a Dios o ser amado por Dios?",
    fr_title: "AIMANT OU AIMÉ ?",
    fr_content: "Alors... qu'est-ce qui est mieux : aimer Dieu ou être aimé de Dieu ?",
    hi_title: "प्यार या प्यार?",
    hi_content: "तो...क्या बेहतर है: ईश्वर से प्रेम करना या ईश्वर द्वारा प्रेम किया जाना?",
    zh_title: "ài hái shì bèi ài ？",
    zh_content: "nà me …… nǎ ge gèng hǎo ： ài shén hái shì bèi shén ài ？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVING OR LOVED?" AND c.name = "content.LOVING OR LOVED?"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.LOVING OR LOVED?"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.LOVING OR LOVED?"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->LOVING OR LOVED?"}]->(child);
```

---
name: "thought.HIS DREAM"
alias: "Thought: His Dream"
type: THOUGHT
parent: "topic.CREATION"
tags:
- divine
- thought
- reality
- truth
- god
level: 2
neo4j: true
ptopic: "[[topic-CREATION]]"
insert: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HIS DREAM",
    alias: "Thought: His Dream",
    parent: "topic.CREATION",
    tags: ['divine', 'thought', 'reality', 'truth', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HIS DREAM",
    en_title: "His Dream",
    en_content: "When God dreams, it's called REALITY.",
    es_title: "Su sueño",
    es_content: "Cuando Dios sueña, se llama REALIDAD.",
    fr_title: "TSon rêve",
    fr_content: "Quand Dieu rêve, cela s'appelle la RÉALITÉ.",
    hi_title: "उसका सपना",
    hi_content: "जब भगवान सपना देखते हैं, तो उसे हकीकत कहते हैं।",
    zh_title: "Tā de mèngxiǎng",
    zh_content: "dāng shàngdì zuòmèng shí, nà jiùshì xiànshí."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HIS DREAM" AND c.name = "content.HIS DREAM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HIS DREAM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.HIS DREAM"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >HIS DREAM" }]->(child);
```

---
name: "thought.LAWS AND THE RICH"
alias: "Thought: Laws And The Rich"
type: THOUGHT
en_content: "As long as the laws favor the rich, the poor will always exist."
parent: "topic.MORALITY"
tags:
- poverty
- law
- wealth
- morality
- society
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012e)
CREATE (t:THOUGHT {
    name: "thought.LAWS AND THE RICH",
    alias: "Thought: Laws And The Rich",
    parent: "topic.MORALITY",
    tags: ['poverty', 'law', 'wealth', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LAWS AND THE RICH",
    en_title: "Laws And The Rich",
    en_content: "As long as the laws favor the rich, the poor will always exist.",
    es_title: "Las Leyes y Los Ricos",
    es_content: "Mientras las leyes favorezcan a los ricos, los pobres siempre existirán.",
    fr_title: "Les Lois et Les Riches",
    fr_content: "Tant que les lois favorisent les riches, les pauvres existeront toujours.",
    hi_title: "कानून और धनवान",
    hi_content: "जब तक कानून धनवानों का पक्ष लेते रहेंगे, तब तक गरीब हमेशा रहेंगे।",
    zh_title: "Fǎlǜ Yǔ Fùrén",
    zh_content: "Zhǐyào fǎlǜ piān'ài fùrén, qióngrén jiù yǒngyuǎn cúnzài."
});

MATCH (t:THOUGHT {name: "thought.LAWS AND THE RICH"})
MATCH (c:CONTENT {name: "content.LAWS AND THE RICH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LAWS AND THE RICH" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.LAWS AND THE RICH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >LAWS AND THE RICH" }]->(child);
```

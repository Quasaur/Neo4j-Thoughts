---
name: "thought.DANGER OF TRUTH"
alias: "Thought: Danger Of Truth"
type: THOUGHT
en_content: "Truth is a dangerous thing...yet so is a lie."
parent: "topic.TRUTH"
tags:
- truth
- lie
- danger
- philosophy
- morality
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.DANGER OF TRUTH",
    alias: "Thought: Danger Of Truth",
    parent: "topic.TRUTH",
    tags: ['truth', 'lie', 'danger', 'philosophy', 'morality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DANGER OF TRUTH",
    en_title: "Danger Of Truth",
    en_content: "Truth is a dangerous thing...yet so is a lie.",
    es_title: "Peligro de la Verdad",
    es_content: "La verdad es una cosa peligrosa... pero también lo es una mentira.",
    fr_title: "Danger de la Vérité",
    fr_content: "La vérité est une chose dangereuse... pourtant un mensonge l'est aussi.",
    hi_title: "सच्चाई का खतरा",
    hi_content: "सच्चाई एक खतरनाक चीज है... फिर भी झूठ भी है।",
    zh_title: "Zhēnlǐ de Wéixiǎn",
    zh_content: "Zhēnlǐ shì yīgè wéixiǎn de dōngxī... Dàn huǎngyán yě shì."
});

MATCH (t:THOUGHT {name: "thought.DANGER OF TRUTH"})
MATCH (c:CONTENT {name: "content.DANGER OF TRUTH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DANGER OF TRUTH" }]->(c);

MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:THOUGHT {name: "thought.DANGER OF TRUTH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >DANGER OF TRUTH" }]->(child);
```

---
name: "thought.GOD HONORS HONOR"
alias: "Thought: God Honors Honor"
type: THOUGHT
en_content: "God is not stupid; He honors those who honor Him...those who ignore Him are lightly esteemed."
parent: "topic.THE GODHEAD"
tags:
- god
- honor
- justice
- truth
- reverence
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.GOD HONORS HONOR",
    alias: "Thought: God Honors Honor",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'honor', 'justice', 'truth', 'reverence'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD HONORS HONOR",
    en_title: "God Honors Honor",
    en_content: "God is not stupid; He honors those who honor Him...those who ignore Him are lightly esteemed.",
    es_title: "Dios honra el honor",
    es_content: "Dios no es estúpido;Él honra a quienes lo honran... quienes lo ignoran son poco estimados.",
    fr_title: "Dieu honore l'honneur",
    fr_content: "Dieu n'est pas stupide ;Il honore ceux qui l'honorent... ceux qui l'ignorent sont peu estimés.",
    hi_title: "भगवान सम्मान सम्मान",
    hi_content: "भगवान मूर्ख नहीं है;वह उन लोगों का सम्मान करता है जो उसका सम्मान करते हैं...जो लोग उसकी उपेक्षा करते हैं उन्हें कम महत्व दिया जाता है।",
    zh_title: "shén zūn zhòng róng yào",
    zh_content: "shén bìng bù yú chǔn ； tā zūn zhòng nà xiē zūn jìng tā de rén …… nà xiē hū shì tā de rén shòu dào qīng shì 。"
});

MATCH (t:THOUGHT {name: "thought.GOD HONORS HONOR"})
MATCH (c:CONTENT {name: "content.GOD HONORS HONOR"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD HONORS HONOR" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD HONORS HONOR"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GOD HONORS HONOR" }]->(child);
```

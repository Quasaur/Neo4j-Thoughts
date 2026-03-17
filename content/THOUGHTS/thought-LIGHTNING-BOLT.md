---
type: THOUGHT
name: "thought.LIGHTNING BOLT"
alias: "Thought: Lightning Bolt"
parent: "topic.ENVIRONMENTAL SCIENCE"
en_content: "A single lightning bolt can be 5 miles in length and hotter than the surface of the Sun...God is Great!"
tags: ["creation", "power", "lightning", "nature", "majesty"]
ptopic: "[[topic-ENVIRONMENTAL-SCIENCE]]"
level: 6
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LIGHTNING BOLT",
    alias: "Thought: Lightning Bolt",
    parent: "topic.ENVIRONMENTAL SCIENCE",
    tags: ['creation', 'power', 'lightning', 'nature', 'majesty'],
    level: 6
});

CREATE (c:CONTENT {
    name: "content.LIGHTNING BOLT",
    ctype: "THOUGHT",
    en_title: "Lightning Bolt",
    en_content: "A single lightning bolt can be 5 miles in length and hotter than the surface of the Sun...God is Great!",
    es_title: "Rayo",
    es_content: "Un solo rayo puede medir 5 millas de largo y ser más caliente que la superficie del Sol... ¡Dios es Grande!",
    fr_title: "Éclair",
    fr_content: "Un seul éclair peut mesurer 5 miles de long et être plus chaud que la surface du Soleil... Dieu est Grand !",
    hi_title: "बिजली की चमक",
    hi_content: "एक बिजली की चमक 5 मील लंबी हो सकती है और सूर्य की सतह से भी अधिक गर्म हो सकती है... भगवान महान हैं!",
    zh_title: "Shan Dian",
    zh_content: "Yi dao shan dian ke yi chang da 5 ying li, wen du bi tai yang biao mian geng re... Shang Di zhen wei da!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIGHTNING BOLT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->LIGHTNING BOLT"
RETURN t, parent;
```

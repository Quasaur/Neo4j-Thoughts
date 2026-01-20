---
name: "thought.LIGHTNING BOLT"
alias: "Thought: Lightning Bolt"
type: THOUGHT
en_content: "A single lightning bolt can be 5 miles in length and hotter than the surface of the Sun...God is Great!"
parent: "topic.CREATION"
tags:
- creation
- power
- lightning
- nature
- majesty
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2011b)
CREATE (t:THOUGHT {
    name: "thought.LIGHTNING BOLT",
    alias: "Thought: Lightning Bolt",
    parent: "topic.CREATION",
    tags: ['creation', 'power', 'lightning', 'nature', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIGHTNING BOLT",
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

MATCH (t:THOUGHT {name: "thought.LIGHTNING BOLT"})
MATCH (c:CONTENT {name: "content.LIGHTNING BOLT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIGHTNING BOLT" }]->(c);

MATCH (parent:TOPIC {name: "topic.CREATION"})
MATCH (child:THOUGHT {name: "thought.LIGHTNING BOLT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >LIGHTNING BOLT" }]->(child);
```

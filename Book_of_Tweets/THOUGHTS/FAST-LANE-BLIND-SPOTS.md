---
name: "thought.FAST LANE BLIND SPOTS"
alias: "Thought: Fast Lane Blind Spots"
type: THOUGHT
en_content: "If you're living in the fast lane, watch your blind spots."
parent: "topic.WISDOM"
tags:
- wisdom
- life
- danger
- awareness
- caution
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.FAST LANE BLIND SPOTS",
    alias: "Thought: Fast Lane Blind Spots",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'life', 'danger', 'awareness', 'caution'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FAST LANE BLIND SPOTS",
    en_title: "Fast Lane Blind Spots",
    en_content: "If you're living in the fast lane, watch your blind spots.",
    es_title: "Puntos Ciegos del Carril Rápido",
    es_content: "Si estás viviendo en el carril rápido, vigila tus puntos ciegos.",
    fr_title: "Angles Morts de la Voie Rapide",
    fr_content: "Si vous vivez dans la voie rapide, surveillez vos angles morts.",
    hi_title: "तेज़ गति की अंधी जगहें",
    hi_content: "यदि आप तेज़ गति से जीवन जी रहे हैं, तो अपनी अंधी जगहों पर ध्यान दें।",
    zh_title: "Kuai Su Dao Shang De Si Jiao",
    zh_content: "Ru Guo Ni Sheng Huo Zai Kuai Su Dao Shang, Yao Zhu Yi Ni De Si Jiao."
});

MATCH (t:THOUGHT {name: "thought.FAST LANE BLIND SPOTS"})
MATCH (c:CONTENT {name: "content.FAST LANE BLIND SPOTS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAST LANE BLIND SPOTS" }]->(c);

MATCH (parent:TOPIC {name: "topic.WISDOM"})
MATCH (child:THOUGHT {name: "thought.FAST LANE BLIND SPOTS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >FAST LANE BLIND SPOTS" }]->(child);
```

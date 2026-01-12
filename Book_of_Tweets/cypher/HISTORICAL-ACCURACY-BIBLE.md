---
name: "thought.HISTORICAL ACCURACY BIBLE"
alias: "Thought: Historical Accuracy Bible"
type: THOUGHT
en_content: "The God in The Bible is described as Truth; therefore The Bible itself must be HISTORICALLY ACCURATE."
parent: "topic.TRUTH"
tags:
- truth
- bible
- history
- accuracy
- revelation
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.HISTORICAL ACCURACY BIBLE",
    alias: "Thought: Historical Accuracy Bible",
    parent: "topic.TRUTH",
    tags: ['truth', 'bible', 'history', 'accuracy', 'revelation'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HISTORICAL ACCURACY BIBLE",
    en_title: "Historical Accuracy Bible",
    en_content: "The God in The Bible is described as Truth; therefore The Bible itself must be HISTORICALLY ACCURATE.",
    es_title: "Precisión Histórica de la Biblia",
    es_content: "El Dios de La Biblia es descrito como Verdad; por lo tanto La Biblia misma debe ser HISTÓRICAMENTE PRECISA.",
    fr_title: "Exactitude Historique de la Bible",
    fr_content: "Le Dieu de La Bible est décrit comme Vérité; par conséquent La Bible elle-même doit être HISTORIQUEMENT EXACTE.",
    hi_title: "बाइबल की ऐतिहासिक सटीकता",
    hi_content: "बाइबल में परमेश्वर को सत्य के रूप में वर्णित किया गया है; इसलिए बाइबल स्वयं ऐतिहासिक रूप से सटीक होनी चाहिए।",
    zh_title: "Sheng Jing de Li Shi Zhun Que Xing",
    zh_content: "Sheng Jing zhong de Shang Di bei miao shu wei Zhen Li; yin ci Sheng Jing ben shen bi xu shi LI SHI ZHUN QUE de."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HISTORICAL ACCURACY BIBLE" AND c.name = "content.HISTORICAL ACCURACY BIBLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HISTORICAL ACCURACY BIBLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.HISTORICAL ACCURACY BIBLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >HISTORICAL ACCURACY BIBLE" }]->(child);
```

---
name: "thought.HEAVEN HEALS SORROW"
alias: "Thought: Heaven Heals Sorrow"
type: THOUGHT
en_content: "Earth has no sorrow that Heaven cannot heal. -- Hymn"
parent: "topic.SPIRITUALITY"
tags:
- healing
- heaven
- sorrow
- comfort
- grace
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN HEALS SORROW",
    alias: "Thought: Heaven Heals Sorrow",
    parent: "topic.SPIRITUALITY",
    tags: ['healing', 'heaven', 'sorrow', 'comfort', 'grace'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEAVEN HEALS SORROW",
    en_title: "Heaven Heals Sorrow",
    en_content: "Earth has no sorrow that Heaven cannot heal. -- Hymn",
    es_title: "El Cielo Sana la Tristeza",
    es_content: "No hay tristeza en la Tierra que el Cielo no pueda sanar. -- Himno",
    fr_title: "Le Ciel Guérit la Douleur",
    fr_content: "La Terre n'a aucune douleur que le Ciel ne puisse guérir. -- Cantique",
    hi_title: "स्वर्ग दुःख को चंगा करता है",
    hi_content: "पृथ्वी पर कोई दुःख नहीं है जिसे स्वर्ग चंगा नहीं कर सकता। -- भजन",
    zh_title: "Tiāntáng Zhìyù Bēishāng",
    zh_content: "Shìjiān méiyǒu tiāntáng bùnéng zhìyù de bēishāng. -- Shèngshī"
});

MATCH (t:THOUGHT {name: "thought.HEAVEN HEALS SORROW"})
MATCH (c:CONTENT {name: "content.HEAVEN HEALS SORROW"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN HEALS SORROW" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.HEAVEN HEALS SORROW"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEAVEN HEALS SORROW" }]->(child);
```

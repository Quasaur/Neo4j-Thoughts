---
name: "thought.MARRIAGE RELIGIOUS INSTITUTION"
alias: "Thought: Marriage Religious Institution"
type: THOUGHT
en_content: "Congress shall make no law regarding the practice of religion...marriage is a RELIGIOUS institution!"
parent: "topic.RELIGION"
tags:
- marriage
- religion
- law
- institution
- history
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Sep-2013)
CREATE (t:THOUGHT {
    name: "thought.MARRIAGE RELIGIOUS INSTITUTION",
    alias: "Thought: Marriage Religious Institution",
    parent: "topic.RELIGION",
    tags: ['marriage', 'religion', 'law', 'institution', 'history'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MARRIAGE RELIGIOUS INSTITUTION",
    en_title: "Marriage Religious Institution",
    en_content: "Congress shall make no law regarding the practice of religion...marriage is a RELIGIOUS institution!",
    es_title: "Matrimonio Institución Religiosa",
    es_content: "El Congreso no hará ley alguna respecto a la práctica de la religión...¡el matrimonio es una institución RELIGIOSA!",
    fr_title: "Mariage Institution Religieuse",
    fr_content: "Le Congrès ne fera aucune loi concernant la pratique de la religion...le mariage est une institution RELIGIEUSE !",
    hi_title: "विवाह धार्मिक संस्था",
    hi_content: "कांग्रेस धर्म के अभ्यास के संबंध में कोई कानून नहीं बनाएगी...विवाह एक धार्मिक संस्था है!",
    zh_title: "Hunyin Zongjiao Jigou",
    zh_content: "Guohui bu de zhiding ren he guanyu zongjiao shijian de falü...hunyin shi yi ge ZONGJIAO jigou!"
});

MATCH (t:THOUGHT {name: "thought.MARRIAGE RELIGIOUS INSTITUTION"})
MATCH (c:CONTENT {name: "content.MARRIAGE RELIGIOUS INSTITUTION"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.MARRIAGE RELIGIOUS INSTITUTION" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.MARRIAGE RELIGIOUS INSTITUTION"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION->MARRIAGE RELIGIOUS INSTITUTION" }]->(child);
```

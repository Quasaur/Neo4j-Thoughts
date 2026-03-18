---
type: THOUGHT
name: "thought.MARRIAGE RELIGIOUS INSTITUTION"
alias: "Thought: Marriage Religious Institution"
parent: "topic.RELIGION"
en_content: "Congress shall make no law regarding the practice of religion...marriage is a RELIGIOUS institution!"
tags: ["marriage", "religion", "law", "institution", "history"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Sep-2013)
CREATE (t:THOUGHT {    name: "thought.MARRIAGE RELIGIOUS INSTITUTION",
    alias: "Thought: Marriage Religious Institution",
    parent: "topic.RELIGION",
    tags: ['marriage', 'religion', 'law', 'institution', 'history'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.MARRIAGE RELIGIOUS INSTITUTION",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MARRIAGE RELIGIOUS INSTITUTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->MARRIAGE RELIGIOUS INSTITUTION"
RETURN t, parent;
```

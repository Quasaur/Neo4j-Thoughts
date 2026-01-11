---
name: "thought.EVIL_WAS_NECESSARY"
alias: "Thought: EVIL WAS NECESSARY"
type: THOUGHT
parent: topic.EVIL
tags:
- lambofgod
- evil
- salvation
- forgiveness
- jesuschrist
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.EVIL_WAS_NECESSARY",
    alias: "Thought: EVIL WAS NECESSARY",
    parent: "topic.EVIL",
    tags: ["lambofgod", "evil", "salvation", "forgiveness", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVIL_WAS_NECESSARY",
    en_title: "EVIL WAS NECESSARY",
    en_content: "…for there was no other way…
…to sacrifice The Lamb of GOD.",
    es_title: "EL MAL ERA NECESARIO",
    es_content: "…porque no había otra manera…
…para sacrificar El Cordero de DIOS.",
    fr_title: "LE MAL ÉTAIT NÉCESSAIRE",
    fr_content: "…car il n’y avait pas d’autre moyen…
…pour sacrifier L'Agneau de DIEU.",
    hi_title: "बुराई आवश्यक थी",
    hi_content: "...क्योंकि कोई दूसरा रास्ता नहीं था...
...परमेश्वर के मेम्ने की बलि चढ़ाने के लिए।",
    zh_title: "xié è shì bì yào de",
    zh_content: "…… yīn wèi méi yǒu qí tā bàn fǎ ……
…… xī shēng shàng dì de gāo yáng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVIL_WAS_NECESSARY" AND c.name = "content.EVIL_WAS_NECESSARY"
MERGE (t)-[:HAS_CONTENT {name: "edge.EVIL_WAS_NECESSARY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.EVIL_WAS_NECESSARY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->EVIL_WAS_NECESSARY"}]->(child);
```

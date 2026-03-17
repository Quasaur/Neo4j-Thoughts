---
type: THOUGHT
name: "thought.EVIL WAS NECESSARY"
alias: "Thought: Evil Was Necessary"
parent: "topic.EVIL"
en_content: |
  …for there was no other way…
  …to sacrifice The Lamb of GOD."
tags: ["lamb_of_god", "evil", "salvation", "forgiveness", "jesus_christ"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.EVIL WAS NECESSARY",
    alias: "Thought: Evil Was Necessary",
    parent: "topic.EVIL",
    tags: ["lamb_of_god", "evil", "salvation", "forgiveness", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVIL WAS NECESSARY",
    ctype: "THOUGHT",
    en_title: "Evil Was Necessary",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EVIL WAS NECESSARY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->EVIL WAS NECESSARY"
RETURN t, parent;
```

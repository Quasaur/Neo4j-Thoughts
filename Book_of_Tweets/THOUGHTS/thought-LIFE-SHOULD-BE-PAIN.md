---
type: THOUGHT
name: "thought.LIFE SHOULD BE PAIN"
alias: "Thought: Life Should Be Pain"
parent: "topic.PHILOSOPHY"
en_content: "Many will tell you life is pain; not many will say it should be. It should be."
tags: ["pain", "life", "philosophy", "suffering", "truth"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2013d)
CREATE (t:THOUGHT {    name: "thought.LIFE SHOULD BE PAIN",
    alias: "Thought: Life Should Be Pain",
    parent: "topic.PHILOSOPHY",
    tags: ['pain', 'life', 'philosophy', 'suffering', 'truth'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.LIFE SHOULD BE PAIN",
    ctype: "THOUGHT",
    en_title: "Life Should Be Pain",
    en_content: "Many will tell you life is pain; not many will say it should be. It should be.",
    es_title: "La Vida Debe Ser Dolor",
    es_content: "Muchos te dirán que la vida es dolor; no muchos dirán que debe serlo. Debe serlo.",
    fr_title: "La Vie Doit Être Souffrance",
    fr_content: "Beaucoup vous diront que la vie est souffrance ; peu nombreux sont ceux qui diront qu'elle doit l'être. Elle doit l'être.",
    hi_title: "जीवन पीड़ा होना चाहिए",
    hi_content: "बहुत से लोग आपसे कहेंगे कि जीवन पीड़ा है; बहुत कम कहेंगे कि यह होना चाहिए। यह होना चाहिए।",
    zh_title: "Shēngmìng Yīnggāi Shì Tòngkǔ",
    zh_content: "Xǔduō rén huì gàosu nǐ shēngmìng shì tòngkǔ de; dàn bù duō de rén huì shuō tā yīnggāi shì. Tā yīnggāi shì."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIFE SHOULD BE PAIN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->LIFE SHOULD BE PAIN"
RETURN t, parent;
```

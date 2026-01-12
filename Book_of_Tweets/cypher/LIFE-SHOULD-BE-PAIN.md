---
name: "thought.LIFE SHOULD BE PAIN"
alias: "Thought: Life Should Be Pain"
type: THOUGHT
en_content: "Many will tell you life is pain; not many will say it should be. It should be."
parent: "topic.PHILOSOPHY"
tags:
- pain
- life
- philosophy
- suffering
- truth
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2013d)
CREATE (t:THOUGHT {
    name: "thought.LIFE SHOULD BE PAIN",
    alias: "Thought: Life Should Be Pain",
    parent: "topic.PHILOSOPHY",
    tags: ['pain', 'life', 'philosophy', 'suffering', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LIFE SHOULD BE PAIN",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LIFE SHOULD BE PAIN" AND c.name = "content.LIFE SHOULD BE PAIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIFE SHOULD BE PAIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.LIFE SHOULD BE PAIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >LIFE SHOULD BE PAIN" }]->(child);
```

---
type: THOUGHT
name: "thought.LIVING IN CHRISTS RIGHTEOUSNESS"
alias: "Thought: Living In Christs Righteousness"
parent: "topic.GRACE"
en_content: "I live--not with my own righteousness, but with Christ's; for God placed me in Christ when He obeyed...now He obeys in me!"
tags: ["righteousness", "grace", "christ", "life", "salvation"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LIVING IN CHRISTS RIGHTEOUSNESS",
    alias: "Thought: Living In Christs Righteousness",
    parent: "topic.GRACE",
    tags: ['righteousness', 'grace', 'christ', 'life', 'salvation'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LIVING IN CHRISTS RIGHTEOUSNESS",
    ctype: "THOUGHT",
    en_title: "Living In Christs Righteousness",
    en_content: "I live--not with my own righteousness but with Christ's; for God placed me in Christ when He obeyed...now He obeys in me!",
    es_title: "Viviendo En La Justicia De Cristo",
    es_content: "Yo vivo--no con mi propia justicia sino con la de Cristo; porque Dios me puso en Cristo cuando Él obedeció...¡ahora Él obedece en mí!",
    fr_title: "Vivre Dans La Justice Du Christ",
    fr_content: "Je vis--non avec ma propre justice mais avec celle du Christ; car Dieu m'a placé en Christ quand Il a obéi...maintenant Il obéit en moi!",
    hi_title: "मसीह की धार्मिकता में जीना",
    hi_content: "मैं जीता हूँ--अपनी धार्मिकता से नहीं बल्कि मसीह की धार्मिकता से; क्योंकि परमेश्वर ने मुझे मसीह में रखा जब उसने आज्ञा मानी...अब वह मुझमें आज्ञा मानता है!",
    zh_title: "Huó Zài Jīdū De Gōngyì Zhōng",
    zh_content: "Wǒ huó zhe--bù shì kào wǒ zìjǐ de gōngyì ér shì kào Jīdū de gōngyì; yīnwèi Shén jiāng wǒ fàng zài Jīdū lǐ dāng tā shùnfú shí...xiànzài tā zài wǒ lǐmiàn shùnfú!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIVING IN CHRISTS RIGHTEOUSNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->LIVING IN CHRISTS RIGHTEOUSNESS"
RETURN t, parent;
```

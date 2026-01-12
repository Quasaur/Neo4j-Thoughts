---
name: "thought.LIVING IN CHRISTS RIGHTEOUSNESS"
alias: "Thought: Living In Christs Righteousness"
type: THOUGHT
en_content: "I live--not with my own righteousness but with Christ's; for God placed me in Christ when He obeyed...now He obeys in me!"
parent: "topic.GRACE"
tags:
- righteousness
- grace
- christ
- life
- salvation
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.LIVING IN CHRISTS RIGHTEOUSNESS",
    alias: "Thought: Living In Christs Righteousness",
    parent: "topic.GRACE",
    tags: ['righteousness', 'grace', 'christ', 'life', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LIVING IN CHRISTS RIGHTEOUSNESS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LIVING IN CHRISTS RIGHTEOUSNESS" AND c.name = "content.LIVING IN CHRISTS RIGHTEOUSNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIVING IN CHRISTS RIGHTEOUSNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.LIVING IN CHRISTS RIGHTEOUSNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LIVING IN CHRISTS RIGHTEOUSNESS" }]->(child);
```

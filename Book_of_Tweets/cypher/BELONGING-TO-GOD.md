---
name: "thought.BELONGING TO GOD"
alias: "Thought: Belonging To God"
type: THOUGHT
en_content: "If we don't belong to God, we belong to ourselves...and shall perish in ourselves because we choose not to live in God."
parent: "topic.HUMANITY"
tags:
- belonging
- identity
- choice
- life
- god
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-May-2011)
CREATE (t:THOUGHT {
    name: "thought.BELONGING TO GOD",
    alias: "Thought: Belonging To God",
    parent: "topic.HUMANITY",
    tags: ['belonging', 'identity', 'choice', 'life', 'god'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BELONGING TO GOD",
    en_title: "Belonging To God",
    en_content: "If we don't belong to God, we belong to ourselves...and shall perish in ourselves because we choose not to live in God.",
    es_title: "Perteneciendo a Dios",
    es_content: "Si no pertenecemos a Dios, nos pertenecemos a nosotros mismos... y pereceremos en nosotros mismos porque elegimos no vivir en Dios.",
    fr_title: "Appartenir à Dieu",
    fr_content: "Si nous n'appartenons pas à Dieu, nous nous appartenons à nous-mêmes... et nous périrons en nous-mêmes parce que nous choisissons de ne pas vivre en Dieu.",
    hi_title: "परमेश्वर से संबंधित होना",
    hi_content: "यदि हम परमेश्वर के नहीं हैं, तो हम अपने ही हैं... और हम अपने आप में नष्ट हो जाएंगे क्योंकि हम परमेश्वर में जीने का चयन नहीं करते।",
    zh_title: "Shǔyú Shàngdì 属于上帝",
    zh_content: "Rúguǒ wǒmen bù shǔyú Shàngdì, wǒmen jiù shǔyú zìjǐ... bìngqiě wǒmen jiāng zài zìjǐ zhōng huǐmiè, yīnwèi wǒmen xuǎnzé bù zài Shàngdì lǐ shēnghuó. 如果我们不属于上帝，我们就属于自己...并且我们将在自己中毁灭，因为我们选择不在上帝里生活。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BELONGING TO GOD" AND c.name = "content.BELONGING TO GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BELONGING TO GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.BELONGING TO GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >BELONGING TO GOD" }]->(child);
```

---
type: THOUGHT
name: "thought.PRAYER MAKES HUMAN"
alias: "Thought: Prayer Makes Human"
parent: "topic.SPIRITUALITY"
en_content: "Prayer, above all else, is what makes me Human; without it, I'm just an animal."
tags: ["prayer", "humanity", "animal", "spirituality", "essence"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013i)
CREATE (t:THOUGHT {    name: "thought.PRAYER MAKES HUMAN",
    alias: "Thought: Prayer Makes Human",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'humanity', 'animal', 'spirituality', 'essence'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.PRAYER MAKES HUMAN",
    ctype: "THOUGHT",
    en_title: "Prayer Makes Human",
    en_content: "Prayer, above all else, is what makes me Human; without it, I'm just an animal.",
    es_title: "La Oración Nos Hace Humanos",
    es_content: "La oración, por encima de todo, es lo que me hace Humano; sin ella, soy solo un animal.",
    fr_title: "La Prière Rend Humain",
    fr_content: "La prière, avant tout, est ce qui me rend Humain; sans elle, je ne suis qu'un animal.",
    hi_title: "प्रार्थना मनुष्य बनाती है",
    hi_content: "प्रार्थना, सब से बढ़कर, वह है जो मुझे मनुष्य बनाती है; इसके बिना, मैं केवल एक पशु हूँ।",
    zh_title: "Qí dǎo shǐ rén chéng wéi rén",
    zh_content: "Qí dǎo, gāo yú yī qiē, shì shǐ wǒ chéng wéi rén de dōng xī; méi yǒu tā, wǒ zhǐ shì yī zhī dòng wù."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRAYER MAKES HUMAN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->PRAYER MAKES HUMAN"
RETURN t, parent;
```

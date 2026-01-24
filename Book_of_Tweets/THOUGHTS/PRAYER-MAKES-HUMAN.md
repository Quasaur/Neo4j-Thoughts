---
name: "thought.PRAYER MAKES HUMAN"
alias: "Thought: Prayer Makes Human"
type: THOUGHT
en_content: "Prayer, above all else, is what makes me Human; without it, I'm just an animal."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- humanity
- animal
- spirituality
- essence
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013i)
CREATE (t:THOUGHT {
    name: "thought.PRAYER MAKES HUMAN",
    alias: "Thought: Prayer Makes Human",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'humanity', 'animal', 'spirituality', 'essence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER MAKES HUMAN",
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

MATCH (t:THOUGHT {name: "thought.PRAYER MAKES HUMAN"})
MATCH (c:CONTENT {name: "content.PRAYER MAKES HUMAN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER MAKES HUMAN" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.PRAYER MAKES HUMAN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->PRAYER MAKES HUMAN" }]->(child);
```

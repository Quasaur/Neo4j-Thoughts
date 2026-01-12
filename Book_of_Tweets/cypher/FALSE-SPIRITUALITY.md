---
name: "thought.FALSE SPIRITUALITY"
alias: "Thought: False Spirituality"
type: THOUGHT
en_content: "False Spirituality: placing the Devil around every corner, under every rock and behind every bush to cover defects of character."
parent: "topic.SPIRITUALITY"
tags:
- spirituality
- deception
- devil
- character
- excuse
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.FALSE SPIRITUALITY",
    alias: "Thought: False Spirituality",
    parent: "topic.SPIRITUALITY",
    tags: ['spirituality', 'deception', 'devil', 'character', 'excuse'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FALSE SPIRITUALITY",
    en_title: "False Spirituality",
    en_content: "False Spirituality: placing the Devil around every corner, under every rock and behind every bush to cover defects of character.",
    es_title: "Falsa Espiritualidad",
    es_content: "Falsa espiritualidad: poner al Diablo en cada esquina, bajo cada piedra y detrás de cada arbusto para cubrir defectos de carácter.",
    fr_title: "Fausse Spiritualité",
    fr_content: "Fausse spiritualité : placer le Diable à chaque coin, sous chaque pierre et derrière chaque buisson pour couvrir les défauts de caractère.",
    hi_title: "झूठी आध्यात्मिकता",
    hi_content: "झूठी आध्यात्मिकता: चरित्र की कमियों को छिपाने के लिए हर कोने, हर पत्थर के नीचे और हर झाड़ी के पीछे शैतान को रखना।",
    zh_title: "Jiǎ língxìng 假灵性",
    zh_content: "Jiǎ língxìng: wèile yǎnshì xìngé shàng de quēxiàn, ér bǎ móguǐ fàng zài měi gè jiǎo luò, měi kuài shítóu xià, hé měi gè guàn mù hòu. 假灵性：为了隐藏性格上的缺陷，而把魔鬼放在每个角落，每块石头下，和每个灌木后。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FALSE SPIRITUALITY" AND c.name = "content.FALSE SPIRITUALITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FALSE SPIRITUALITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.FALSE SPIRITUALITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >FALSE SPIRITUALITY" }]->(child);
```

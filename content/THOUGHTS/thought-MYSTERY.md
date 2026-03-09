---
type: THOUGHT
name: "thought.MYSTERY"
alias: "Thought: Mystery"
parent: "topic.PSYCHOLOGY"
tags: ["wife", "mystery", "understanding", "life", "gift"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MYSTERY",
    alias: "Thought: Mystery",
    parent: "topic.PSYCHOLOGY",
    tags: ["wife", "mystery", "understanding", "life", "gift"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MYSTERY",
    ctype: "THOUGHT",
    en_title: "Mystery",
 es_title: "MISTERIO",
 fr_title: "MYSTÈRE",
 hi_title: "रहस्य",
 zh_title: "shén mì",
    en_content: "",
 es_content: "Hay tantas cosas sobre mi esposa que no entiendo...
...pero cuando estamos solos y en silencio, ¡ella me da VIDA!",
 fr_content: "Il y a tellement de choses sur ma femme que je ne comprends pas...
...mais quand nous sommes seuls ensemble et tranquilles, elle me donne la VIE !",
 hi_content: "मेरी पत्नी के बारे में बहुत सी बातें हैं जो मुझे समझ नहीं आती...
...लेकिन जब हम एक साथ अकेले और शांत होते हैं, तो वह मुझे जीवन देती है!",
 zh_content: "wǒ de qī zǐ yǒu hěn duō shì qíng wǒ bù míng bái ......
... dàn shì dāng wǒ men dān dú ān jìng dì zài yì qǐ shí ， tā gěi le wǒ shēng mìng ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MYSTERY" AND c.name = "content.MYSTERY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.MYSTERY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.MYSTERY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->MYSTERY"}]->(child);
```
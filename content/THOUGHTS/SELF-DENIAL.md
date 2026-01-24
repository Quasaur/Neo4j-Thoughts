---
name: "thought.SELF_DENIAL"
alias: "Thought: SELF-DENIAL"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- self
- denial
- humility
- deprecation
- worship
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SELF_DENIAL",
    alias: "Thought: SELF-DENIAL",
    parent: "topic.ATTITUDE",
    tags: ["self", "denial", "humility", "deprecation", "worship"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SELF_DENIAL",
    en_title: "SELF-DENIAL",
    en_content: "# Thought: SELF-DENIAL
[!Thought-en]
If you can't say \"No\" to Self, you can't say \"Yes\" to God.

[!Pensamiento-es]
Si no puedes decir “No” a ti mismo, no puedes decir “Sí” a Dios.

[!Pensée-fr]
Si vous ne pouvez pas dire « Non » à vous-même, vous ne pouvez pas dire « Oui » à Dieu.

[!सोचा-hi]
यदि आप स्वयं को \"नहीं\" नहीं कह सकते, तो आप ईश्वर को \"हाँ\" भी नहीं कह सकते।

[!思考-zh]
如果你不能对自己说“不”，你就不能对上帝说“是”。",
    es_title: "ABNEGACIÓN",
    es_content: "#Pensamiento: AUTONEGACIÓN
[!Pensamiento-es]
Si no puedes decir \"No\" a ti mismo, no puedes decir \"Sí\" a Dios.

[!Pensamiento-es]
Si no puedes decir “No” a ti mismo, no puedes decir “Sí” a Dios.

[!Pensée-fr]
Si no puedes decir \"non\" a ti mismo, no puedes decir \"oui\" a dieu.

[!सोचा-hola]
यदि आप स्वयं को \"नहीं\" नहीं कह सकते, तो आप ईश्वर को \"हँ\" भी नहीं कह सकते।

[!Piensa-zh]
Si no puedes decirte \"no\" a ti mismo, no puedes decirle \"sí\" a Dios.",
    fr_title: "ABNÉGATION",
    fr_content: "#Pensée : DÉNI DE SOI
[!Pensée-fr]
Si vous ne pouvez pas dire « Non » à vous-même, vous ne pouvez pas dire « Oui » à Dieu.

[!Pensamiento-es]
Si vous ne pouvez pas dire « Non » à toi, vous ne pouvez pas dire « Sí » à Dieu.

[!Pensée-fr]
Si vous ne pouvez pas dire « Non » à vous-même, vous ne pouvez pas dire « Oui » à Dieu.

[!सोचा-salut]
यदि आप स्वयं को \"नहीं\" नहीं कह सकते, तो आप ईश्वर को \"हँ\" भी नहीं कह सकते।

[!Think-zh]
Si vous ne pouvez pas vous dire « non », vous ne pouvez pas dire « oui » à Dieu.",
    hi_title: "आत्मोत्सर्ग",
    hi_content: "#विचार: आत्म-त्याग
[!विचार-एन]
यदि आप स्वयं को \"नहीं\" नहीं कह सकते, तो आप भगवान को \"हाँ\" नहीं कह सकते।

[!पेन्सामिएंटो-एस]
यदि कोई व्यक्ति \"नहीं\" का निर्णय करता है, तो कोई भी व्यक्ति \"नहीं\" का निर्णय लेता है।

[!पेन्सी-fr]
यदि आपने मुझे बहुत बुरा महसूस कराया है \"नहीं\" तो आप मुझे नहीं पा सकते हैं, यदि आप मुझे नहीं पा सकते हैं \"नहीं\"।

[!सोचा-हाय]
यदि आप स्वयं को \"नहीं\" नहीं कह सकते, तो आप ईश्वर को \"हां\" भी नहीं कह सकते।

[!सोचें-zh]
यदि आप स्वयं को \"नहीं\" नहीं कह सकते, तो आप भगवान को \"हाँ\" नहीं कह सकते।",
    zh_title: "zì wǒ fǒu dìng",
    zh_content: "# Thought: SELF-DENIAL
[!Thought-en]
If you can't say \"No\" to Self, you can't say \"Yes\" to God.

[!Pensamiento-es]
Si no puedes decir “No” a ti mismo, no puedes decir “Sí” a Dios.

[!Pensée-fr]
Si vous ne pouvez pas dire « Non » à vous-même, vous ne pouvez pas dire « Oui » à Dieu.

[!सोचा-hi]
यदि आप स्वयं को \"नहीं\" नहीं कह सकते, तो आप ईश्वर को \"हाँ\" भी नहीं कह सकते।

[! sī kǎo -zh]
 rú guǒ nǐ bù néng duì zì jǐ shuō “ bù ”， nǐ jiù bù néng duì shàng dì shuō “ shì ”。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SELF_DENIAL" AND c.name = "content.SELF_DENIAL"
MERGE (t)-[:HAS_CONTENT {name: "edge.SELF_DENIAL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.SELF_DENIAL"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->SELF_DENIAL"}]->(child);
```

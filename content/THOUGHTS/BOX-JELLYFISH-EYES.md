---
name: "thought.BOX JELLYFISH EYES"
alias: "Thought: Box Jellyfish Eyes"
type: THOUGHT
en_content: "The box jellyfish--nature's most poisonous creature--has 24 eyes and 360-degree vision...God is great!"
parent: topic.BIOLOGY
tags:
  - creation
  - nature
  - jellyfish
  - design
  - power
level: 6
neo4j: true
ptopic: "[[topic-BIOLOGY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Aug-2011a)
CREATE (t:THOUGHT {
    name: "thought.BOX JELLYFISH EYES",
    alias: "Thought: Box Jellyfish Eyes",
    parent: "topic.BIOLOGY",
    tags: ['creation', 'nature', 'jellyfish', 'design', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BOX JELLYFISH EYES",
    en_title: "Box Jellyfish Eyes",
    en_content: "The box jellyfish--nature's most poisonous creature--has 24 eyes and 360-degree vision...God is great!",
    es_title: "Ojos de la Medusa de Caja",
    es_content: "La medusa de caja--la criatura más venenosa de la naturaleza--tiene 24 ojos y visión de 360 grados... ¡Dios es grande!",
    fr_title: "Yeux de la Méduse-boîte",
    fr_content: "La méduse-boîte--la créature la plus venimeuse de la nature--a 24 yeux et une vision à 360 degrés... Dieu est grand !",
    hi_title: "बॉक्स जेलीफिश की आंखें",
    hi_content: "बॉक्स जेलीफिश--प्रकृति का सबसे जहरीला जीव--के पास 24 आंखें और 360-डिग्री दृष्टि है... परमेश्वर महान है!",
    zh_title: "Xiāngxíng shāyú de yǎnjuāng 箱形水母的眼睛",
    zh_content: "Xiāngxíng shāyú--dàzìrán zuì yǒudú de shēngwù--yǒu 24 zhī yǎnjuāng hé 360 dù shìjào... Shàngdì zhēn wěidà! 箱形水母--大自然最有毒的生物--有24只眼睛和360度视角...上帝真伟大！"
});

MATCH (t:THOUGHT {name: "thought.BOX JELLYFISH EYES"})
MATCH (c:CONTENT {name: "content.BOX JELLYFISH EYES"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.BOX JELLYFISH EYES" }]->(c);

MATCH (parent:TOPIC {name: "topic.BIOLOGY"})
MATCH (child:THOUGHT {name: "thought.BOX JELLYFISH EYES"})
MERGE (parent)-[:HAS_THOUGHT { "name": "BIOLOGY->BOX JELLYFISH EYES" }]->(child);
```

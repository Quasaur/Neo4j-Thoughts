---
type: THOUGHT
name: "thought.MURDER"
alias: "Thought: Murder"
parent: "topic.PSYCHOLOGY"
tags: ["crime", "punishment", "intent", "kill", "judgment"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MURDER",
    alias: "Thought: Murder",
    parent: "topic.PSYCHOLOGY",
    tags: ["crime", "punishment", "intent", "kill", "judgment"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MURDER",
    ctype: "THOUGHT",
    en_title: "Murder",
 es_title: "ASESINATO",
 fr_title: "MEURTRE",
 hi_title: "हत्या",
 zh_title: "móu shā",
    en_content: "",
 es_content: "Si tienes edad suficiente para asesinar con intención, tienes edad suficiente para ser ejecutado con prejuicios extremos.",
 fr_content: "Si vous êtes assez vieux pour commettre un meurtre intentionnel, vous êtes assez vieux pour être exécuté avec des préjugés extrêmes.",
 hi_content: "यदि आप इरादे से हत्या करने के लिए पर्याप्त बूढ़े हैं, तो आप अत्यधिक पूर्वाग्रह के साथ मारे जाने के लिए भी काफी बूढ़े हैं।",
 zh_content: "rú guǒ nǐ yǐ jīng dào le kě yǐ xù yì móu shā de nián jì ， nà me nǐ yě yǐ jīng dào le kě yǐ dài zhe jí duān piān jiàn bèi chǔ jué de nián jì le 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MURDER" AND c.name = "content.MURDER"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.MURDER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.MURDER"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->MURDER"}]->(child);
```
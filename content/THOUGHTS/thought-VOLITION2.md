---
type: THOUGHT
name: "thought.VOLITION2"
alias: "Thought: Second Volition"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["freedom", "volition", "free_will", "misused", "abused"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.VOLITION2",
    alias: "Thought: Second Volition",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "free_will", "misused", "abused"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION2",
    ctype: "THOUGHT",
    en_title: "Second Volition",
 es_title: "SEGUNDA VOLICIÓN",
 fr_title: "DEUXIÈME VOLITION",
 hi_title: "दूसरी इच्छा",
 zh_title: "dì èr cì yì yuàn",
    en_content: "",
 es_content: "¿Será que Dios le dio a la humanidad catorce mil años de libre albedrío; para que cuando Él nos lo quite... ¿no lo extrañemos?",
 fr_content: "Se pourrait-il que Dieu ait donné à l’humanité quatorze mille ans de libre arbitre ; pour que quand Il l'enlèvera... nous ne le manquerons pas ?",
 hi_content: "क्या ऐसा हो सकता है कि ईश्वर ने मानवता को चौदह हजार वर्ष की स्वतंत्र इच्छा दी हो; ताकि जब वह इसे ले जाए...हम इसे चूक न जाएँ?",
 zh_content: "nán dào shàng dì gěi le rén lèi yī wàn sì qiān nián de zì yóu yì zhì ？ zhè yàng dāng tā bǎ tā ná zǒu shí …… wǒ men jiù bú huì cuò guò tā ？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION2" AND c.name = "content.VOLITION2"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.VOLITION2"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION2"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->VOLITION2"}]->(child);
```
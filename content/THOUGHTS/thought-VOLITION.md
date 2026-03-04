---
type: THOUGHT
name: "thought.VOLITION"
alias: "Thought: Volition"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["paradox", "volition", "free_will", "fullness", "jesus_christ"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.VOLITION",
    alias: "Thought: Volition",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["paradox", "volition", "free_will", "fullness", "jesus_christ"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION",
    ctype: "THOUGHT",
    en_title: "Volition",
 es_title: "VOLUNTAD",
 fr_title: "VOLITION",
 hi_title: "इच्छाशक्ति",
 zh_title: "yì zhì",
    en_content: "",
 es_content: "¡Tu voluntad nunca es más libre que cuando está bajo el control absoluto del Espíritu Santo de Jesucristo! 
Juan 14:11",
 fr_content: "Votre volonté n’est jamais plus libre que lorsqu’elle est sous le contrôle absolu du Saint-Esprit de Jésus-Christ ! 
Jean 14:11",
 hi_content: "आपकी इच्छा कभी भी इससे अधिक स्वतंत्र नहीं होती जब यह यीशु मसीह की पवित्र आत्मा के पूर्ण नियंत्रण में होती है! 
यूहन्ना 14:11",
 zh_content: "dāng nǐ de yì zhì chǔ yú yē sū jī dū shèng líng de jué duì kòng zhì zhī xià shí ， nǐ de yì zhì shì zuì zì yóu de ！ 
 yuē hàn fú yīn  14:11"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION" AND c.name = "content.VOLITION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.VOLITION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->VOLITION"}]->(child);
```
---
type: THOUGHT
name: "thought.CONTENTMENT"
alias: "Thought: CONTENTMENT"
parent: "topic.ATTITUDE"
tags: ["contentment", "acceptance", "carefree", "failure", "faith"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.CONTENTMENT",
    alias: "Thought: CONTENTMENT",
    parent: "topic.ATTITUDE",
    tags: ["contentment", "acceptance", "carefree", "failure", "faith"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONTENTMENT",
    ctype: "THOUGHT",
    en_title: "CONTENTMENT",
 es_title: "CONTENTAMIENTO",
 fr_title: "CONTENTEMENT",
 hi_title: "संतोष",
 zh_title: "mǎn yì",
    en_content: "",
 es_content: "Juego mi mejor ajedrez cuando no me importa ganar... o mejor dicho, cuando no tengo ansiedad por cometer errores.",
 fr_content: "Je joue de mon mieux aux échecs quand je ne me soucie pas de gagner… ou plutôt, quand je n’ai aucune angoisse à l’idée de faire des erreurs.",
 hi_content: "मैं अपना सर्वश्रेष्ठ शतरंज तब खेलता हूं जब मुझे जीत की परवाह नहीं होती... या यूँ कहें कि, जब मुझे गलतियाँ करने की कोई चिंता नहीं होती।",
 zh_content: "dāng wǒ bù guān xīn shèng lì shí ， huò zhě gèng què qiè dì shuō ， dāng wǒ bù dān xīn fàn cuò wù shí ， wǒ huì xià zuì hǎo de qí 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CONTENTMENT" AND c.name = "content.CONTENTMENT"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.CONTENTMENT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.CONTENTMENT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->CONTENTMENT"}]->(child);
```
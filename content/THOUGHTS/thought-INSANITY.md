---
type: THOUGHT
name: "thought.INSANITY"
alias: "Thought: Insanity"
parent: "topic.PSYCHOLOGY"
tags: ["insanity", "madness", "delusion", "narcissism", "fooliishness"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INSANITY",
    alias: "Thought: Insanity",
    parent: "topic.PSYCHOLOGY",
    tags: ["insanity", "madness", "delusion", "narcissism", "fooliishness"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INSANITY",
    ctype: "THOUGHT",
    en_title: "Insanity",
 es_title: "LOCURA",
 fr_title: "FOLIE",
 hi_title: "पागलपन",
 zh_title: "fēng kuáng",
    en_content: "",
 es_content: "¡Lucifer tuvo el descaro absoluto de pedirle a su CREADOR que lo adorara!
En la Corte del Cielo la locura y el pecado son lo mismo.",
 fr_content: "Lucifer a eu le culot absolu de demander à son CRÉATEUR de l'adorer !
Dans la Cour du Ciel, la folie et le péché ne font qu'un.",
 hi_content: "लूसिफ़ेर के पास अपने निर्माता से उसकी पूजा करने के लिए कहने का अदम्य साहस था!
स्वर्ग के दरबार में पागलपन और पाप एक ही हैं।",
 zh_content: "lù xī fǎ jìng rán hòu yán wú chǐ dì yāo qiú tā de chuàng zào zhě chóng bài tā ！
 zài tiān tíng lǐ ， fēng kuáng hé zuì è shì yī huí shì 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INSANITY" AND c.name = "content.INSANITY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.INSANITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.INSANITY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->INSANITY"}]->(child);
```
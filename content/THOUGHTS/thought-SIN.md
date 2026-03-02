---
type: THOUGHT
name: "thought.SIN"
alias: "Thought: SIN"
parent: "topic.GRACE"
tags: ["grace", "gospel", "love", "power", "jesus_christ"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SIN",
    alias: "Thought: SIN",
    parent: "topic.GRACE",
    tags: ["grace", "gospel", "love", "power", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIN",
    ctype: "THOUGHT",
    en_title: "SIN",
 es_title: "PECADO",
 fr_title: "PÉCHÉ",
 hi_title: "पाप",
 zh_title: "zuì",
    en_content: "",
 es_content: "La gracia no es que DIOS sea débil ante el pecado; ¡La gracia es DIOS haciéndote más fuerte que el pecado!",
 fr_content: "La grâce n’est pas que DIEU soit faible envers le péché ; La grâce, c'est DIEU qui vous rend plus fort que le péché !",
 hi_content: "पाप के प्रति ईश्वर का कमजोर होना अनुग्रह नहीं है; ईश्वर की कृपा ही आपको पाप से अधिक मजबूत बनाती है!",
 zh_content: "ēn diǎn bú shì shén duì zuì de ruǎn ruò ； ér shì shén duì zuì de ruǎn ruò 。 ēn diǎn shì shén ràng nǐ bǐ zuì gèng qiáng dà ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SIN" AND c.name = "content.SIN"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.SIN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.SIN"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->SIN"}]->(child);
```
---
name: "thought.THE_LAST_WORD"
alias: "Thought: THE LAST WORD"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- gospel
- jesuschrist
- livingword
- lastword
- wordofgod
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_LAST_WORD",
    alias: "Thought: THE LAST WORD",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "jesuschrist", "livingword", "lastword", "wordofgod"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE_LAST_WORD",
    en_title: "THE LAST WORD",
    en_content: "Yehoshua Ha Meshiach: Jesus The Christ: The Living Word...The Last Word!",
    es_title: "LA ÚLTIMA PALABRA",
    es_content: "Yehoshua Ha Meshiach: Jesús El Cristo: La Palabra Viva... ¡La Última Palabra!",
    fr_title: "LE DERNIER MOT",
    fr_content: "Yehoshua Ha Meshiach : Jésus le Christ : La Parole vivante... La Dernière Parole !",
    hi_title: "आखिरी शब्द",
    hi_content: "येहोशुआ हा मेशियाच: जीसस द क्राइस्ट: द लिविंग वर्ड...द लास्ट वर्ड!",
    zh_title: "zuì hòu yī jù huà",
    zh_content: "Yehoshua Ha Meshiach： yē sū jī dū ： huó shēng shēng de dào …… zuì hòu de dào ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_LAST_WORD" AND c.name = "content.THE_LAST_WORD"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_LAST_WORD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.THE_LAST_WORD"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GOSPEL->THE_LAST_WORD"}]->(child);
```

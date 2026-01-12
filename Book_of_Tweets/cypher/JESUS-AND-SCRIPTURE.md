---
name: "thought.JESUS AND SCRIPTURE"
alias: "Thought: Jesus And Scripture"
type: THOUGHT
en_content: "Jesus treated the Scriptures as the Testimony of God...I would be foolish to do otherwise."
parent: "topic.TRUTH"
tags:
- jesus
- scripture
- bible
- truth
- testimony
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.JESUS AND SCRIPTURE",
    alias: "Thought: Jesus And Scripture",
    parent: "topic.TRUTH",
    tags: ['jesus', 'scripture', 'bible', 'truth', 'testimony'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.JESUS AND SCRIPTURE",
    en_title: "Jesus And Scripture",
    en_content: "Jesus treated the Scriptures as the Testimony of God...I would be foolish to do otherwise.",
    es_title: "Jesús Y Las Escrituras",
    es_content: "Jesús trató las Escrituras como el Testimonio de Dios...Sería necio de mi parte hacer lo contrario.",
    fr_title: "Jésus Et L'Écriture",
    fr_content: "Jésus a traité les Écritures comme le Témoignage de Dieu...Je serais fou de faire autrement.",
    hi_title: "यीशु और धर्मग्रंथ",
    hi_content: "यीशु ने धर्मग्रंथों को परमेश्वर की गवाही के रूप में माना...मैं अन्यथा करने में मूर्ख होऊंगा।",
    zh_title: "Yesu Yu Shengjing",
    zh_content: "Yesu jiang Shengjing dangzuo Shen de Jianzheng...Wo ruoshi buzhe yang zuo jiushi yukun de."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.JESUS AND SCRIPTURE" AND c.name = "content.JESUS AND SCRIPTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.JESUS AND SCRIPTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.JESUS AND SCRIPTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >JESUS AND SCRIPTURE" }]->(child);
```

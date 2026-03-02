---
type: THOUGHT
name: "thought.BENEFICIARIES"
alias: "Thought: BENEFICIARIES"
parent: "topic.EVANGELISM"
tags: ["interpersonal", "encounter", "daily", "victims", "beneficiaries"]
ptopic: "[[topic-EVANGELISM]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.BENEFICIARIES",
    alias: "Thought: BENEFICIARIES",
    parent: "topic.EVANGELISM",
    tags: ["interpersonal", "encounter", "daily", "victims", "beneficiaries"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BENEFICIARIES",
    ctype: "THOUGHT",
    en_title: "BENEFICIARIES",
    en_content: "Those I encounter in my everyday life are either victims or beneficiaries of my relationship with God.",
 es_title: "BENEFICIARIOS",
 es_content: "Aquellos con los que me encuentro en mi vida diaria son víctimas o beneficiarios de mi relación con Dios.",
 fr_title: "BÉNÉFICIAIRES",
 fr_content: "Ceux que je rencontre dans ma vie quotidienne sont soit des victimes, soit des bénéficiaires de ma relation avec Dieu.",
 hi_title: "लाभार्थी नहीं",
 hi_content: "मैं अपने रोजमर्रा के जीवन में जिन लोगों से मिलता हूं वे या तो पीड़ित हैं या भगवान के साथ मेरे रिश्ते के लाभार्थी हैं।",
 zh_title: "shòu yì rén",
 zh_content: "wǒ zài rì cháng shēng huó zhōng yù dào de rén yào me shì wǒ yǔ shàng dì guān xì de shòu hài zhě ， yào me shì shòu yì zhě 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BENEFICIARIES" AND c.name = "content.BENEFICIARIES"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.BENEFICIARIES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVANGELISM" AND child.name = "thought.BENEFICIARIES"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVANGELISM->BENEFICIARIES"}]->(child);
```
---
type: THOUGHT
name: "thought.INTEGRITY"
alias: "Thought: Integrity"
parent: "topic.MORALITY"
tags: ["stand", "True", "integrity", "character", "godliness"]
ptopic: "[[topic-MORALITY]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.INTEGRITY",
    alias: "Thought: Integrity",
    parent: "topic.MORALITY",
    tags: ["stand", "True", "integrity", "character", "godliness"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INTEGRITY",
    ctype: "THOUGHT",
    en_title: "Integrity",
    en_content: "",
    es_title: "INTEGRIDAD",
    es_content: "Ganar es divertido y el éxito es grandioso; ¡Pero mucho más satisfactorio es mantenerse firme y ser sincero!",
    fr_title: "INTÉGRITÉ",
    fr_content: "Gagner est amusant et le succès est formidable ; mais il est bien plus gratifiant de rester ferme et d’être vrai !",
    hi_title: "अखंडता",
    hi_content: "जीतना मज़ेदार है और सफलता महान है; लेकिन इससे कहीं अधिक संतुष्टिदायक बात दृढ़ता से खड़े रहना और सच्चा होना है!",
    zh_title: "zhèng zhí",
    zh_content: "shèng lì shì yǒu qù de ， chéng gōng shì wěi dà de ； dàn gèng lìng rén mǎn zú de shì jiān dìng lì chǎng hé chéng shí ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INTEGRITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->INTEGRITY"
RETURN t, parent;
```

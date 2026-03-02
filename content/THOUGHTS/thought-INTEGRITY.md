---
type: THOUGHT
name: "thought.INTEGRITY"
alias: "Thought: INTEGRITY"
parent: "topic.MORALITY"
tags: ["stand", "True", "integrity", "character", "godliness"]
ptopic: "[[topic-MORALITY]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INTEGRITY",
    alias: "Thought: INTEGRITY",
    parent: "topic.MORALITY",
    tags: ["stand", "True", "integrity", "character", "godliness"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INTEGRITY",
    ctype: "THOUGHT",
    en_title: "INTEGRITY",
 es_title: "INTEGRIDAD",
 fr_title: "INTÉGRITÉ",
 hi_title: "अखंडता",
 zh_title: "zhèng zhí",
    en_content: "",
 es_content: "Ganar es divertido y el éxito es grandioso; ¡Pero mucho más satisfactorio es mantenerse firme y ser sincero!",
 fr_content: "Gagner est amusant et le succès est formidable ; mais il est bien plus gratifiant de rester ferme et d’être vrai !",
 hi_content: "जीतना मज़ेदार है और सफलता महान है; लेकिन इससे कहीं अधिक संतुष्टिदायक बात दृढ़ता से खड़े रहना और सच्चा होना है!",
 zh_content: "shèng lì shì yǒu qù de ， chéng gōng shì wěi dà de ； dàn gèng lìng rén mǎn zú de shì jiān dìng lì chǎng hé chéng shí ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INTEGRITY" AND c.name = "content.INTEGRITY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.INTEGRITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.INTEGRITY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MORALITY->INTEGRITY"}]->(child);
```
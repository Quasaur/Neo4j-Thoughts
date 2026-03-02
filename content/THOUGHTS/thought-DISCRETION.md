---
type: THOUGHT
name: "thought.DISCRETION"
alias: "Thought: DISCRETION"
parent: "topic.PSYCHOLOGY"
tags: ["discretion", "sensitivity", "tactfulness", "relationships", "wisdom"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DISCRETION",
    alias: "Thought: DISCRETION",
    parent: "topic.PSYCHOLOGY",
    tags: ["discretion", "sensitivity", "tactfulness", "relationships", "wisdom"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DISCRETION",
    ctype: "THOUGHT",
    en_title: "DISCRETION",
 es_title: "DISCRECIÓN",
 fr_title: "DISCRÉTION",
 hi_title: "विवेक",
 zh_title: "shěn shèn",
    en_content: "",
 es_content: "Dios sabe cosas sobre las personas que te rodean de las que tú no tienes idea; si una de esas cosas sale a la luz es por algo.",
 fr_content: "Dieu sait des choses sur les gens autour de vous dont vous n'avez aucune idée ; si une de ces choses se révèle, c’est pour une raison.",
 hi_content: "ईश्वर आपके आस-पास के लोगों के बारे में ऐसी बातें जानता है जिनके बारे में आपको कोई जानकारी नहीं है; यदि उनमें से कोई एक चीज़ प्रकाश में आती है, तो वह किसी कारण से होती है।",
 zh_content: "shén zhī dào nǐ zhōu wéi de rén suǒ bù zhī dào de shì qíng ； rú guǒ qí zhōng yī jiàn shì qíng bèi bào guāng ， nà shì yǒu yuán yīn de 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DISCRETION" AND c.name = "content.DISCRETION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.DISCRETION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.DISCRETION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->DISCRETION"}]->(child);
```
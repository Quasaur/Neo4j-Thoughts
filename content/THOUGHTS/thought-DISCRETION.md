---
type: THOUGHT
name: "thought.DISCRETION"
alias: "Thought: Discretion"
parent: "topic.PSYCHOLOGY"
tags: ["discretion", "sensitivity", "tactfulness", "relationships", "wisdom"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DISCRETION",
    alias: "Thought: Discretion",
    parent: "topic.PSYCHOLOGY",
    tags: ["discretion", "sensitivity", "tactfulness", "relationships", "wisdom"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DISCRETION",
    ctype: "THOUGHT",
    en_title: "Discretion",
    en_content: "",
    es_title: "DISCRECIÓN",
    es_content: "Dios sabe cosas sobre las personas que te rodean de las que tú no tienes idea; si una de esas cosas sale a la luz es por algo.",
    fr_title: "DISCRÉTION",
    fr_content: "Dieu sait des choses sur les gens autour de vous dont vous n'avez aucune idée ; si une de ces choses se révèle, c’est pour une raison.",
    hi_title: "विवेक",
    hi_content: "ईश्वर आपके आस-पास के लोगों के बारे में ऐसी बातें जानता है जिनके बारे में आपको कोई जानकारी नहीं है; यदि उनमें से कोई एक चीज़ प्रकाश में आती है, तो वह किसी कारण से होती है।",
    zh_title: "shěn shèn",
    zh_content: "shén zhī dào nǐ zhōu wéi de rén suǒ bù zhī dào de shì qíng ； rú guǒ qí zhōng yī jiàn shì qíng bèi bào guāng ， nà shì yǒu yuán yīn de 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DISCRETION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->DISCRETION"
RETURN t, parent;
```

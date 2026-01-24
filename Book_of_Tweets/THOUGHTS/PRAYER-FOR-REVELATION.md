---
name: "thought.PRAYER FOR REVELATION"
alias: "Thought: Prayer For Revelation"
type: THOUGHT
en_content: "God knows things about the people around you that you have no idea of; if one of those things comes to light, it is so you can pray."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- revelation
- empathy
- spirituality
- discernment
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.PRAYER FOR REVELATION",
    alias: "Thought: Prayer For Revelation",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'revelation', 'empathy', 'spirituality', 'discernment'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER FOR REVELATION",
    en_title: "Prayer For Revelation",
    en_content: "God knows things about the people around you that you have no idea of; if one of those things comes to light, it is so you can pray.",
    es_title: "Oración Por Revelación",
    es_content: "Dios conoce cosas acerca de las personas que te rodean de las que no tienes ni idea; si una de esas cosas sale a la luz, es para que puedas orar.",
    fr_title: "Prière Pour La Révélation",
    fr_content: "Dieu connaît des choses sur les gens qui t'entourent dont tu n'as aucune idée; si l'une de ces choses vient à la lumière, c'est pour que tu puisses prier.",
    hi_title: "प्रकाशन के लिए प्रार्थना",
    hi_content: "परमेश्वर आपके आसपास के लोगों के बारे में ऐसी बातें जानता है जिनका आपको कोई अंदाज़ा नहीं है; यदि उनमें से कोई बात प्रकाश में आती है, तो यह इसलिए है कि आप प्रार्थना कर सकें।",
    zh_title: "qǐ qiú qǐ shì de dǎo gào",
    zh_content: "shàng dì zhī dào nǐ zhōu wéi rén men de shì qíng, ér nǐ duì cǐ háo wú tóu xù; rú guǒ qí zhōng yī jiàn shì qíng bào lù chū lái, nà shi wèi le ràng nǐ néng gòu qí dǎo."
});

MATCH (t:THOUGHT {name: "thought.PRAYER FOR REVELATION"})
MATCH (c:CONTENT {name: "content.PRAYER FOR REVELATION"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER FOR REVELATION" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.PRAYER FOR REVELATION"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->PRAYER FOR REVELATION" }]->(child);
```

---
name: "thought.NOTHING TO OFFER"
alias: "Thought: Nothing To Offer"
type: THOUGHT
en_content: "God is not interested in what you can offer Him; because the truth is that you have nothing to give God until He gives it to you first!"
parent: "topic.THE GODHEAD"
tags:
- provision
- offering
- dependence
- majesty
- god
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Apr-2012a)
CREATE (t:THOUGHT {
    name: "thought.NOTHING TO OFFER",
    alias: "Thought: Nothing To Offer",
    parent: "topic.THE GODHEAD",
    tags: ['provision', 'offering', 'dependence', 'majesty', 'god'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NOTHING TO OFFER",
    en_title: "Nothing To Offer",
    en_content: "God is not interested in what you can offer Him; because the truth is that you have nothing to give God until He gives it to you first!",
    es_title: "Nada Que Ofrecer",
    es_content: "A Dios no le interesa lo que puedas ofrecerle; ¡porque la verdad es que no tienes nada que darle a Dios hasta que Él te lo dé primero!",
    fr_title: "Rien à Offrir",
    fr_content: "Dieu ne s'intéresse pas à ce que vous pouvez Lui offrir ; car la vérité est que vous n'avez rien à donner à Dieu jusqu'à ce qu'Il vous le donne en premier !",
    hi_title: "देने के लिए कुछ नहीं",
    hi_content: "परमेश्वर इस बात में रुचि नहीं रखता कि आप उसे क्या दे सकते हैं; क्योंकि सच्चाई यह है कि जब तक परमेश्वर आपको पहले न दे, तब तक आपके पास परमेश्वर को देने के लिए कुछ भी नहीं है!",
    zh_title: "Wu Ke Feng Xian",
    zh_content: "Shen bu zai yi ni neng gei Ta shen me; yin wei shi shi shi, zhi you Shen xian gei le ni, ni cai you dong xi ke yi gei Shen!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOTHING TO OFFER" AND c.name = "content.NOTHING TO OFFER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING TO OFFER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NOTHING TO OFFER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NOTHING TO OFFER" }]->(child);
```

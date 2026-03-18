---
type: THOUGHT
name: "thought.BETTER NOT EASIER"
alias: "Thought: Better Not Easier"
parent: "topic.THE GODHEAD"
en_content: "Jesus did not come to make our lives easier; Christ came to make our lives better!"
tags: ["jesus", "better", "easier", "life"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Nov-2013)
CREATE (t:THOUGHT {    name: "thought.BETTER NOT EASIER",
    alias: "Thought: Better Not Easier",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'better', 'easier', 'life'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.BETTER NOT EASIER",
    ctype: "THOUGHT",
    en_title: "Better Not Easier",
    en_content: "Jesus did not come to make our lives easier; Christ came to make our lives better!",
    es_title: "Mejor, No Más Fácil",
    es_content: "Jesús no vino para hacer nuestras vidas más fáciles; ¡Cristo vino para hacer nuestras vidas mejores!",
    fr_title: "Meilleur, Pas Plus Facile",
    fr_content: "Jésus n'est pas venu pour rendre nos vies plus faciles ; Christ est venu pour rendre nos vies meilleures !",
    hi_title: "बेहतर, आसान नहीं",
    hi_content: "यीशु हमारे जीवन को आसान बनाने के लिए नहीं आए; मसीह हमारे जीवन को बेहतर बनाने के लिए आए!",
    zh_title: "Gèng hǎo, bù shì gèng róngyì  gèng hǎo ， bú shì gèng róng yì",
    zh_content: "Yēsū lái bùshì wèile ràng wǒmen de shēnghuó gèng róngyì; Jīdū lái shì wèile ràng wǒmen de shēnghuó gèng hǎo!  yē sū lái bú shì wèi le ràng wǒ men de shēng huó gèng róng yì ； jī dū lái shì wèi le ràng wǒ men de shēng huó gèng hǎo ！"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BETTER NOT EASIER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->BETTER NOT EASIER"
RETURN t, parent;
```

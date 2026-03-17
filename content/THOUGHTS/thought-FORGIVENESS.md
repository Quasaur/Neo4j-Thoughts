---
type: THOUGHT
name: "thought.FORGIVENESS"
alias: "Thought: Forgiveness"
parent: "topic.MERCY"
tags: ["forgiveness", "atonement", "propitiation", "thecross", "jesus_christ"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FORGIVENESS",
    alias: "Thought: Forgiveness",
    parent: "topic.MERCY",
    tags: ["forgiveness", "atonement", "propitiation", "thecross", "jesus_christ"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FORGIVENESS",
    ctype: "THOUGHT",
    en_title: "Forgiveness",
    en_content: "",
    es_title: "PERDÓN",
    es_content: "El pecado perdonado aún debe ser castigado y expiado.
¡La Cruz de Jesucristo SATISFA LA Justicia y Venganza Implacables de DIOS!
Sin La Cruz, el Perdón Divino es imposible.",
    fr_title: "PARDON",
    fr_content: "Le péché pardonné doit toujours être puni et expié.
La Croix de Jésus-Christ SATISFAIT la Justice et la Vengeance Implacables de DIEU !
Sans la Croix, le pardon divin est impossible.",
    hi_title: "क्षमा",
    hi_content: "क्षमा किए गए पाप को अभी भी दंडित किया जाना चाहिए और प्रायश्चित किया जाना चाहिए।
यीशु मसीह का क्रूस परमेश्वर के अथक न्याय और प्रतिशोध को संतुष्ट करता है!
क्रॉस के बिना, दिव्य क्षमा असंभव है।",
    zh_title: "ráo shù",
    zh_content: "bèi kuān shù de zuì réng rán bì xū shòu dào chéng fá hé shú zuì 。
 yē sū jī dū de shí zì jià mǎn zú le shén wú qíng de gōng yì hé fù chóu ！
 méi yǒu shí zì jià ， shén shèng de kuān shù shì bù kě néng de 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FORGIVENESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MERCY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MERCY->FORGIVENESS"
RETURN t, parent;
```

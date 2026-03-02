---
type: THOUGHT
name: "thought.FORGIVENESS"
alias: "Thought: FORGIVENESS"
parent: "topic.MERCY"
tags: ["forgiveness", "atonement", "propitiation", "thecross", "jesus_christ"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FORGIVENESS",
    alias: "Thought: FORGIVENESS",
    parent: "topic.MERCY",
    tags: ["forgiveness", "atonement", "propitiation", "thecross", "jesus_christ"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FORGIVENESS",
    ctype: "THOUGHT",
    en_title: "FORGIVENESS",
 es_title: "PERDÓN",
 fr_title: "PARDON",
 hi_title: "क्षमा",
 zh_title: "ráo shù",
    en_content: "",
 es_content: "El pecado perdonado aún debe ser castigado y expiado.
¡La Cruz de Jesucristo SATISFA LA Justicia y Venganza Implacables de DIOS!
Sin La Cruz, el Perdón Divino es imposible.",
 fr_content: "Le péché pardonné doit toujours être puni et expié.
La Croix de Jésus-Christ SATISFAIT la Justice et la Vengeance Implacables de DIEU !
Sans la Croix, le pardon divin est impossible.",
 hi_content: "क्षमा किए गए पाप को अभी भी दंडित किया जाना चाहिए और प्रायश्चित किया जाना चाहिए।
यीशु मसीह का क्रूस परमेश्वर के अथक न्याय और प्रतिशोध को संतुष्ट करता है!
क्रॉस के बिना, दिव्य क्षमा असंभव है।",
 zh_content: "bèi kuān shù de zuì réng rán bì xū shòu dào chéng fá hé shú zuì 。
 yē sū jī dū de shí zì jià mǎn zú le shén wú qíng de gōng yì hé fù chóu ！
 méi yǒu shí zì jià ， shén shèng de kuān shù shì bù kě néng de 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FORGIVENESS" AND c.name = "content.FORGIVENESS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FORGIVENESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MERCY" AND child.name = "thought.FORGIVENESS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MERCY->FORGIVENESS"}]->(child);
```
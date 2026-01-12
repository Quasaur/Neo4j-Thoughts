---
name: "thought.GRACE TO HUMBLE"
alias: "Thought: Grace To Humble"
type: THOUGHT
en_content: "Salvation in a Nutshell: God resists the proud, but gives Grace to the humble."
parent: "topic.GRACE"
tags:
- grace
- humility
- proud
- god
- salvation
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Jan-2012b)
CREATE (t:THOUGHT {
    name: "thought.GRACE TO HUMBLE",
    alias: "Thought: Grace To Humble",
    parent: "topic.GRACE",
    tags: ['grace', 'humility', 'proud', 'god', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRACE TO HUMBLE",
    en_title: "Grace To Humble",
    en_content: "Salvation in a Nutshell: God resists the proud, but gives Grace to the humble.",
    es_title: "Gracia Para Los Humildes",
    es_content: "La Salvación en Pocas Palabras: Dios resiste a los soberbios, pero da gracia a los humildes.",
    fr_title: "Grâce Aux Humbles",
    fr_content: "Le Salut en Bref: Dieu résiste aux orgueilleux, mais il fait grâce aux humbles.",
    hi_title: "विनम्रों को अनुग्रह",
    hi_content: "उद्धार संक्षेप में: परमेश्वर अभिमानियों का विरोध करता है, परन्तु विनम्रों पर अनुग्रह करता है।",
    zh_title: "Ci En Gui Yu Qian Bei",
    zh_content: "Jiu En Gai Yao: Shen Di Dang Jiao Ao De Ren, Ci En Gei Qian Bei De Ren."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GRACE TO HUMBLE" AND c.name = "content.GRACE TO HUMBLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GRACE TO HUMBLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.GRACE TO HUMBLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >GRACE TO HUMBLE" }]->(child);
```

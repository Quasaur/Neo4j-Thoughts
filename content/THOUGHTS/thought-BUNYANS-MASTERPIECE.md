---
type: THOUGHT
name: "thought.BUNYANS MASTERPIECE"
alias: "Thought: Law and Grace"
parent: "topic.GRACE"
en_content: "Reading Bunyan's masterpiece: The Doctrine of Law and Grace Unfolded...Wow!!!"
tags: ["john_bunyan", "law", "grace", "literature", "revelation"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.BUNYANS MASTERPIECE",
    alias: "Thought: Law and Grace",
    parent: "topic.GRACE",
    tags: ["john_bunyan", "law", "grace", "literature", "revelation"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BUNYANS MASTERPIECE",
    ctype: "THOUGHT",
    en_title: "Bunyans Masterpiece",
    en_content: "Reading Bunyan's masterpiece: The Doctrine of Law and Grace Unfolded...Wow!!!",
    es_title: "OBRA DE BUNYAN",
    es_content: "Leyendo la obra maestra de Bunyan: La doctrina de la ley y la gracia desplegadas... ¡Guau!",
    fr_title: "CHEF-D'ŒUVRE DE BUNYAN",
    fr_content: "Lecture du chef-d'œuvre de Bunyan : La Doctrine de la Loi et de la Grâce Dévoilée... Wow !!!",
    hi_title: "बनियान की कृति",
    hi_content: "बनियान की उत्कृष्ट कृति पढ़ रहे हैं: कानून और अनुग्रह का सिद्धांत सामने आया... वाह!!!",
    zh_title: "bān nián jié zuò",
    zh_content: "yuè dú bān nián de jié zuò ： lǜ fǎ hé ēn diǎn de jiào yì zhǎn kāi le …… wà o ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BUNYANS MASTERPIECE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->BUNYANS MASTERPIECE"
RETURN t, parent;
```

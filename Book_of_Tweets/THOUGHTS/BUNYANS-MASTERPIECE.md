---
name: "thought.BUNYANS MASTERPIECE"
alias: "Thought: Law and Grace"
type: THOUGHT
tags:
- john_bunyan
- law
- grace
- literature
- revelation
en_content: "Reading Bunyan's masterpiece: The Doctrine of Law and Grace Unfolded...Wow!!!"
parent: topic.GRACE
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {
    name: "thought.BUNYANS MASTERPIECE",
    alias: "Thought: BUNYANS MASTERPIECE",
    parent: "topic.GRACE",
    tags: ["john_bunyan", "law", "grace", "literature", "revelation"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BUNYANS MASTERPIECE",
    en_title: "BUNYANS MASTERPIECE",
    en_content: "Reading Bunyan's masterpiece: The Doctrine of Law and Grace Unfolded...Wow!!!",
    es_title: "OBRA DE BUNYAN",
    es_content: "Leyendo la obra maestra de Bunyan: La doctrina de la ley y la gracia desplegadas... ¡Guau!",
    fr_title: "CHEF-D'ŒUVRE DE BUNYAN",
    fr_content: "Lecture du chef-d'œuvre de Bunyan : La Doctrine de la Loi et de la Grâce Dévoilée... Wow !!!",
    hi_title: "बनियान की कृति",
    hi_content: "बनियान की उत्कृष्ट कृति पढ़ रहे हैं: कानून और अनुग्रह का सिद्धांत सामने आया... वाह!!!"
    zh_title: "bān nián jié zuò",
    zh_content: "yuè dú bān nián de jié zuò ： lǜ fǎ hé ēn diǎn de jiào yì zhǎn kāi le …… wà o ！"
});

MATCH (t:THOUGHT {name: "thought.BUNYANS MASTERPIECE"})
MATCH (c:CONTENT {name: "content.BUNYANS MASTERPIECE"})
MERGE (t)-[:HAS_CONTENT {name: "edge.BUNYANS MASTERPIECE"}]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.BUNYANS MASTERPIECE"})
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->BUNYANS MASTERPIECE"}]->(child);
```

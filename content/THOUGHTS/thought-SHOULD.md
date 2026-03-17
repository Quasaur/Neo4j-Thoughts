---
type: THOUGHT
name: "thought.SHOULD"
alias: "Thought: Should"
parent: "topic.MORALITY"
tags: ["law", "order", "discipline", "principle", "god"]
ptopic: "[[topic-MORALITY]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SHOULD",
    alias: "Thought: Should",
    parent: "topic.MORALITY",
    tags: ["law", "order", "discipline", "principle", "god"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SHOULD",
    ctype: "THOUGHT",
    en_title: "Should",
    en_content: "",
    es_title: "DEBERÍA",
    es_content: "La palabra \\\"debería\\\" prueba la Existencia de Dios... nos señala un Ideal que no estamos a la altura y nos da un Estándar por el cual debemos juzgarnos a nosotros mismos.",
    fr_title: "DEVRAIT",
    fr_content: "",
    hi_title: "चाहिए",
    hi_content: "शब्द \\\"चाहिए\\\" ईश्वर के अस्तित्व को सिद्ध करता है... हमें एक ऐसे आदर्श की ओर इंगित करता है जिस पर हम खरे नहीं उतरते हैं और हमें एक मानक देता है जिसके द्वारा हमें स्वयं का मूल्यांकन करना चाहिए।",
    zh_title: "yīng gāi",
    zh_content: ""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SHOULD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->SHOULD"
RETURN t, parent;
```

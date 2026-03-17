---
type: THOUGHT
name: "thought.REACTION"
alias: "Thought: Reaction"
parent: "topic.PSYCHOLOGY"
en_content: "Feeling is the reaction of the flesh to circumstance. Feeling is not Truth. Just because you feel angry it doesn't mean you should be."
tags: ["react", "feeling", "flesh", "circumstance", "truth"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.REACTION",
    alias: "Thought: Reaction",
    parent: "topic.PSYCHOLOGY",
    tags: ["react", "feeling", "flesh", "circumstance", "truth"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.REACTION",
    ctype: "THOUGHT",
    en_title: "Reaction",
    en_content: "Feeling is the reaction of the flesh to circumstance. Feeling is not Truth. Just because you feel angry it doesn't mean you should be.",
    es_title: "Reacción",
    es_content: "Sentir es la reacción de la carne ante las circunstancias. Sentir no es la Verdad. Que sientas ira no significa que debas sentirla.",
    fr_title: "Réaction",
    fr_content: "Le sentiment est la réaction de la chair face aux circonstances. Le sentiment n'est pas la vérité. Ce n'est pas parce que vous vous sentez en colère que vous devriez l'être.",
    hi_title: "रिएक्शन",
    hi_content: "फीलिंग, हालात के प्रति शरीर का रिएक्शन है। फीलिंग सच नहीं है। सिर्फ इसलिए कि आपको गुस्सा आ रहा है, इसका मतलब यह नहीं है कि आपको गुस्सा आना चाहिए।",
    zh_title: "Fǎnyìng",
    zh_content: "gǎnjué shì ròutǐ duì huánjìng de fǎnyìng. Gǎnjué bìngfēi zhēnlǐ. Jǐnjǐn yīnwèi nǐ gǎndào fènnù, bìng bù yìwèizhe nǐ jiù yīnggāi fènnù."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.REACTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->REACTION"
RETURN t, parent;
```

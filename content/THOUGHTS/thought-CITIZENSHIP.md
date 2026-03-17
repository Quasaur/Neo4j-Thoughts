---
type: THOUGHT
name: "thought.CITIZENSHIP"
alias: "Thought: Citizenship"
parent: "topic.ECONOMICS"
tags: ["citizenship", "kingdom", "reign_of_god", "freedom", "jesus_christ"]
ptopic: "[[topic-ECONOMICS]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.CITIZENSHIP",
    alias: "Thought: Citizenship",
    parent: "topic.ECONOMICS",
    tags: ["citizenship", "kingdom", "reign_of_god", "freedom", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CITIZENSHIP",
    ctype: "THOUGHT",
    en_title: "Citizenship",
    en_content: "REMEMBER: there is no 'cost of living' in the Kingdom of the Heavens. Change your citizenship IMMEDIATELY!!!",
    es_title: "CIUDADANÍA",
    es_content: "RECUERDA: no hay 'costo de vida' en el Reino de los Cielos. ¡¡¡Cambia tu ciudadanía INMEDIATAMENTE!!!",
    fr_title: "CITOYENNETÉ",
    fr_content: "RAPPELEZ-VOUS : il n'y a pas de « coût de la vie » dans le Royaume des Cieux. Changez de citoyenneté IMMÉDIATEMENT !!!",
    hi_title: "सिटिज़नशिप",
    hi_content: "याद रखें: स्वर्ग के राज्य में 'जीवनयापन की कोई कीमत' नहीं है। तुरंत अपनी नागरिकता बदलें!!!",
    zh_title: "guó jí",
    zh_content: "qǐng jì zhù ： tiān guó lǐ méi yǒu “ shēng huó fèi yòng ”。 lì jí gēng gǎi nín de guó jí ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CITIZENSHIP"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ECONOMICS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ECONOMICS->CITIZENSHIP"
RETURN t, parent;
```

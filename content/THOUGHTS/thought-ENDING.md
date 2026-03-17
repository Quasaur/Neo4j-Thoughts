---
type: THOUGHT
name: thought.ENDING
alias: "Thought: Ending"
parent: topic.APOCALYPSE
en_content: The Bible goes into far more detail regarding how the world will end than how the world began.
tags:
  - ending
  - bible
  - apocalypse
  - judgment
  - new_jerusalem
ptopic: "[[topic-APOCALYPSE]]"
level: 5
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ENDING",
    alias: "Thought: Ending",
    parent: "topic.APOCALYPSE",
    tags: ["ending", "bible", "apocalypse", "judgment", "new_jerusalem"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.ENDING",
    ctype: "THOUGHT",
    en_title: "Thought: Ending",
    en_content: "The Bible goes into far more detail regarding how the world will end than how the world began.",
    es_title: "Pensamiento: final",
    es_content: "La Biblia entra en muchos más detalles sobre cómo terminará el mundo que cómo comenzó.",
    fr_title: "Pensée : Fin",
    fr_content: "La Bible donne beaucoup plus de détails sur la façon dont le monde finira que sur la façon dont le monde a commencé.",
    hi_title: "विचार: समाप्त",
    hi_content: "दुनिया कैसे शुरू हुई इसकी तुलना में बाइबल इस बारे में कहीं अधिक विस्तार से बताती है कि दुनिया का अंत कैसे होगा।",
    zh_title: "xiǎng fǎ : jié shù",
    zh_content: "shèng jīng duì shì jiè rú hé jié shù de miáo shù bǐ shì jiè rú hé kāi shǐ gèng jiā xiáng xì ."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ENDING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.APOCALYPSE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.APOCALYPSE->ENDING"
RETURN t, parent;
```

---
type: THOUGHT
name: "thought.CHRISTS AMNESTY"
alias: "Thought: Christs Amnesty"
parent: "topic.GRACE"
en_content: "Humanity's trial is over, and we have been judged. Execution of sentence is nearer than we realize. Christ is God's Only Amnesty."
tags: ["amnesty", "christ", "judgment", "grace", "humanity"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.CHRISTS AMNESTY",
    alias: "Thought: Christs Amnesty",
    parent: "topic.GRACE",
    tags: ['amnesty', 'christ', 'judgment', 'grace', 'humanity'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHRISTS AMNESTY",
    ctype: "THOUGHT",
    en_title: "Christs Amnesty",
    en_content: "Humanity's trial is over, and we have been judged. Execution of sentence is nearer than we realize. Christ is God's Only Amnesty.",
    es_title: "La Amnistía de Cristo",
    es_content: "El juicio de la humanidad ha terminado, y hemos sido juzgados. La ejecución de la sentencia está más cerca de lo que creemos. Cristo es la Única Amnistía de Dios.",
    fr_title: "L'Amnistie du Christ",
    fr_content: "Le procès de l'humanité est terminé, et nous avons été jugés. L'exécution de la sentence est plus proche que nous ne le réalisons. Le Christ est la Seule Amnistie de Dieu.",
    hi_title: "मसीह की क्षमा",
    hi_content: "मानवता का मुकदमा समाप्त हो गया है, और हमें न्याय दिया गया है। सज़ा का निष्पादन हमारी सोच से कहीं अधिक निकट है। मसीह परमेश्वर की एकमात्र क्षमा है।",
    zh_title: "Jīdū de Tèshè",
    zh_content: "Rénlèi de shěnpàn yǐ jiéshù, Wǒmen yǐ bèi shěnpàn. Xíngfá de zhíxíng bǐ wǒmen yìdào de gèng jìn. Jīdū shì Shàngdì Wéiyī de Tèshè."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CHRISTS AMNESTY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->CHRISTS AMNESTY"
RETURN t, parent;
```

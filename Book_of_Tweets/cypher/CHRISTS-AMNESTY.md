---
name: "thought.CHRISTS AMNESTY"
alias: "Thought: Christs Amnesty"
type: THOUGHT
en_content: "Humanity's trial is over, and we have been judged. Execution of sentence is nearer than we realize. Christ is God's Only Amnesty."
parent: "topic.GRACE"
tags:
- amnesty
- christ
- judgment
- grace
- humanity
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Feb-2012)
CREATE (t:THOUGHT {
    name: "thought.CHRISTS AMNESTY",
    alias: "Thought: Christs Amnesty",
    parent: "topic.GRACE",
    tags: ['amnesty', 'christ', 'judgment', 'grace', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHRISTS AMNESTY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CHRISTS AMNESTY" AND c.name = "content.CHRISTS AMNESTY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRISTS AMNESTY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.CHRISTS AMNESTY"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >CHRISTS AMNESTY" }]->(child);
```

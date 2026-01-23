---
name: "thought.CHRISTS FINAL VIRTUE"
alias: "Thought: Christs Final Virtue"
type: THOUGHT
en_content: "Humanity's Last and only remaining Virtue is Jesus Christ; rejecting Him is turning our backs on the only Good left to us."
parent: "topic.GRACE"
tags:
- jesus
- virtue
- humanity
- grace
- rejection
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.CHRISTS FINAL VIRTUE",
    alias: "Thought: Christs Final Virtue",
    parent: "topic.GRACE",
    tags: ['jesus', 'virtue', 'humanity', 'grace', 'rejection'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHRISTS FINAL VIRTUE",
    en_title: "Christs Final Virtue",
    en_content: "Humanity's Last and only remaining Virtue is Jesus Christ; rejecting Him is turning our backs on the only Good left to us.",
    es_title: "La Última Virtud de Cristo",
    es_content: "La última y única Virtud restante de la humanidad es Jesucristo; rechazarlo es darle la espalda al único Bien que nos queda.",
    fr_title: "La Dernière Vertu du Christ",
    fr_content: "La dernière et seule vertu restante de l'humanité est Jésus-Christ ; le rejeter, c'est tourner le dos au seul Bien qui nous reste.",
    hi_title: "मसीह का अंतिम गुण",
    hi_content: "मानवता का अंतिम और एकमात्र शेष गुण यीशु मसीह है; उसे अस्वीकार करना हमें बची एकमात्र भलाई से पीठ फेरना है।",
    zh_title: "Jīdū de Zuìhòu Měidé",
    zh_content: "Rénlèi zuìhòu yě shì wéiyī shèngxià de Měidé jiù shì Yēsū Jīdū; Jùjué Tā jiù shì bèiqì wǒmen wéiyī shèngxià de Shàn."
});

MATCH (t:THOUGHT {name: "thought.CHRISTS FINAL VIRTUE"})
MATCH (c:CONTENT {name: "content.CHRISTS FINAL VIRTUE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRISTS FINAL VIRTUE" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.CHRISTS FINAL VIRTUE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >CHRISTS FINAL VIRTUE" }]->(child);
```

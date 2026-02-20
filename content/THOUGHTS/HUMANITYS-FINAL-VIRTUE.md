---
name: "thought.HUMANITYS FINAL VIRTUE"
alias: "Thought: Humanity's Final Virtue"
type: THOUGHT
en_content: Humanity's Last and only remaining Virtue is Jesus Christ; rejecting Him is turning our backs on the only Good left to us.
parent: "topic.GRACE"
tags:
  - jesus
  - virtue
  - humanity
  - grace
  - rejection
level: 3
neo4j: true
ptopic: "[[topic-GRACE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.HUMANITYS FINAL VIRTUE",
    alias: "Thought: Humanity's Final Virtue",
    parent: "topic.GRACE",
    tags: ['jesus', 'virtue', 'humanity', 'grace', 'rejection'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMANITYS FINAL VIRTUE",
    en_title: "Humanity's Final Virtue",
    en_content: "Humanity's Last and only remaining Virtue is Jesus Christ; rejecting Him is turning our backs on the only Good left to us.",
    es_title: "La virtud final de la humanidad",
    es_content: "La última y única virtud que le queda a la humanidad es Jesucristo; rechazarlo es darle la espalda al único bien que nos queda.",
    fr_title: "La dernière vertu de l'humanité",
    fr_content: "La dernière et unique vertu qui reste à l'humanité est Jésus-Christ ; le rejeter, c'est tourner le dos au seul Bien qui nous reste.",
    hi_title: "मानवता का अंतिम सद्गुण",
    hi_content: "मानवता का आखिरी और एकमात्र बचा हुआ सद्गुण यीशु मसीह हैं; उन्हें अस्वीकार करना हमारे पास बची हुई एकमात्र अच्छाई से मुंह मोड़ना है।",
    zh_title: "Rénlèi zuìhòu de déxíng",
    zh_content: "rénlèi zuìhòu yěshì wéiyī shèng xià de dé háng jiùshì yēsū jīdū; jùjué tā jiùshì bèiqì wǒmen jǐn cún de liáng shàn."
});

MATCH (t:THOUGHT {name: "thought.HUMANITYS FINAL VIRTUE"})
MATCH (c:CONTENT {name: "content.HUMANITYS FINAL VIRTUE"})
MERGE (t)-[:HAS_CONTENT { name: "t.edge.HUMANITYS FINAL VIRTUE" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.HUMANITYS FINAL VIRTUE"})
MERGE (parent)-[:HAS_THOUGHT { name: "t.edge.GRACE->HUMANITYS FINAL VIRTUE" }]->(child);
```

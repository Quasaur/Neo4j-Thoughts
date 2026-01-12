---
name: "thought.HONESTY THROUGH LOVE"
alias: "Thought: Honesty Through Love"
type: THOUGHT
en_content: When you know God loves you, it's easier to be honest about your faults.
parent: topic.LOVE
tags:
  - honesty
  - love
  - faults
  - attitude
  - character
level: 3
neo4j: true
ptopic: "[[topic-LOVE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jun-2012a)
CREATE (t:THOUGHT {
    name: "thought.HONESTY THROUGH LOVE",
    alias: "Thought: Honesty Through Love",
    parent: "topic.ATTITUDE",
    tags: ['honesty', 'love', 'faults', 'attitude', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HONESTY THROUGH LOVE",
    en_title: "Honesty Through Love",
    en_content: "When you know God loves you, it's easier to be honest about your faults.",
    es_title: "Honestidad a Través del Amor",
    es_content: "Cuando sabes que Dios te ama, es más fácil ser honesto acerca de tus defectos.",
    fr_title: "L'Honnêteté par l'Amour",
    fr_content: "Quand vous savez que Dieu vous aime, il est plus facile d'être honnête au sujet de vos défauts.",
    hi_title: "प्रेम के माध्यम से ईमानदारी",
    hi_content: "जब आप जानते हैं कि परमेश्वर आपसे प्रेम करता है, तो अपनी कमियों के बारे में ईमानदार होना आसान हो जाता है।",
    zh_title: "Tōngguò ài ér chéngshí",
    zh_content: "Dāng nǐ zhīdào shàngdì ài nǐ shí, duì zìjǐ de quēdiǎn chéngshí biàn gèng jiā róngyì."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HONESTY THROUGH LOVE" AND c.name = "content.HONESTY THROUGH LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HONESTY THROUGH LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HONESTY THROUGH LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >HONESTY THROUGH LOVE" }]->(child);
```

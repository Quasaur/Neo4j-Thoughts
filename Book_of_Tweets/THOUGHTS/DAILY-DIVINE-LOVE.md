---
name: "thought.DAILY DIVINE LOVE"
alias: "Thought: Daily Divine Love"
type: THOUGHT
en_content: "Though I may deserve Wrath I still need Love...and God gives me His Love every morning!"
parent: "topic.GRACE"
tags:
- love
- grace
- wrath
- morning
- god
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jun-2012b)
CREATE (t:THOUGHT {
    name: "thought.DAILY DIVINE LOVE",
    alias: "Thought: Daily Divine Love",
    parent: "topic.GRACE",
    tags: ['love', 'grace', 'wrath', 'morning', 'god'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DAILY DIVINE LOVE",
    en_title: "Daily Divine Love",
    en_content: "Though I may deserve Wrath I still need Love...and God gives me His Love every morning!",
    es_title: "Amor Divino Diario",
    es_content: "Aunque pueda merecer ira, aún necesito amor... ¡y Dios me da Su amor cada mañana!",
    fr_title: "Amour Divin Quotidien",
    fr_content: "Bien que je mérite la colère, j'ai encore besoin d'amour... et Dieu me donne Son amour chaque matin !",
    hi_title: "दैनिक दिव्य प्रेम",
    hi_content: "हालांकि मुझे क्रोध मिलना चाहिए, मुझे अभी भी प्रेम की आवश्यकता है... और परमेश्वर मुझे हर सुबह अपना प्रेम देते हैं!",
    zh_title: "Měirì Shénshèng de Ài",
    zh_content: "Suīrán wǒ kěnéng zhīdé fèn nù, wǒ háishì xūyào ài... Shàngdì měi tiān zǎoshang dōu gěi wǒ Tā de ài!"
});

MATCH (t:THOUGHT {name: "thought.DAILY DIVINE LOVE"})
MATCH (c:CONTENT {name: "content.DAILY DIVINE LOVE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DAILY DIVINE LOVE" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.DAILY DIVINE LOVE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE->DAILY DIVINE LOVE" }]->(child);
```

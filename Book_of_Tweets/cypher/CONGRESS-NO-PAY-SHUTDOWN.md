---
name: "thought.CONGRESS NO PAY SHUTDOWN"
alias: "Thought: Congress No Pay Shutdown"
type: THOUGHT
en_content: "Congress should not get paid as long as the Federal Government is shut down!"
parent: "topic.MORALITY"
tags:
- congress
- shutdown
- money
- morality
- justice
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2013b)
CREATE (t:THOUGHT {
    name: "thought.CONGRESS NO PAY SHUTDOWN",
    alias: "Thought: Congress No Pay Shutdown",
    parent: "topic.MORALITY",
    tags: ['congress', 'shutdown', 'money', 'morality', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONGRESS NO PAY SHUTDOWN",
    en_title: "Congress No Pay Shutdown",
    en_content: "Congress should not get paid as long as the Federal Government is shut down!",
    es_title: "Congreso Sin Pago Cierre",
    es_content: "¡El Congreso no debería recibir pago mientras el Gobierno Federal esté cerrado!",
    fr_title: "Congrès Sans Paie Fermeture",
    fr_content: "Le Congrès ne devrait pas être payé tant que le gouvernement fédéral est fermé !",
    hi_title: "कांग्रेस बिना वेतन बंद",
    hi_content: "जब तक संघीय सरकार बंद है, कांग्रेस को वेतन नहीं मिलना चाहिए!",
    zh_title: "Guóhuì Wú Zhīfù Guānbì",
    zh_content: "Zhǐyào Liánbāng Zhèngfǔ guānbì, Guóhuì jiù bù yīnggāi dédào zhīfù!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CONGRESS NO PAY SHUTDOWN" AND c.name = "content.CONGRESS NO PAY SHUTDOWN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CONGRESS NO PAY SHUTDOWN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CONGRESS NO PAY SHUTDOWN"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CONGRESS NO PAY SHUTDOWN" }]->(child);
```

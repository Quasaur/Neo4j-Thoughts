---
type: THOUGHT
name: "thought.CONGRESS NO PAY SHUTDOWN"
alias: "Thought: Congress No Pay Shutdown"
parent: "topic.MORALITY"
en_content: "Congress should not get paid as long as the Federal Government is shut down!"
tags: ["congress", "shutdown", "money", "morality", "justice"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2013b)
CREATE (t:THOUGHT {    name: "thought.CONGRESS NO PAY SHUTDOWN",
    alias: "Thought: Congress No Pay Shutdown",
    parent: "topic.MORALITY",
    tags: ['congress', 'shutdown', 'money', 'morality', 'justice'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CONGRESS NO PAY SHUTDOWN",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CONGRESS NO PAY SHUTDOWN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->CONGRESS NO PAY SHUTDOWN"
RETURN t, parent;
```

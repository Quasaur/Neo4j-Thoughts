---
name: "thought.SUBMITTING OUR PLANS"
alias: "Thought: Ego and Submission"
type: THOUGHT
tags:
- ego
- submission
- plans
- gods_plan
- humility
en_content: "Our egos are so massive...we're always trying to fit God into our plans rather than submitting ourselves to His Plan."
parent: topic.HUMILITY
level: 4
neo4j: true
insert: true
---
# Thought: SUBMITTING OUR PLANS
> [!Thought-en]
> Our egos are so massive...we're always trying to fit God into our plans rather than submitting ourselves to His Plan.

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {
    name: "thought.SUBMITTING OUR PLANS",
    alias: "Thought: SUBMITTING OUR PLANS",
    parent: "topic.HUMILITY",
    tags: ["ego", "submission", "plans", "gods_plan", "humility"],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SUBMITTING OUR PLANS",
    en_title: "SUBMITTING OUR PLANS",
    en_content: "Our egos are so massive...we're always trying to fit God into our plans rather than submitting ourselves to His Plan.",
    es_title: "SOMETIENDO NUESTROS PLANES",
    es_content: "Nuestros egos son tan masivos... siempre estamos tratando de encajar a Dios en nuestros planes en lugar de someternos a Su Plan.",
    fr_title: "SOUMETTRE NOS PLANS",
    fr_content: "Nos egos sont si massifs... nous essayons toujours de faire entrer Dieu dans nos plans plutôt que de nous soumettre à Son Plan.",
    hi_title: "योजनाएं समर्पित करना",
    hi_content: "हमारे अहंकार इतने विशाल हैं... हम हमेशा भगवान को अपनी योजनाओं में फिट करने की कोशिश करते हैं बजाय इसके कि हम खुद को उनकी योजना के प्रति समर्पित कर दें।"
    zh_title: "fú cóng jì huà",
    zh_content: "wǒ men de zì wǒ shì rú cǐ bàng dà …… wǒ men zǒng shì shì tú ràng shàng dì fú hé wǒ men de jì huà ， ér bù shì ràng wǒ men zì jǐ fú cóng tā de jì huà 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SUBMITTING OUR PLANS" AND c.name = "content.SUBMITTING OUR PLANS"
MERGE (t)-[:HAS_CONTENT {name: "edge.SUBMITTING OUR PLANS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMILITY" AND child.name = "thought.SUBMITTING OUR PLANS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMILITY >SUBMITTING OUR PLANS"}]->(child);
```

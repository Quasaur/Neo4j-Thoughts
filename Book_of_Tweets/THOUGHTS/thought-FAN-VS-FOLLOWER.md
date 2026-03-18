---
type: THOUGHT
name: "thought.FAN VS FOLLOWER"
alias: "Thought: Fan Vs Follower"
parent: "topic.SPIRITUALITY"
en_content: "You can be a fan of Christ yet not a follower; but you cannot be a follower and not be a fan!"
tags: ["follower", "fan", "christ", "spirituality", "commitment"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-May-2012a)
CREATE (t:THOUGHT {    name: "thought.FAN VS FOLLOWER",
    alias: "Thought: Fan Vs Follower",
    parent: "topic.SPIRITUALITY",
    tags: ['follower', 'fan', 'christ', 'spirituality', 'commitment'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.FAN VS FOLLOWER",
    ctype: "THOUGHT",
    en_title: "Fan Vs Follower",
    en_content: "You can be a fan of Christ yet not a follower; but you cannot be a follower and not be a fan!",
    es_title: "Admirador versus Seguidor",
    es_content: "Puedes ser un admirador de Cristo pero no un seguidor; pero no puedes ser un seguidor y no ser un admirador!",
    fr_title: "Fan contre Disciple",
    fr_content: "Vous pouvez être un fan du Christ sans être un disciple ; mais vous ne pouvez pas être un disciple sans être un fan !",
    hi_title: "प्रशंसक बनाम अनुयायी",
    hi_content: "आप मसीह के प्रशंसक हो सकते हैं लेकिन अनुयायी नहीं; लेकिन आप अनुयायी होकर प्रशंसक न होना असंभव है!",
    zh_title: "Fēnsī yǔ mén tú  fěn sī yǔ mén tú",
    zh_content: "Nǐ kěyǐ shì Jīdū de fēnsī, dàn què bù shì mén tú; dàn nǐ bù néng chéngwéi mén tú què bù shì fēnsī!  nǐ kě yǐ shì jī dū de fěn sī ， dàn què bú shì mén tú ； dàn nǐ bù néng chéng wéi mén tú què bú shì fěn sī ！"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FAN VS FOLLOWER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->FAN VS FOLLOWER"
RETURN t, parent;
```

---
name: "thought.FAN VS FOLLOWER"
alias: "Thought: Fan Vs Follower"
type: THOUGHT
en_content: "You can be a fan of Christ yet not a follower; but you cannot be a follower and not be a fan!"
parent: "topic.SPIRITUALITY"
tags:
- follower
- fan
- christ
- spirituality
- commitment
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-May-2012a)
CREATE (t:THOUGHT {
    name: "thought.FAN VS FOLLOWER",
    alias: "Thought: Fan Vs Follower",
    parent: "topic.SPIRITUALITY",
    tags: ['follower', 'fan', 'christ', 'spirituality', 'commitment'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FAN VS FOLLOWER",
    en_title: "Fan Vs Follower",
    en_content: "You can be a fan of Christ yet not a follower; but you cannot be a follower and not be a fan!",
    es_title: "Admirador versus Seguidor",
    es_content: "Puedes ser un admirador de Cristo pero no un seguidor; pero no puedes ser un seguidor y no ser un admirador!",
    fr_title: "Fan contre Disciple",
    fr_content: "Vous pouvez être un fan du Christ sans être un disciple ; mais vous ne pouvez pas être un disciple sans être un fan !",
    hi_title: "प्रशंसक बनाम अनुयायी",
    hi_content: "आप मसीह के प्रशंसक हो सकते हैं लेकिन अनुयायी नहीं; लेकिन आप अनुयायी होकर प्रशंसक न होना असंभव है!",
    zh_title: "Fēnsī yǔ mén tú 粉丝与门徒",
    zh_content: "Nǐ kěyǐ shì Jīdū de fēnsī, dàn què bù shì mén tú; dàn nǐ bù néng chéngwéi mén tú què bù shì fēnsī! 你可以是基督的粉丝，但却不是门徒；但你不能成为门徒却不是粉丝！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FAN VS FOLLOWER" AND c.name = "content.FAN VS FOLLOWER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAN VS FOLLOWER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.FAN VS FOLLOWER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >FAN VS FOLLOWER" }]->(child);
```

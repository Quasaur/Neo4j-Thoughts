---
name: "thought.RESPECTING OUR BODIES"
alias: "Thought: Respecting Our Bodies"
type: THOUGHT
en_content: We don't respect our own bodies yet we want others to respect us!
parent: topic.ATTITUDE
tags:
  - respect
  - body
  - attitude
  - character
  - integrity
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013d)
CREATE (t:THOUGHT {
    name: "thought.RESPECTING OUR BODIES",
    alias: "Thought: Respecting Our Bodies",
    parent: "topic.ATTITUDE",
    tags: ['respect', 'body', 'attitude', 'character', 'integrity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RESPECTING OUR BODIES",
    en_title: "Respecting Our Bodies",
    en_content: "We don't respect our own bodies yet we want others to respect us!",
    es_title: "Respetando Nuestros Cuerpos",
    es_content: "¡No respetamos nuestros propios cuerpos pero queremos que otros nos respeten!",
    fr_title: "Respecter Nos Corps",
    fr_content: "Nous ne respectons pas nos propres corps mais nous voulons que les autres nous respectent !",
    hi_title: "अपने शरीर का सम्मान करना",
    hi_content: "हम अपने शरीर का सम्मान नहीं करते फिर भी चाहते हैं कि दूसरे हमारा सम्मान करें!",
    zh_title: "Zun Zhong Wo Men De Shen Ti",
    zh_content: "Wo men bu zun zhong zi ji de shen ti, que yao qiu bie ren zun zhong wo men!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.RESPECTING OUR BODIES" AND c.name = "content.RESPECTING OUR BODIES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RESPECTING OUR BODIES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.RESPECTING OUR BODIES"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >RESPECTING OUR BODIES" }]->(child);
```

---
name: "thought.OWNING ALL THINGS"
alias: "Thought: Owning All Things"
type: THOUGHT
en_content: "Revelation 21:7: You cannot own ALL THINGS unless you no longer need them."
parent: "topic.PHILOSOPHY"
tags:
- ownership
- attachment
- philosophy
- desire
- abundance
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.OWNING ALL THINGS",
    alias: "Thought: Owning All Things",
    parent: "topic.PHILOSOPHY",
    tags: ['ownership', 'attachment', 'philosophy', 'desire', 'abundance'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.OWNING ALL THINGS",
    en_title: "Owning All Things",
    en_content: "Revelation 21:7: You cannot own ALL THINGS unless you no longer need them.",
    es_title: "Poseer Todas las Cosas",
    es_content: "Apocalipsis 21:7: No puedes poseer TODAS LAS COSAS a menos que ya no las necesites.",
    fr_title: "Posséder Toutes Choses",
    fr_content: "Apocalypse 21:7: Tu ne peux posséder TOUTES CHOSES que si tu n'en as plus besoin.",
    hi_title: "सभी चीजों का स्वामित्व",
    hi_content: "प्रकाशितवाक्य 21:7: आप सभी चीजों के स्वामी तब तक नहीं हो सकते जब तक आपको उनकी आवश्यकता है।",
    zh_title: "Yōngyǒu Yīqiè",
    zh_content: "Qǐshìlù 21:7: Chúfēi nǐ bù zài xūyào tāmen, fǒuzé nǐ wúfǎ yōngyǒu YĪQIÈ SHÌWÙ."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.OWNING ALL THINGS" AND c.name = "content.OWNING ALL THINGS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OWNING ALL THINGS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.OWNING ALL THINGS"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >OWNING ALL THINGS" }]->(child);
```

---
type: THOUGHT
name: "thought.AMERICA ACCOUNTABLE FREEDOMS"
alias: "Thought: America Accountable Freedoms"
parent: "topic.MORALITY"
en_content: "America, God will hold you accountable for the way you spent your freedoms."
tags: ["america", "freedom", "accountability", "morality", "judgment"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Jul-2013)
CREATE (t:THOUGHT {    name: "thought.AMERICA ACCOUNTABLE FREEDOMS",
    alias: "Thought: America Accountable Freedoms",
    parent: "topic.MORALITY",
    tags: ['america', 'freedom', 'accountability', 'morality', 'judgment'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.AMERICA ACCOUNTABLE FREEDOMS",
    ctype: "THOUGHT",
    en_title: "America Accountable Freedoms",
    en_content: "America, God will hold you accountable for the way you spent your freedoms.",
    es_title: "América Responsable de sus Libertades",
    es_content: "América, Dios te hará responsable por la forma en que usaste tus libertades.",
    fr_title: "L'Amérique Responsable de ses Libertés",
    fr_content: "Amérique, Dieu te tiendra responsable de la façon dont tu as utilisé tes libertés.",
    hi_title: "अमेरिका अपनी स्वतंत्रताओं के लिए जवाबदेह",
    hi_content: "अमेरिका, भगवान आपको जवाबदेह ठहराएंगे कि आपने अपनी स्वतंत्रताओं का उपयोग कैसे किया।",
    zh_title: "Měiguó duì zìyóu",
    zh_content: "Měiguó, shàngdì huì ràng nǐ wèi nǐ shǐyòng zìyóu de fāngshì fùzé."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.AMERICA ACCOUNTABLE FREEDOMS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->AMERICA ACCOUNTABLE FREEDOMS"
RETURN t, parent;
```

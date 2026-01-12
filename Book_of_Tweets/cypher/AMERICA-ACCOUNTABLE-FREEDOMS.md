---
name: "thought.AMERICA ACCOUNTABLE FREEDOMS"
alias: "Thought: America Accountable Freedoms"
type: THOUGHT
en_content: "America, God will hold you accountable for the way you spent your freedoms."
parent: "topic.MORALITY"
tags:
- america
- freedom
- accountability
- morality
- judgment
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Jul-2013)
CREATE (t:THOUGHT {
    name: "thought.AMERICA ACCOUNTABLE FREEDOMS",
    alias: "Thought: America Accountable Freedoms",
    parent: "topic.MORALITY",
    tags: ['america', 'freedom', 'accountability', 'morality', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AMERICA ACCOUNTABLE FREEDOMS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AMERICA ACCOUNTABLE FREEDOMS" AND c.name = "content.AMERICA ACCOUNTABLE FREEDOMS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.AMERICA ACCOUNTABLE FREEDOMS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.AMERICA ACCOUNTABLE FREEDOMS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >AMERICA ACCOUNTABLE FREEDOMS" }]->(child);
```

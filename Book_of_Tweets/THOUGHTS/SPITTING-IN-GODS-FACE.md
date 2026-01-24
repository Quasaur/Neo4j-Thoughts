---
name: "thought.SPITTING IN GODS FACE"
alias: "Thought: Spitting In Gods Face"
type: THOUGHT
en_content: "America can spit in God's Face over this gay thing if it wants to, but this is NOT going to end well for any of us."
parent: "topic.MORALITY"
tags:
- america
- morality
- judgment
- truth
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Mar-2014)
CREATE (t:THOUGHT {
    name: "thought.SPITTING IN GODS FACE",
    alias: "Thought: Spitting In Gods Face",
    parent: "topic.MORALITY",
    tags: ['america', 'morality', 'judgment', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SPITTING IN GODS FACE",
    en_title: "Spitting In Gods Face",
    en_content: "America can spit in God's Face over this gay thing if it wants to, but this is NOT going to end well for any of us.",
    es_title: "Escupir En La Cara De Dios",
    es_content: "Estados Unidos puede escupir en la Cara de Dios por este asunto gay si quiere, pero esto NO va a terminar bien para ninguno de nosotros.",
    fr_title: "Cracher Au Visage De Dieu",
    fr_content: "L'Amérique peut cracher au Visage de Dieu à cause de cette affaire gay si elle le veut, mais cela ne va PAS bien finir pour aucun d'entre nous.",
    hi_title: "भगवान के चेहरे पर थूकना",
    hi_content: "अमेरिका चाहे तो इस समलैंगिक मामले को लेकर भगवान के चेहरे पर थूक सकता है, लेकिन यह हम में से किसी के लिए भी अच्छा अंत नहीं होगा।",
    zh_title: "Xiang Shangdi Lian Shang Tu Tuomo",
    zh_content: "Meiguo ruguo xiang yinwei tongxinglian de shi xiang Shangdi lian shang tu tuomo, ta keyi zheme zuo, dan zhe dui women renhe ren lai shuo dou BU hui you hao jieguo."
});

MATCH (t:THOUGHT {name: "thought.SPITTING IN GODS FACE"})
MATCH (c:CONTENT {name: "content.SPITTING IN GODS FACE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPITTING IN GODS FACE" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.SPITTING IN GODS FACE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->SPITTING IN GODS FACE" }]->(child);
```

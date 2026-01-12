---
name: "thought.SUPPRESSING THE BIBLE"
alias: "Thought: Suppressing The Bible"
type: THOUGHT
en_content: "Where Satan cannot suppress the distribution of the Bible he has convinced the population to stay away from it."
parent: "topic.TRUTH"
tags:
- bible
- satan
- truth
- deception
- revelation
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.SUPPRESSING THE BIBLE",
    alias: "Thought: Suppressing The Bible",
    parent: "topic.TRUTH",
    tags: ['bible', 'satan', 'truth', 'deception', 'revelation'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SUPPRESSING THE BIBLE",
    en_title: "Suppressing The Bible",
    en_content: "Where Satan cannot suppress the distribution of the Bible he has convinced the population to stay away from it.",
    es_title: "Suprimiendo La Biblia",
    es_content: "Donde Satanás no puede suprimir la distribución de la Biblia, ha convencido a la población para que se mantenga alejada de ella.",
    fr_title: "Supprimer La Bible",
    fr_content: "Là où Satan ne peut pas supprimer la distribution de la Bible, il a convaincu la population de s'en tenir à l'écart.",
    hi_title: "बाइबल का दमन",
    hi_content: "जहाँ शैतान बाइबल के वितरण को दबा नहीं सकता, वहाँ उसने जनसंख्या को इससे दूर रहने के लिए राजी कर लिया है।",
    zh_title: "Yayi Shengjing",
    zh_content: "Zai Sadan wufa yayi Shengjing faxing de difang, ta shuofu renmin yuan li Shengjing."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SUPPRESSING THE BIBLE" AND c.name = "content.SUPPRESSING THE BIBLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SUPPRESSING THE BIBLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.SUPPRESSING THE BIBLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >SUPPRESSING THE BIBLE" }]->(child);
```

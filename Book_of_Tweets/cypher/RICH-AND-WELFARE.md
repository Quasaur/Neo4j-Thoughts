---
name: "thought.RICH AND WELFARE"
alias: "Thought: Rich And Welfare"
type: THOUGHT
en_content: "The rich don't want to pay for welfare ...nor do they wish to hire welfare recipients."
parent: "topic.MORALITY"
tags:
- wealth
- morality
- society
- poverty
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2011d)
CREATE (t:THOUGHT {
    name: "thought.RICH AND WELFARE",
    alias: "Thought: Rich And Welfare",
    parent: "topic.MORALITY",
    tags: ['wealth', 'morality', 'society', 'poverty', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RICH AND WELFARE",
    en_title: "Rich And Welfare",
    en_content: "The rich don't want to pay for welfare ...nor do they wish to hire welfare recipients.",
    es_title: "Los Ricos y el Bienestar Social",
    es_content: "Los ricos no quieren pagar por el bienestar social... ni tampoco desean contratar a los beneficiarios de la asistencia social.",
    fr_title: "Les Riches et l'Aide Sociale",
    fr_content: "Les riches ne veulent pas payer pour l'aide sociale... ils ne souhaitent pas non plus embaucher les bénéficiaires de l'aide sociale.",
    hi_title: "अमीर और कल्याण",
    hi_content: "अमीर लोग कल्याण के लिए भुगतान नहीं करना चाहते... न ही वे कल्याण प्राप्तकर्ताओं को काम पर रखना चाहते हैं।",
    zh_title: "Fu Ren Yu Fu Li",
    zh_content: "Fu ren bu yuan yi wei fu li fu kuan... ye bu yuan yi gu yong fu li shou yi zhe."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.RICH AND WELFARE" AND c.name = "content.RICH AND WELFARE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RICH AND WELFARE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.RICH AND WELFARE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >RICH AND WELFARE" }]->(child);
```

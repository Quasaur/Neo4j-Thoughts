---
name: "thought.GRACE VS SATAN"
alias: "Thought: Grace Vs Satan"
type: THOUGHT
en_content: "Apart from Grace, what difference is there between me and Satan? He's older and smarter...other than that we're both petty little monsters."
parent: "topic.GRACE"
tags:
- grace
- satan
- human_nature
- humility
- comparison
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.GRACE VS SATAN",
    alias: "Thought: Grace Vs Satan",
    parent: "topic.GRACE",
    tags: ["grace", "satan", "human_nature", "humility", "comparison"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRACE VS SATAN",
    en_title: "Grace Vs Satan",
    en_content: "Apart from Grace, what difference is there between me and Satan? He's older and smarter...other than that we're both petty little monsters.",
    es_title: "Gracia Vs Satanás",
    es_content: "Sin la Gracia, ¿qué diferencia hay entre yo y Satanás? Él es más viejo y más astuto... aparte de eso, ambos somos pequeños monstruos mezquinos.",
    fr_title: "Grâce Contre Satan",
    fr_content: "Sans la Grâce, quelle différence y a-t-il entre moi et Satan ? Il est plus âgé et plus intelligent... à part cela, nous sommes tous deux de petits monstres mesquins.",
    hi_title: "कृपा बनाम शैतान",
    hi_content: "कृपा के अतिरिक्त, मेरे और शैतान के बीच क्या अंतर है? वह अधिक पुराना और चतुर है... इसके अलावा हम दोनों छोटे और क्षुद्र राक्षस हैं।",
    zh_title: "En Dian Dui Sa Dan",
    zh_content: "Chu Le En Dian, Wo He Sa Dan You Shen Me Qu Bie Ne? Ta Nian Ji Geng Da, Geng Cong Ming... Chu Ci Zhi Wai, Wo Men Dou Shi Xiao Qi De Xiao Guai Wu."
});

MATCH (t:THOUGHT {name: "thought.GRACE VS SATAN"})
MATCH (c:CONTENT {name: "content.GRACE VS SATAN"})
MERGE (t)-[:HAS_CONTENT {name: "edge.GRACE VS SATAN"}]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.GRACE VS SATAN"})
MERGE (parent)-[:HAS_THOUGHT {name: "GRACE >GRACE VS SATAN"}]->(child);
```

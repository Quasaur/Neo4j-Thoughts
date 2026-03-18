---
type: THOUGHT
name: "thought.GRACE VS SATAN"
alias: "Thought: Grace Vs Satan"
parent: "topic.EVIL"
en_content: "Apart from Grace, what difference is there between me and Satan? He's older and smarter...other than that we're both petty little monsters."
tags: ["grace", "satan", "human_nature", "evil", "comparison"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GRACE VS SATAN",
    alias: "Thought: Grace Vs Satan",
    parent: "topic.EVIL",
    tags: ["grace", "satan", "human_nature", "evil", "comparison"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GRACE VS SATAN",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GRACE VS SATAN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->GRACE VS SATAN"
RETURN t, parent;
```

---
name: "thought.BUILD ON THE ROCK"
alias: "Thought: Build On The Rock"
type: THOUGHT
en_content: "You can build WITH Gold, but you can't build ON Gold; you must build on The ROCK...it's not as shiny, but it's a lot stronger!"
parent: "topic.SPIRITUALITY"
tags:
- rock
- gold
- foundation
- spirituality
- strength
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.BUILD ON THE ROCK",
    alias: "Thought: Build On The Rock",
    parent: "topic.SPIRITUALITY",
    tags: ['rock', 'gold', 'foundation', 'spirituality', 'strength'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BUILD ON THE ROCK",
    en_title: "Build On The Rock",
    en_content: "You can build WITH Gold, but you can't build ON Gold; you must build on The ROCK...it's not as shiny, but it's a lot stronger!",
    es_title: "Construir Sobre La Roca",
    es_content: "Puedes construir CON Oro, pero no puedes construir SOBRE Oro; debes construir sobre La ROCA... ¡no es tan brillante, pero es mucho más fuerte!",
    fr_title: "Construire Sur Le Roc",
    fr_content: "Vous pouvez construire AVEC de l'or, mais vous ne pouvez pas construire SUR l'or ; vous devez construire sur LE ROC... ce n'est pas aussi brillant, mais c'est beaucoup plus solide !",
    hi_title: "चट्टान पर निर्माण करें",
    hi_content: "आप सोने के साथ निर्माण कर सकते हैं, लेकिन आप सोने पर निर्माण नहीं कर सकते; आपको चट्टान पर निर्माण करना होगा... यह उतना चमकदार नहीं है, लेकिन यह बहुत अधिक मजबूत है!",
    zh_title: "Zài Pánshí shàng Jiànzào",
    zh_content: "Nǐ kěyǐ yòng huángjīn jiànzào, dàn nǐ bùnéng zài huángjīn shàng jiànzào; nǐ bìxū zài pánshí shàng jiànzào... tā méiyǒu nàme shǎnliàng, dàn tā gèngjiā qiángzhuàng!"
});

MATCH (t:THOUGHT {name: "thought.BUILD ON THE ROCK"})
MATCH (c:CONTENT {name: "content.BUILD ON THE ROCK"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.BUILD ON THE ROCK" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.BUILD ON THE ROCK"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >BUILD ON THE ROCK" }]->(child);
```

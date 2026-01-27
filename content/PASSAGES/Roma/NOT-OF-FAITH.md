---
name: passage.NOT-OF-FAITH
alias: "Passage: NOT-OF-FAITH"
type: PASSAGE
parent: topic.FAITH
tags:
- faith
- doubt
- condemnation
- sin
- wordofgod
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.NOT-OF-FAITH",
    alias: "Passage: NOT-OF-FAITH",
    parent: "topic.FAITH",
    tags: ["faith", "doubt", "condemnation", "sin", "wordofgod"],
    source: "'Romans 14:23'",
    sortedsource: "'Romans 14:23'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Romans+14%3A23&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NOT-OF-FAITH",
    en_title: "NOT-OF-FAITH",
    en_content: "But the one who doubts is condemned if he eats, because his eating is not from faith; and whatever is not from faith is sin.",
 es_title: "NO-DE-FE",
 es_content: "Pero el que duda, si come, se condena, porque no come por fe; y todo lo que no proviene de la fe es pecado.",
 fr_title: "NON-DE-FOI",
 fr_content: "Mais celui qui doute est condamné s'il mange, parce que ce n'est pas par foi qu'il mange ; et tout ce qui ne vient pas de la foi est un péché.",
 hi_title: "आस्था का नहीं",
 hi_content: "परन्तु जो सन्देह करता है, यदि वह खाता है, तो दोषी ठहराया जाता है, क्योंकि उसका खाना विश्वास से नहीं होता; और जो कुछ विश्वास से नहीं वह पाप है।",
 zh_title: "bù xìn yǎng",
 zh_content: "dàn huái yí de rén ruò chī jiù huì bèi dìng zuì ， yīn wèi tā de chī bú shì chū yú xìn xīn ； tā de chī shì chū yú xìn xīn 。 fán bù chū yú xìn xīn de dōu shì zuì 。",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.NOT-OF-FAITH"})
MATCH (c:CONTENT {name: "content.NOT-OF-FAITH"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.NOT-OF-FAITH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:PASSAGE {name: "passage.NOT-OF-FAITH"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.FAITH->NOT-OF-FAITH"}]->(child);

```

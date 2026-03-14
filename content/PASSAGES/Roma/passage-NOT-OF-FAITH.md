---
type: PASSAGE
name: "passage.NOT-OF-FAITH"
alias: "Passage: Not-of-faith"
parent: "topic.FAITH"
en_content: "But the one who doubts is condemned if he eats, because his eating is not from faith; and whatever is not from faith is sin."
tags: ["faith", "doubt", "condemnation", "sin", "word_of_god"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.NOT-OF-FAITH",
    parent: "topic.FAITH",
    alias: "Passage: Not-of-faith",
    tags: ["faith", "doubt", "condemnation", "sin", "word_of_god"],
    source: "'Romans 14:23'",
    sortedsource: "'Romans 14:23'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Romans+14%3A23&version=NASB)",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.NOT-OF-FAITH",
    ctype: "PASSAGE",
    en_title: "Not-of-faith",
    en_content: "But the one who doubts is condemned if he eats, because his eating is not from faith; and whatever is not from faith is sin.",
 es_title: "NO-DE-FE",
 es_content: "Pero el que duda, si come, se condena, porque no come por fe; y todo lo que no proviene de la fe es pecado.",
 fr_title: "NON-DE-FOI",
 fr_content: "Mais celui qui doute est condamné s'il mange, parce que ce n'est pas par foi qu'il mange ; et tout ce qui ne vient pas de la foi est un péché.",
 hi_title: "आस्था का नहीं",
 hi_content: "परन्तु जो सन्देह करता है, यदि वह खाता है, तो दोषी ठहराया जाता है, क्योंकि उसका खाना विश्वास से नहीं होता; और जो कुछ विश्वास से नहीं वह पाप है।",
 zh_title: "bù xìn yǎng",
 zh_content: "dàn huái yí de rén ruò chī jiù huì bèi dìng zuì ， yīn wèi tā de chī bú shì chū yú xìn xīn ； tā de chī shì chū yú xìn xīn 。 fán bù chū yú xìn xīn de dōu shì zuì 。",


})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.NOT-OF-FAITH"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.FAITH"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.FAITH->NOT-OF-FAITH"
RETURN b, parent;
```

---
type: THOUGHT
name: "thought.ETERNAL LIFE"
alias: "Thought: Eternal Life"
parent: "topic.FAITHFULNESS"
en_content: "ETERNAL LIFE: God's promise (covenant) to NEVER stop dreaming about you!"
tags: ["immortality", "eternal_life", "promise", "covenant", "god"]
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ETERNAL LIFE",
    alias: "Thought: Eternal Life",
    parent: "topic.FAITHFULNESS",
    tags: ["immortality", "eternal_life", "promise", "covenant", "god"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ETERNAL LIFE",
    ctype: "THOUGHT",
    en_title: "Eternal Life",
    en_content: "ETERNAL LIFE: God's promise (covenant) to NEVER stop dreaming about you!",
    es_title: "VIDA ETERNA",
    es_content: "VIDA ETERNA: La promesa (pacto) de Dios de ¡NUNCA dejar de soñar contigo!",
    fr_title: "LA VIE ÉTERNELLE",
    fr_content: "VIE ÉTERNELLE : La promesse (alliance) de Dieu de ne JAMAIS cesser de rêver de toi !",
    hi_title: "शाश्वत जीवन",
    hi_content: "अनन्त जीवन: भगवान का वादा (वाचा) आपके बारे में सपने देखना कभी बंद नहीं करेगा!",
    zh_title: "yǒng shēng",
    zh_content: "yǒng shēng ： shàng dì de yīng xǔ （ shèng yuē ） yǒng yuǎn bú huì tíng zhǐ duì nǐ de mèng xiǎng ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ETERNAL LIFE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FAITHFULNESS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FAITHFULNESS->ETERNAL LIFE"
RETURN t, parent;
```

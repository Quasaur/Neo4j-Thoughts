---
type: THOUGHT
name: "thought.ETERNAL_LIFE"
alias: "Thought: ETERNAL LIFE"
parent: "topic.FAITHFULNESS"
en_content: "ETERNAL LIFE: God's promise (covenant) to NEVER stop dreaming about you!"
tags: ["immortality", "eternal_life", "promise", "covenant", "god"]
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ETERNAL_LIFE",
    alias: "Thought: ETERNAL LIFE",
    parent: "topic.FAITHFULNESS",
    tags: ["immortality", "eternal_life", "promise", "covenant", "god"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ETERNAL_LIFE",
    ctype: "THOUGHT",
    en_title: "ETERNAL LIFE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ETERNAL_LIFE" AND c.name = "content.ETERNAL_LIFE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.ETERNAL_LIFE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITHFULNESS" AND child.name = "thought.ETERNAL_LIFE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITHFULNESS->ETERNAL_LIFE"}]->(child);
```

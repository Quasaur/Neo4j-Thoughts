---
name: "thought.DIVINE_SEED"
alias: "Thought: DIVINE SEED"
type: THOUGHT
parent: topic.GRACE
tags:
- seed
- wordofgod
- holyspirit
- sowing
- reaping
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DIVINE_SEED",
    alias: "Thought: DIVINE SEED",
    parent: "topic.GRACE",
    tags: ["seed", "wordofgod", "holyspirit", "sowing", "reaping"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DIVINE_SEED",
    en_title: "DIVINE SEED",
    en_content: "A woman cannot give her husband a child without first receiving his seed; likewise we cannot give God worship, glory or obedience without first receiving the Seed of His Word fertilized by the Holy Spirit.",
    es_title: "SEMILLA DIVINA",
    es_content: "Una mujer no puede darle un hijo a su marido sin antes recibir su simiente; de igual manera no podemos darle adoración, gloria u obediencia a Dios sin antes recibir la Semilla de Su Palabra fecundada por el Espíritu Santo.",
    fr_title: "GRAINE DIVINE",
    fr_content: "Une femme ne peut pas donner un enfant à son mari sans avoir reçu au préalable sa semence ; de même, nous ne pouvons pas rendre culte, gloire ou obéissance à Dieu sans d’abord recevoir la Semence de Sa Parole fécondée par le Saint-Esprit.",
    hi_title: "दिव्य बीज",
    hi_content: "कोई स्त्री अपने पति का बीज प्राप्त किए बिना उसे बच्चा नहीं दे सकती; इसी प्रकार हम पवित्र आत्मा द्वारा निषेचित उनके वचन के बीज को प्राप्त किए बिना ईश्वर की पूजा, महिमा या आज्ञाकारिता नहीं दे सकते।",
    zh_title: "shén shèng zhǒng zi",
    zh_content: "nǚ rén rú guǒ méi yǒu xiān dé dào zhàng fū de zhǒng zi ， jiù bù néng gěi tā de zhàng fū shēng hái zi 。 tóng yàng dì ， rú guǒ wǒ men méi yǒu xiān jiē shòu shèng líng suǒ yùn yù de shàng dì huà yǔ de zhǒng zi ， wǒ men jiù wú fǎ jìng bài shàng dì 、 róng yào shàng dì huò shùn fú shàng dì 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DIVINE_SEED" AND c.name = "content.DIVINE_SEED"
MERGE (t)-[:HAS_CONTENT {name: "edge.DIVINE_SEED"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.DIVINE_SEED"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->DIVINE_SEED"}]->(child);
```

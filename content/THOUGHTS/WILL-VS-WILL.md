---
name: "thought.WILL_VS_WILL"
alias: "Thought: WILL VS WILL"
type: THOUGHT
parent: topic.FAITHFULNESS
tags:
- selfdenial
- humility
- seekyefirst
- god
- divinewill
neo4j: true
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.WILL_VS_WILL",
    alias: "Thought: WILL VS WILL",
    parent: "topic.FAITHFULNESS",
    tags: ["selfdenial", "humility", "seekyefirst", "god", "divinewill"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WILL_VS_WILL",
    en_title: "WILL VS WILL",
    en_content: "The Challenge of life is not to do God's Will, it is to do God's Will when your will is headed in another direction.",
    es_title: "VOLUNTAD CONTRA VOLUNTAD",
    es_content: "El Desafío de la vida no es hacer la Voluntad de Dios, es hacer la Voluntad de Dios cuando tu voluntad se dirige en otra dirección.",
    fr_title: "VOLONTÉ CONTRE VOLONTÉ",
    fr_content: "Le défi de la vie n'est pas de faire la Volonté de Dieu, c'est de faire la Volonté de Dieu lorsque votre volonté va dans une autre direction.",
    hi_title: "विल बनाम विल",
    hi_content: "जीवन की चुनौती ईश्वर की इच्छा पूरी करना नहीं है, बल्कि ईश्वर की इच्छा पूरी करना है जब आपकी इच्छा किसी और दिशा में जा रही हो।",
    zh_title: "yì zhì yǔ yì zhì",
    zh_content: "shēng mìng de tiǎo zhàn bú shì zūn xíng shàng dì de zhǐ yì ， ér shì dāng nǐ de yì yuàn zhuǎn xiàng lìng yí gè fāng xiàng shí ， réng yào zūn xíng shàng dì de zhǐ yì 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WILL_VS_WILL" AND c.name = "content.WILL_VS_WILL"
MERGE (t)-[:HAS_CONTENT {name: "edge.WILL_VS_WILL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITHFULNESS" AND child.name = "thought.WILL_VS_WILL"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FAITHFULNESS->WILL_VS_WILL"}]->(child);
```

---
name: "thought.IMAGE OF GOD"
alias: "Thought: Image Of God"
type: THOUGHT
en_content: "I'm NOT the child of monkeys; I was created in God's Image and after His Likeness; I should be treated as such--and so should you!"
parent: "topic.CREATION"
tags:
- creation
- identity
- image
- god
- value
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012c_2)
CREATE (t:THOUGHT {
    name: "thought.IMAGE OF GOD",
    alias: "Thought: Image Of God",
    parent: "topic.CREATION",
    tags: ['creation', 'identity', 'image', 'god', 'value'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IMAGE OF GOD",
    en_title: "Image Of God",
    en_content: "I'm NOT the child of monkeys; I was created in God's Image and after His Likeness; I should be treated as such--and so should you!",
    es_title: "Imagen de Dios",
    es_content: "NO soy hijo de monos; fui creado a Imagen de Dios y a Su Semejanza; debo ser tratado como tal--¡y tú también!",
    fr_title: "Image de Dieu",
    fr_content: "Je ne suis PAS l'enfant de singes ; j'ai été créé à l'Image de Dieu et à Sa Ressemblance ; je devrais être traité comme tel--et vous aussi !",
    hi_title: "परमेश्वर की छवि",
    hi_content: "मैं बंदरों की संतान नहीं हूँ; मैं परमेश्वर की छवि में और उनकी समानता में बनाया गया; मेरे साथ वैसा ही व्यवहार होना चाहिए--और आपके साथ भी!",
    zh_title: "Shàngdì de xínxiàng 上帝的形象",
    zh_content: "Wǒ bù shì hóuzi de háizi; wǒ shì àn Shàngdì de xínxiàng hé tā de yàngshì zhàozào de; yīnggāi zhèyàng duìzhì wǒ--nǐ yě shì! 我不是猴子的孩子；我是按上帝的形象和他的样式造的；应该这样对待我--你也是！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IMAGE OF GOD" AND c.name = "content.IMAGE OF GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.IMAGE OF GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.IMAGE OF GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >IMAGE OF GOD" }]->(child);
```

---
name: "thought.INTELLIGENT_DESIGN"
alias: "Thought: INTELLIGENT DESIGN"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- monalisa
- leonardo
- evolutionists
- pseudoscience
- creationism
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INTELLIGENT_DESIGN",
    alias: "Thought: INTELLIGENT DESIGN",
    parent: "topic.COSMOLOGY",
    tags: ["monalisa", "leonardo", "evolutionists", "pseudoscience", "creationism"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INTELLIGENT_DESIGN",
    en_title: "INTELLIGENT DESIGN",
    en_content: "Could you look at the Mona Lisa and then say that Leonardo did not exist? Such are the men who speak under the cloak of science.",
    es_title: "DISEÑO INTELIGENTE",
    es_content: "¿Podrías mirar la Mona Lisa y luego decir que Leonardo no existió? Así son los hombres que hablan bajo el manto de la ciencia.",
    fr_title: "CONCEPTION INTELLIGENTE",
    fr_content: "Pourriez-vous regarder la Joconde et dire ensuite que Léonard n’existait pas ? Tels sont les hommes qui parlent sous le couvert de la science.",
    hi_title: "बुद्धिमान डिजाइन",
    hi_content: "क्या आप मोना लिसा को देख सकते हैं और फिर कह सकते हैं कि लियोनार्डो का अस्तित्व ही नहीं था? ऐसे ही लोग हैं जो विज्ञान की आड़ में बातें करते हैं।",
    zh_title: "zhì néng shè jì",
    zh_content: "nǐ néng kàn zhe 《 méng nà lì shā 》 rán hòu shuō dá fēn qí bù cún zài ma ？ zhè xiē rén jiù shì pī zhe kē xué wài yī shuō huà de rén 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INTELLIGENT_DESIGN" AND c.name = "content.INTELLIGENT_DESIGN"
MERGE (t)-[:HAS_CONTENT {name: "edge.INTELLIGENT_DESIGN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.INTELLIGENT_DESIGN"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.COSMOLOGY->INTELLIGENT_DESIGN"}]->(child);
```

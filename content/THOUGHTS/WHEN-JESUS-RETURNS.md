---
name: "thought.WHEN_JESUS_RETURNS"
alias: "Thought: WHEN JESUS RETURNS"
type: THOUGHT
parent: topic.HISTORY
tags:
- apocalypse
- demons
- angels
- spirituality
- life
neo4j: true
ptopic: "[[topic-HISTORY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.WHEN_JESUS_RETURNS",
    alias: "Thought: WHEN JESUS RETURNS",
    parent: "topic.HISTORY",
    tags: ["apocalypse", "demons", "angels", "spirituality", "life"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.WHEN_JESUS_RETURNS",
    en_title: "WHEN JESUS RETURNS",
    en_content: "…and with Him choirs of angels that outnumber demons and humans combined, it’s over (the deception, delusion and lies).
NOW is the time to turn off the TV, radio and phone.
NOW is the time for weeping, mourning, repenting, begging for mercy and praying.",
    es_title: "CUANDO JESUS ​​REGRESE",
    es_content: "…y con Él coros de ángeles que superan en número a demonios y humanos combinados, se acabó (el engaño, el engaño y las mentiras).
AHORA es el momento de apagar la televisión, la radio y el teléfono.
AHORA es el momento de llorar, lamentarse, arrepentirse, suplicar misericordia y orar.",
    fr_title: "QUAND JÉSUS RETOURNE",
    fr_content: "…et avec Lui des chœurs d’anges qui sont plus nombreux que les démons et les humains réunis, c’est fini (la tromperie, l’illusion et les mensonges).
Il est MAINTENANT temps d’éteindre la télévision, la radio et le téléphone.
MAINTENANT est le moment de pleurer, de faire le deuil, de se repentir, de demander grâce et de prier.",
    hi_title: "जब यीशु वापस आये",
    hi_content: "...और उसके साथ राक्षसों और मनुष्यों से अधिक संख्या वाले स्वर्गदूतों के समूह ने मिलकर, यह (धोखा, भ्रम और झूठ) खत्म कर दिया है।
अब टीवी, रेडियो और फोन बंद करने का समय आ गया है।
अब रोने, शोक मनाने, पश्चाताप करने, दया की भीख माँगने और प्रार्थना करने का समय है।",
    zh_title: "dāng yē sū zài lái shí",
    zh_content: "…… hé tā yì qǐ ， tiān shǐ hé chàng tuán de shù liàng chāo guò le è mó hé rén lèi de zǒng hé ， yī qiè dōu jié shù le （ qī piàn 、 wàng xiǎng hé huǎng yán ）。
 xiàn zài shì guān diào diàn shì 、 shōu yīn jī hé diàn huà de shí hòu le 。
 xiàn zài shì kū qì 、 āi dào 、 huǐ gǎi 、 qǐ qiú lián mǐn hé qí dǎo de shí hòu 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WHEN_JESUS_RETURNS" AND c.name = "content.WHEN_JESUS_RETURNS"
MERGE (t)-[:HAS_CONTENT {name: "edge.WHEN_JESUS_RETURNS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HISTORY" AND child.name = "thought.WHEN_JESUS_RETURNS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HISTORY->WHEN_JESUS_RETURNS"}]->(child);
```

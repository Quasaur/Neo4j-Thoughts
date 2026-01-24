---
name: "thought.SHUT_DOWN"
alias: "Thought: SHUT DOWN"
type: THOUGHT
parent: topic.FREEDOM
tags:
- free
- expression
- constitutiion
- rights
- tiktok
neo4j: true
ptopic: "[[topic-FREEDOM]]"
level: 5
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SHUT_DOWN",
    alias: "Thought: SHUT DOWN",
    parent: "topic.FREEDOM",
    tags: ["free", "expression", "constitutiion", "rights", "tiktok"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.SHUT_DOWN",
    en_title: "SHUT DOWN",
    en_content: "To the United States Congress:
You can't shut down the porn industry, yet you can shut down my constitutional right to free expression on TikTok...
...you're FIRED.",
    es_title: "CERRAR",
    es_content: "Al Congreso de los Estados Unidos:
No se puede cerrar la industria del porno, pero sí se puede cerrar mi derecho constitucional a la libre expresión en TikTok...
...estás DESPEDIDO.",
    fr_title: "FERMER",
    fr_content: "Au Congrès des États-Unis :
Vous ne pouvez pas fermer l’industrie du porno, mais vous pouvez néanmoins supprimer mon droit constitutionnel à la libre expression sur TikTok…
... vous êtes LICENCIÉ.",
    hi_title: "शट डाउन",
    hi_content: "संयुक्त राज्य कांग्रेस के लिए:
आप पोर्न उद्योग को बंद नहीं कर सकते, फिर भी आप टिकटॉक पर स्वतंत्र अभिव्यक्ति के मेरे संवैधानिक अधिकार को बंद कर सकते हैं...
...तुम्हें निकाल दिया गया है।",
    zh_title: "guān bì",
    zh_content: "zhì měi guó guó huì ：
 nǐ wú fǎ guān bì sè qíng háng yè ， dàn nǐ kě yǐ guān bì wǒ zài  TikTok  shàng zì yóu biǎo dá de xiàn fǎ quán lì ……
... nǐ bèi jiě gù le 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SHUT_DOWN" AND c.name = "content.SHUT_DOWN"
MERGE (t)-[:HAS_CONTENT {name: "edge.SHUT_DOWN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FREEDOM" AND child.name = "thought.SHUT_DOWN"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FREEDOM->SHUT_DOWN"}]->(child);
```

---
type: THOUGHT
name: "thought.PRIORITIES"
alias: "Thought: PRIORITIES"
parent: "topic.WISDOM"
tags: ["priorities", "seekyefirst", "divine_will", "god", "faith"]
ptopic: "[[topic-WISDOM]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PRIORITIES",
    alias: "Thought: PRIORITIES",
    parent: "topic.WISDOM",
    tags: ["priorities", "seekyefirst", "divine_will", "god", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PRIORITIES",
    ctype: "THOUGHT",
    en_title: "PRIORITIES",
 es_title: "PRIORIDADES",
 fr_title: "PRIORITÉS",
 hi_title: "वरीयताओं",
 zh_title: "yōu xiān shì xiàng",
    en_content: "",
 es_content: "La verdad es que la Voluntad de Dios no es lo suficientemente importante para ninguno de nosotros.",
 fr_content: "La vérité est que la Volonté de Dieu n’est pas assez importante pour aucun d’entre nous.",
 hi_content: "सच तो यह है कि ईश्वर की इच्छा हममें से किसी के लिए भी उतनी महत्वपूर्ण नहीं है।",
 zh_content: "shì shí shàng ， shàng dì de zhǐ yì duì wǒ men rèn hé rén lái shuō dōu bù gòu zhòng yào 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRIORITIES" AND c.name = "content.PRIORITIES"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.PRIORITIES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.PRIORITIES"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.WISDOM->PRIORITIES"}]->(child);
```
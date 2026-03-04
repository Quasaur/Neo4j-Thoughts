---
type: THOUGHT
name: "thought.GRATITUDE"
alias: "Thought: Gratitude"
parent: "topic.ATTITUDE"
tags: ["thanksgiving", "humility", "decision", "mercy", "dead"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GRATITUDE",
    alias: "Thought: Gratitude",
    parent: "topic.ATTITUDE",
    tags: ["thanksgiving", "humility", "decision", "mercy", "dead"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRATITUDE",
    ctype: "THOUGHT",
    en_title: "Gratitude",
 es_title: "GRATITUD",
 fr_title: "GRATITUDE",
 hi_title: "कृतज्ञता",
 zh_title: "gǎn jī",
    en_content: "",
 es_content: "Los últimos meses han sido muy desafiantes... ¡pero es mejor que estar muerto (LOL)!",
 fr_content: "Les derniers mois ont été très difficiles... mais c'est mieux que d'être mort (MDR) !",
 hi_content: "पिछले कुछ महीने बहुत चुनौतीपूर्ण रहे हैं...लेकिन यह मरने से भी बेहतर है (LOL)!",
 zh_content: "guò qù de jǐ gè yuè fēi cháng jù yǒu tiǎo zhàn xìng …… dàn zǒng bǐ sǐ le hǎo （ xiào ）！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GRATITUDE" AND c.name = "content.GRATITUDE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.GRATITUDE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.GRATITUDE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->GRATITUDE"}]->(child);
```
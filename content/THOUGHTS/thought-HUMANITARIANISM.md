---
type: THOUGHT
name: "thought.HUMANITARIANISM"
alias: "Thought: HUMANITARIANISM"
parent: "topic.RELIGION"
tags: ["humanity", "self_worship", "god", "judgment", "accountable"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMANITARIANISM",
    alias: "Thought: HUMANITARIANISM",
    parent: "topic.RELIGION",
    tags: ["humanity", "self_worship", "god", "judgment", "accountable"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HUMANITARIANISM",
    ctype: "THOUGHT",
    en_title: "HUMANITARIANISM",
 es_title: "HUMANITARISMO",
 fr_title: "HUMANITARISME",
 hi_title: "मानवतावाद",
 zh_title: "rén dào zhǔ yì",
    en_content: "",
 es_content: "Sin responsabilidad, el hombre puede llamarse Dios (humanitarismo, hermana gemela de la evolución).",
 fr_content: "Sans responsabilité, l'homme peut s'appeler Dieu (l'humanitarisme, la sœur jumelle de l'évolution).",
 hi_content: "जवाबदेही के बिना, मनुष्य स्वयं को भगवान (मानवतावाद, विकासवाद की जुड़वां बहन) कह सकता है।",
 zh_content: "méi yǒu zé rèn ， rén kě yǐ chēng zì jǐ wèi shàng dì （ rén dào zhǔ yì ， jìn huà lùn de luán shēng jiě mèi ）。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMANITARIANISM" AND c.name = "content.HUMANITARIANISM"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.HUMANITARIANISM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.HUMANITARIANISM"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.RELIGION->HUMANITARIANISM"}]->(child);
```
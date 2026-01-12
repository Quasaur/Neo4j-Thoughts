---
name: "thought.NUTRITION MUSCLE ACHES"
alias: "Thought: Nutrition Muscle Aches"
type: THOUGHT
en_content: "Nutrition: Muscle aches may benefit from the following: Astaxanthin, Calcium, Magnesium, Bromelain, Creatine."
parent: "topic.CREATION"
tags:
- creation
- health
- nutrition
- biology
- body
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.NUTRITION MUSCLE ACHES",
    alias: "Thought: Nutrition Muscle Aches",
    parent: "topic.CREATION",
    tags: ['creation', 'health', 'nutrition', 'biology', 'body'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NUTRITION MUSCLE ACHES",
    en_title: "Nutrition Muscle Aches",
    en_content: "Nutrition: Muscle aches may benefit from the following: Astaxanthin, Calcium, Magnesium, Bromelain, Creatine.",
    es_title: "Dolores musculares",
    es_content: "Nutrición: Los dolores musculares pueden beneficiarse de lo siguiente: astaxantina, calcio, magnesio, bromelina y creatina.",
    fr_title: "Douleurs musculaires",
    fr_content: "Nutrition : Les douleurs musculaires peuvent bénéficier des éléments suivants : Astaxanthine, Calcium, Magnésium, Bromélaïne, Créatine.",
    hi_title: "पोषण मांसपेशियों में दर्द",
    hi_content: "पोषण: मांसपेशियों के दर्द में निम्नलिखित से लाभ हो सकता है: एस्टैक्सैन्थिन, कैल्शियम, मैग्नीशियम, ब्रोमेलैन, क्रिएटिन।",
    zh_title: "营养肌肉酸痛",
    zh_content: "营养：肌肉疼痛可能受益于以下物质：虾青素、钙、镁、菠萝蛋白酶、肌酸。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NUTRITION MUSCLE ACHES" AND c.name = "content.NUTRITION MUSCLE ACHES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NUTRITION MUSCLE ACHES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.NUTRITION MUSCLE ACHES"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >NUTRITION MUSCLE ACHES" }]->(child);
```

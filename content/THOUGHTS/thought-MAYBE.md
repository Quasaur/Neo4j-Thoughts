---
type: THOUGHT
name: "thought.MAYBE"
alias: "Thought: Maybe"
parent: "topic.MERCY"
tags: ["compassion", "pity", "leniency", "kindness", "love"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MAYBE",
    alias: "Thought: Maybe",
    parent: "topic.MERCY",
    tags: ["compassion", "pity", "leniency", "kindness", "love"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.MAYBE",
    ctype: "THOUGHT",
    en_title: "Maybe",
 es_title: "TAL VEZ",
 fr_title: "PEUT ÊTRE",
 hi_title: "शायद",
 zh_title: "huò xǔ",
    en_content: "",
 es_content: "Tal vez... sólo tal vez... tal vez los monstruos también necesiten amor.",
 fr_content: "Peut-être... juste peut-être... peut-être que les monstres ont aussi besoin d'amour.",
 hi_content: "शायद...बस शायद...शायद राक्षसों को भी प्यार की ज़रूरत है।",
 zh_content: "yě xǔ …… zhǐ shì yě xǔ …… yě xǔ guài wù yě xū yào ài 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MAYBE" AND c.name = "content.MAYBE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.MAYBE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MERCY" AND child.name = "thought.MAYBE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MERCY->MAYBE"}]->(child);
```
---
title: "Thought: COWARDS"
alias: "Thought: The Terrorist Delusion"
type: THOUGHT
tags:
  - terrorists
  - freedom_fighters
  - cowards
  - children
  - satan
ptopic: "[[topic-EVIL]]"
neo4j: true
inserted: true
level: 4
---

```cypher
CREATE (t:THOUGHT {
    name: "thought.COWARDS",
    alias: "Thought: The Terrorist Delusion",
    parent: "topic.EVIL",
    tags: ["terrorists", "freedom_fighters", "cowards", "children", "satan"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.COWARDS",
    en_title: "Cowards",
    en_content: "Terrorists and freedom fighters are children of the Devil...COWARDS...just like their daddy.",
    es_title: "Cobardes",
    es_content: "Los terroristas y los luchadores por la libertad son hijos del diablo... COBARDES... igual que su papá.",
    fr_title: "Lâches",
    fr_content: "Les terroristes et les combattants de la liberté sont des enfants du Diable... des lâches... tout comme leur père.",
    hi_title: "कायर",
    hi_content: "आतंकवादी और स्वतंत्रता सेनानी शैतान के बच्चे हैं...कायर...ठीक अपने बाप की तरह।",
    zh_title: "Nuòfū",
    zh_content: "kǒngbù fèn zǐ hé zìyóu zhànshì dōu shì móguǐ de zǐsì……nuòfū……jiù xiàng tāmen de lǎo diē yīyàng."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.COWARDS" AND c.name = "content.COWARDS"
MERGE (t)-[:HAS_CONTENT {name: "edge.COWARDS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.COWARDS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->COWARDS"}]->(child);
```


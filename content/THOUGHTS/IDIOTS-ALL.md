---
name: "thought.IDIOTS_ALL"
alias: "Thought: IDIOTS ALL"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- foolish
- stupid
- humanity
- everyone
- intelligence
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.IDIOTS_ALL",
    alias: "Thought: IDIOTS ALL",
    parent: "topic.PSYCHOLOGY",
    tags: ["foolish", "stupid", "humanity", "everyone", "intelligence"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.IDIOTS_ALL",
    en_title: "IDIOTS ALL",
    en_content: "Everyone's an idiot about something!",
    es_title: "IDIOTAS TODOS",
    es_content: "¡Todo el mundo es idiota por algo!",
    fr_title: "LES IDIOTS TOUS",
    fr_content: "Tout le monde est idiot à propos de quelque chose !",
    hi_title: "सभी बेवकूफ",
    hi_content: "हर कोई किसी न किसी मामले में मूर्ख है!",
    zh_title: "dōu shì bái chī",
    zh_content: "měi gè rén zài mǒu xiē shì qíng shàng dōu shì bái chī ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IDIOTS_ALL" AND c.name = "content.IDIOTS_ALL"
MERGE (t)-[:HAS_CONTENT {name: "edge.IDIOTS_ALL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.IDIOTS_ALL"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->IDIOTS_ALL"}]->(child);
```

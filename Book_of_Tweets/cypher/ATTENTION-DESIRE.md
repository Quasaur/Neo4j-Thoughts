---
name: thought.ATTENTION DESIRE
alias: "Thought: Attention Desire"
type: THOUGHT
en_content: I only want your attention when you don't want to give it to me.
parent: topic.ATTITUDE
tags:
  - attitude
  - attention
  - human_nature
  - desire
  - pride
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Aug-2011a)
CREATE (t:THOUGHT {
    name: "thought.ATTENTION DESIRE",
    alias: "Thought: Attention Desire",
    parent: "topic.ATTITUDE",
    tags: ['attitude', 'attention', 'human_nature', 'desire', 'pride'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ATTENTION DESIRE",
    en_title: "Attention Desire",
    en_content: "I only want your attention when you don't want to give it to me.",
    es_title: "Deseo de Atención",
    es_content: "Solo quiero tu atención cuando no quieres dármela.",
    fr_title: "Désir d'Attention",
    fr_content: "Je ne veux ton attention que lorsque tu ne veux pas me la donner.",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "मुझे केवल तभी आपका ध्यान चाहिए जब आप मुझे देना नहीं चाहते।",
    zh_title: "渴望关注",
    zh_content: "我只在你不想给我关注的时候才想要你的关注。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ATTENTION DESIRE" AND c.name = "content.ATTENTION DESIRE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ATTENTION DESIRE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ATTENTION DESIRE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >ATTENTION DESIRE" }]->(child);
```

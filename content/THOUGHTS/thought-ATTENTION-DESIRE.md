---
type: THOUGHT
name: "thought.ATTENTION DESIRE"
alias: "Thought: Attention Desire"
parent: "topic.ATTITUDE"
en_content: "I only want your attention when you don't want to give it to me."
tags: ["attitude", "attention", "human_nature", "desire", "pride"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
---





```Cypher
CREATE (t:THOUGHT {
    name: "thought.ATTENTION DESIRE",
    alias: "Thought: Attention Desire",
    parent: "topic.ATTITUDE",
    tags: ["attitude", "attention", "human_nature", "desire", "pride"],
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
    zh_title: "Kěwàng guānzhù",
    zh_content: "Wǒ zhǐ zài nǐ bù xiǎng gěi wǒ guānzhù de shíhòu cái xiǎng yào nǐ de guānzhù."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ATTENTION DESIRE" AND c.name = "content.ATTENTION DESIRE"
MERGE (t)-[:HAS_CONTENT {name: "edge.ATTENTION DESIRE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ATTENTION DESIRE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->ATTENTION DESIRE"}]->(child);
```

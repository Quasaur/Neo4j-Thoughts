---
name: "thought.EQUALITY AT RETURN"
alias: "Thought: Equality At Return"
type: THOUGHT
en_content: "True economic political and social equality will never exist on Earth until Christ returns."
parent: "topic.SOTERIOLOGY"
tags:
- equality
- christ
- return
- politics
- society
level: 3
neo4j: true
ptopic: "[[topic-SOTERIOLOGY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012f)
CREATE (t:THOUGHT {
    name: "thought.EQUALITY AT RETURN",
    alias: "Thought: Equality At Return",
    parent: "topic.SOTERIOLOGY",
    tags: ['equality', 'christ', 'return', 'politics', 'society'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.EQUALITY AT RETURN",
    en_title: "Equality At Return",
    en_content: "True economic political and social equality will never exist on Earth until Christ returns.",
    es_title: "Igualdad en el Regreso",
    es_content: "La verdadera igualdad económica, política y social nunca existirá en la Tierra hasta que Cristo regrese.",
    fr_title: "Égalité au Retour",
    fr_content: "La véritable égalité économique, politique et sociale n'existera jamais sur Terre jusqu'au retour du Christ.",
    hi_title: "वापसी पर समानता",
    hi_content: "जब तक मसीह वापस नहीं आएगा तब तक पृथ्वी पर सच्ची आर्थिक, राजनीतिक और सामाजिक समानता कभी अस्तित्व में नहीं आएगी।",
    zh_title: "Gui Lai Shi De Ping Deng",
    zh_content: "Zhen Zheng De Jing Ji Zheng Zhi He She Hui Ping Deng Yong Yuan Bu Hui Zai Di Qiu Shang Cun Zai, Zhi Dao Ji Du Fu Gui."
});

MATCH (t:THOUGHT {name: "thought.EQUALITY AT RETURN"})
MATCH (c:CONTENT {name: "content.EQUALITY AT RETURN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.EQUALITY AT RETURN" }]->(c);

MATCH (parent:TOPIC {name: "topic.SOTERIOLOGY"})
MATCH (child:THOUGHT {name: "thought.EQUALITY AT RETURN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SOTERIOLOGY>EQUALITY AT RETURN" }]->(child);
```

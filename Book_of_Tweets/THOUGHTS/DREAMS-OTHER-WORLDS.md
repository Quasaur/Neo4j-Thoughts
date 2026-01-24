---
name: "thought.DREAMS OTHER WORLDS"
alias: "Thought: Dreams Other Worlds"
type: THOUGHT
en_content: "What if dreams were peeks into another life...on another planet ...in another galaxy very similar to ours?"
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- dreams
- existence
- universe
- imagination
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.DREAMS OTHER WORLDS",
    alias: "Thought: Dreams Other Worlds",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'dreams', 'existence', 'universe', 'imagination'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DREAMS OTHER WORLDS",
    en_title: "Dreams Other Worlds",
    en_content: "What if dreams were peeks into another life...on another planet ...in another galaxy very similar to ours?",
    es_title: "Sueños de Otros Mundos",
    es_content: "¿Qué pasaría si los sueños fueran vistazos a otra vida... en otro planeta... en otra galaxia muy similar a la nuestra?",
    fr_title: "Rêves d'Autres Mondes",
    fr_content: "Et si les rêves étaient des aperçus d'une autre vie... sur une autre planète... dans une autre galaxie très similaire à la nôtre ?",
    hi_title: "स्वप्न अन्य संसार",
    hi_content: "क्या होगा अगर स्वप्न किसी अन्य जीवन की झलकियां होते... किसी अन्य ग्रह पर... किसी अन्य आकाशगंगा में जो हमारी आकाशगंगा के समान होती?",
    zh_title: "Meng Jing Qi Ta Shi Jie",
    zh_content: "Ru guo meng jing shi dui ling yi zhong sheng huo de kui shi... zai ling yi ge xing qiu shang... zai ling yi ge yu wo men hen xiang si de yin he xi zhong, na hui zen me yang?"
});

MATCH (t:THOUGHT {name: "thought.DREAMS OTHER WORLDS"})
MATCH (c:CONTENT {name: "content.DREAMS OTHER WORLDS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DREAMS OTHER WORLDS" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.DREAMS OTHER WORLDS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY->DREAMS OTHER WORLDS" }]->(child);
```

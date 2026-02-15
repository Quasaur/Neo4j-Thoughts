---
name: "thought.INSATIABLE"
alias: "Thought: Insatiable"
type: THOUGHT
parent: "topic.EVIL"
en_content: "The human flesh nature is never satisfied. Thus humanity is plunged into every kind of addiction to satiate the unforgiving beast."
tags:
- flesh
- carnal
- animalistic
- impetuous
- instinctual
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INSATIABLE",
    alias: "Thought: Instatiable",
    parent: "topic.EVIL",
    tags: ["flesh", "carnal", "animalistic", "impetuous", "instinctual"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INSATIABLE",
    en_title: "Instatiable",
    en_content: "The human flesh nature is never satisfied. Thus humanity is plunged into every kind of addiction to satiate the unforgiving beast.",
    es_title: "Insaciable",
    es_content: "La naturaleza humana nunca se satisface. Por ello, la humanidad se ve inmersa en todo tipo de adicciones para saciar a la bestia implacable.",
    fr_title: "Insatiable",
    fr_content: "La nature humaine est insatiable. C'est pourquoi l'humanité sombre dans toutes sortes d'addictions pour assouvir sa soif insatiable.".
    hi_title: "भी न तृप्त होने वाला".
    hi_content: "इंसानी शरीर कभी संतुष्ट नहीं होता। इसलिए इंसान इस बेरहम जानवर को संतुष्ट करने के लिए हर तरह के नशे में डूबा रहता है।",
    zh_title: "Yǒng bù mǎnzú",
    zh_content: "rénlèi de ròutǐ běnxìng yǒng bù mǎnzú. Yīncǐ, rénlèi chénnì yú gè zhǒng gè yàng de shìhào, yǐ qiú mǎnzú zhè wúqíng de yěshòu."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INSATIABLE" AND c.name = "content.INSATIABLE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.INSATIABLE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.INSATIABLE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->INSATIABLE"}]->(child);
```
---
name: "thought.WEALTH DISPARITY GAP"
alias: "Thought: Wealth Disparity Gap"
type: THOUGHT
en_content: "Median White household wealth: $US113,000. Median Black household wealth: $US5,700. Oh yeah...life's fair!"
parent: "topic.MORALITY"
tags:
- wealth
- race
- inequality
- society
- justice
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.WEALTH DISPARITY GAP",
    alias: "Thought: Wealth Disparity Gap",
    parent: "topic.MORALITY",
    tags: ['wealth', 'race', 'inequality', 'society', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WEALTH DISPARITY GAP",
    en_title: "Wealth Disparity Gap",
    en_content: "Median White household wealth: $US113,000. Median Black household wealth: $US5,700. Oh yeah...life's fair!",
    es_title: "Brecha de Disparidad de Riqueza",
    es_content: "Riqueza mediana de hogares blancos: $US113,000. Riqueza mediana de hogares negros: $US5,700. ¡Ah sí... la vida es justa!",
    fr_title: "Écart de Disparité de Richesse",
    fr_content: "Richesse médiane des ménages blancs : 113 000 $US. Richesse médiane des ménages noirs : 5 700 $US. Ah oui... la vie est juste !",
    hi_title: "धन असमानता का अंतर",
    hi_content: "श्वेत परिवारों की औसत संपत्ति: $US113,000। अश्वेत परिवारों की औसत संपत्ति: $US5,700। अरे हाँ... जीवन न्यायसंगत है!",
    zh_title: "Caifu Chaju Quekou",
    zh_content: "Bairenjiating zhongwei caifu: Meiyuan 113,000 yuan. Heirenjiating zhongwei caifu: Meiyuan 5,700 yuan. Ai, shi de... shenghuo zhen gongping!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WEALTH DISPARITY GAP" AND c.name = "content.WEALTH DISPARITY GAP"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WEALTH DISPARITY GAP" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.WEALTH DISPARITY GAP"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >WEALTH DISPARITY GAP" }]->(child);
```

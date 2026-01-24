---
name: "thought.STANDARD MODEL HOLES"
alias: "Thought: Standard Model Holes"
type: THOUGHT
en_content: "The holes in the Standard Model, irreducible and specific complexity, the lack of transitional links in the fossil record...take your pick."
parent: "topic.PHILOSOPHY"
tags:
- science
- philosophy
- creation
- complexity
- truth
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Nov-2010e)
CREATE (t:THOUGHT {
    name: "thought.STANDARD MODEL HOLES",
    alias: "Thought: Standard Model Holes",
    parent: "topic.PHILOSOPHY",
    tags: ['science', 'philosophy', 'creation', 'complexity', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.STANDARD MODEL HOLES",
    en_title: "Standard Model Holes",
    en_content: "The holes in the Standard Model, irreducible and specific complexity, the lack of transitional links in the fossil record...take your pick.",
    es_title: "Agujeros modelo estándar",
    es_content: "Los agujeros en el Modelo Estándar, la complejidad irreductible y específica, la falta de vínculos de transición en el registro fósil... elija.",
    fr_title: "Trous du modèle standard",
    fr_content: "Les trous dans le Modèle Standard, la complexité irréductible et spécifique, l'absence de liens transitionnels dans les archives fossiles... faites votre choix.",
    hi_title: "मानक मॉडल छेद",
    hi_content: "मानक मॉडल में छेद, अपरिवर्तनीय और विशिष्ट जटिलता, जीवाश्म रिकॉर्ड में संक्रमणकालीन लिंक की कमी... अपना चयन करें।",
    zh_title: "标准型号孔",
    zh_content: "标准模型中的漏洞、不可简化的特定复杂性、化石记录中缺乏过渡链接......任你选择。"
});

MATCH (t:THOUGHT {name: "thought.STANDARD MODEL HOLES"})
MATCH (c:CONTENT {name: "content.STANDARD MODEL HOLES"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.STANDARD MODEL HOLES" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.STANDARD MODEL HOLES"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY->STANDARD MODEL HOLES" }]->(child);
```

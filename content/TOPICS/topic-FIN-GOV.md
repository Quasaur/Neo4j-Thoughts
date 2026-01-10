---
name: topic.FIN-GOV
alias: "Topic: How Government is Financed"
type: TOPIC
parent: topic.FINANCE
tags:
- currency
- subsidize
- funding
- bankroll
- liquidate
neo4j: true
ptopic: "[[topic-FINANCE]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.FIN-GOV",
    alias: "Topic: How Government is Financed",
    parent: "topic.FINANCE",
    tags: ["currency", "subsidize", "funding", "bankroll", "liquidate"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.FIN-GOV",
    en_title: "GOVERNMENT-FINANCE",
    en_content: "Government finances include revenues, expenditures (spending), debt, and assets (cash and security holdings).",
    es_title: "FINANZAS DEL GOBIERNO",
    es_content: "Las finanzas del gobierno incluyen ingresos, gastos, deuda y activos (efectivo y tenencias de valores).",
    fr_title: "FINANCES PUBLIQUES",
    fr_content: "Les finances publiques comprennent les recettes, les dépenses, la dette et les actifs (trésorerie et titres).",
    hi_title: "सरकारी वित्त",
    hi_content: "सरकारी वित्त में राजस्व, व्यय (खर्च), ऋण और परिसंपत्तियां (नकदी और सुरक्षा होल्डिंग्स) शामिल हैं।",
    zh_title: "Zhèngfǔ cái zhèng",
    zh_content: "Zhèngfǔ cáizhèng bāokuò shōurù, zhīchū, zhàiwù hé zīchǎn (xiànjīn hé zhèngquàn chí yǒu liàng)."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.FIN-GOV" AND d.name = "desc.FIN-GOV"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.FIN-GOV"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.FINANCE" AND c.name = "topic.FIN-GOV"
MERGE (p)-[:HAS_CHILD {name: "edge.FINANCE->FIN-GOV"}]->(c);

```

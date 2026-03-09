---
type: TOPIC
name: "topic.FIN GOV"
alias: "Topic: How Government is Financed"
parent: "topic.FINANCE"
en_content: "Government finances include revenues, expenditures (spending), debt, and assets (cash and security holdings)."
tags: ["currency", "subsidize", "funding", "bankroll", "liquidate"]
ptopic: "[[topic-FINANCE]]"
level: 5
neo4j: true
verified: true
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.FIN GOV",
    alias: "Topic: How Government is Financed",
    parent: "topic.FINANCE",
    tags: ["currency", "subsidize", "funding", "bankroll", "liquidate"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.FIN GOV",
    en_title: "Topic: How Government is Financed",
    en_content: "Government finances include revenues, expenditures (spending), debt, and assets (cash and security holdings).",
    es_title: "Tema: Cómo se financia el gobierno",
    es_content: "Las finanzas del gobierno incluyen ingresos, gastos, deuda y activos (efectivo y tenencias de valores).",
    fr_title: "Sujet : Comment le gouvernement est financé",
    fr_content: "Les finances publiques comprennent les recettes, les dépenses, la dette et les actifs (trésorerie et titres).",
    hi_title: "विषय: सरकार को फाइनेंस कैसे किया जाता है",
    hi_content: "सरकारी वित्त में राजस्व, व्यय (खर्च), ऋण और परिसंपत्तियां (नकदी और सुरक्षा होल्डिंग्स) शामिल हैं।",
    zh_title: "Zhǔtí: Zhèngfǔ de cáizhèng láiyuán",
    zh_content: "Zhèngfǔ cáizhèng bāokuò shōurù, zhīchū, zhàiwù hé zīchǎn (xiànjīn hé zhèngquàn chí yǒu liàng)."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.FIN GOV"})
MATCH (d:DESCRIPTION {name: "desc.FIN GOV"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.FIN GOV"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.FINANCE"
MATCH (c:TOPIC)
WHERE c.name = "topic.FIN GOV"
MERGE (p)-[:HAS_CHILD {name: "edge.FINANCE->FIN GOV"}]->(c);

```

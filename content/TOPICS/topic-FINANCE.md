---
name: topic.FINANCE
alias: "Topic: Sources of Funding"
type: TOPIC
parent: topic.WEALTH
tags:
- currency
- subsidize
- funding
- bankroll
- liquidate
neo4j: true
ptopic: "[[topic-WEALTH]]"
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.FINANCE",
    alias: "Topic: Sources of Funding",
    parent: "topic.WEALTH",
    tags: ["currency", "subsidize", "funding", "bankroll", "liquidate"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.FINANCE",
    en_title: "FINANCE",
    en_content: "Money or other liquid resources of a government, business, group, or individual; the system that includes the circulation of money, the granting of credit, the making of investments, and the provision of banking facilities; the science or study of the management of funds; the obtaining of funds or capital.",
    es_title: "FINANZAS",
    es_content: "Dinero u otros recursos líquidos de un gobierno, empresa, grupo o individuo; el sistema que incluye la circulación de dinero, la concesión de crédito, la realización de inversiones y la provisión de servicios bancarios; la ciencia o el estudio de la gestión de fondos; la obtención de fondos o capital.",
    fr_title: "FINANCE",
    fr_content: "Argent ou autres ressources liquides d'un gouvernement, d'une entreprise, d'un groupe ou d'un individu ; le système qui comprend la circulation de l'argent, l'octroi de crédit, la réalisation d'investissements et la fourniture de services bancaires ; la science ou l'étude de la gestion des fonds ; l'obtention de fonds ou de capitaux.",
    hi_title: "वित्त",
    hi_content: "सकिसी सरकार, व्यवसाय, समूह या व्यक्ति का धन या अन्य तरल संसाधन; वह प्रणाली जिसमें धन का प्रचलन, ऋण प्रदान करना, निवेश करना और बैंकिंग सुविधाओं का प्रावधान शामिल है; निधियों के प्रबंधन का विज्ञान या अध्ययन; निधियों या पूंजी की प्राप्ति।",
    zh_title: "Cáiwù",
    zh_content: "Zhèngfǔ, qǐyè, tuántǐ huò gèrén de huòbì huò qítā liúdòng zīyuán; bāokuò huòbì liútōng, xìndài fāfàng, tóuzī hé yínháng shèshī tígōng de xìtǒng; zījīn guǎnlǐ de kēxué huò yánjiū; zījīn huò zīběn de huòqǔ."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.FINANCE" AND d.name = "desc.FINANCE"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.FINANCE"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.WEALTH" AND c.name = "topic.FINANCE"
MERGE (p)-[:HAS_CHILD {name: "edge.WEALTH->FINANCE"}]->(c);

```

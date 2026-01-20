---
name: topic.LINGUISTICS
alias: "Topic: Linguistic Anthropology"
type: TOPIC
parent: topic.ANTHROPOLOGY
tags:
- human
- speech
- anthropology
- language
- lexical
neo4j: true
ptopic: "[[topic-ANTHROPOLOGY]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.LINGUISTICS",
    alias: "Topic: Linguistic Anthropology",
    parent: "topic.ANTHROPOLOGY",
    tags: ["human", "speech", "anthropology", "language", "lexical"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.LINGUISTICS",
    en_title: "LINGUISTICS",
    en_content: "The study of human speech including the units, nature, structure, and modification of language.",
    es_title: "LINGÜÍSTICA",
    es_content: "El estudio del habla humana, incluidas las unidades, la naturaleza, la estructura y la modificación del lenguaje.",
    fr_title: "LINGUISTIQUE",
    fr_content: "L'étude de la parole humaine, y compris les unités, la nature, la structure et la modification du langage.",
    hi_title: "भाषाविज्ञान",
    hi_content: "मानव वाणी का अध्ययन जिसमें भाषा की इकाइयाँ, प्रकृति, संरचना और संशोधन शामिल हैं।",
    zh_title: "Yǔyán xué",
    zh_content: "Rénlèi yǔyán de yánjiū, bāokuò yǔyán de dānyuán, xìngzhì, jiégòu hé xiūgǎi."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.LINGUISTICS"})
MATCH (d:DESCRIPTION {name: "desc.LINGUISTICS"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.LINGUISTICS"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.ANTHROPOLOGY"
MATCH (c:TOPIC)
WHERE c.name = "topic.LINGUISTICS"
MERGE (p)-[:HAS_CHILD {name: "edge.ANTHROPOLOGY->LINGUISTICS"}]->(c);

```

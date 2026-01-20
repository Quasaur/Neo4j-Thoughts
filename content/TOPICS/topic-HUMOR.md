---
name: topic.HUMOR
alias: "Topic: The Science of Laughter"
type: TOPIC
parent: topic.PSYCHOLOGY
tags:
- ludicrous
- absurd
- incongruous
- comical
- funny
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.HUMOR",
    alias: "Topic: The Science of Laughter",
    parent: "topic.PSYCHOLOGY",
    tags: ["ludicrous", "absurd", "incongruous", "comical", "funny"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.HUMOR",
    en_title: "HUMOR",
    en_content: "The mental faculty of discovering, expressing, or appreciating the ludicrous or absurdly incongruous; the ability to be funny or to be amused by things that are funny; something that is or is designed to be comical or amusing.",
    es_title: "HUMOR",
    es_content: "La facultad mental de descubrir, expresar o apreciar lo ridículo o absurdamente incongruente; la capacidad de ser divertido o de divertirse con cosas que son divertidas; algo que es o está diseñado para ser cómico o divertido.",
    fr_title: "HUMOUR",
    fr_content: "La faculté mentale de découvrir, d'exprimer ou d'apprécier le ridicule ou l'absurdement incongru ; la capacité d'être drôle ou de s'amuser de choses qui sont drôles ; quelque chose qui est ou est conçu pour être comique ou amusant.",
    hi_title: "हास्य",
    hi_content: "हास्यास्पद या बेतुकेपन से असंगत को खोजने, व्यक्त करने या उसका आनंद लेने की मानसिक क्षमता; मज़ेदार होने या मज़ेदार चीजों से मनोरंजन करने की क्षमता; कुछ ऐसा जो हास्यपूर्ण या मनोरंजक है या होने के लिए डिज़ाइन किया गया है।",
    zh_title: "Yōumò",
    zh_content: "Fāxiàn, biǎodá huò xīnshǎng huāngmiù huò huāngmiù de bù xiétiáo de xīnlǐ nénglì; gǎoxiiào huò bèi gǎoxiiào de shìwù dòulè de nénglì; shì huò bèi shèjì wéi huádī huò yulè de shìwù."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.HUMOR"})
MATCH (d:DESCRIPTION {name: "desc.HUMOR"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.HUMOR"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.PSYCHOLOGY"
MATCH (c:TOPIC)
WHERE c.name = "topic.HUMOR"
MERGE (p)-[:HAS_CHILD {name: "edge.PSYCHOLOGY->HUMOR"}]->(c);

```

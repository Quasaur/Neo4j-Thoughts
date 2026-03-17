---
type: THOUGHT
name: "thought.VOICE OF THE DEVIL"
alias: "Thought: Voice Of The Devil"
parent: "topic.EVIL"
en_content: "Submitting to hate, bitterness and violence is giving a voice to The Devil; these have become his most cherished attributes."
tags: ["hate", "bitterness", "violence", "devil", "spiritual_warfare"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.VOICE OF THE DEVIL",
    alias: "Thought: Voice Of The Devil",
    parent: "topic.EVIL",
    tags: ['hate', 'bitterness', 'violence', 'devil', 'spiritual_warfare'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.VOICE OF THE DEVIL",
    ctype: "THOUGHT",
    en_title: "Voice Of The Devil",
    en_content: "Submitting to hate, bitterness and violence is giving a voice to The Devil; these have become his most cherished attributes.",
    es_title: "Voz del diablo",
    es_content: "Someterse al odio, la amargura y la violencia es darle voz al Diablo;estos se han convertido en sus atributos más preciados.",
    fr_title: "Voix du diable",
    fr_content: "Se soumettre à la haine, à l’amertume et à la violence, c’est donner la parole au Diable ;ceux-ci sont devenus ses attributs les plus précieux.",
    hi_title: "शैतान की आवाज",
    hi_content: "नफरत, कड़वाहट और हिंसा के आगे झुकना शैतान को आवाज़ देना है;ये उनके सबसे प्रिय गुण बन गए हैं।",
    zh_title: "è mó zhī shēng",
    zh_content: "qū fú yú chóu hèn 、 tòng kǔ hé bào lì jiù shì xiàng mó guǐ fā chū shēng yīn ； zhè xiē yǐ chéng wéi tā zuì zhēn xī de pǐn zhì 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.VOICE OF THE DEVIL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->VOICE OF THE DEVIL"
RETURN t, parent;
```

---
type: THOUGHT
name: "thought.PREDESTINED"
alias: "Thought: Predestined"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["sovereignty", "election", "lordship", "chosen", "jesus_christ"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PREDESTINED",
    alias: "Thought: Predestined",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["sovereignty", "election", "lordship", "chosen", "jesus_christ"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PREDESTINED",
    ctype: "THOUGHT",
    en_title: "Predestined",
    en_content: "",
    es_title: "PREDESTINADO",
    es_content: "Durante décadas he probado todos los métodos posibles para destruir mi Salvación.
Ahora, en la última parte de mi vida, finalmente estoy empezando a darme cuenta de que, para empezar, nunca fue mi salvación.",
    fr_title: "PRÉDESTINÉ",
    fr_content: "Pendant des décennies, j’ai essayé toutes les méthodes possibles pour détruire mon salut.
Maintenant, dans la dernière partie de ma vie, je commence enfin à réaliser que cela n’a jamais été mon salut.",
    hi_title: "पूर्वनिर्धारित",
    hi_content: "दशकों से मैंने अपनी मुक्ति को नष्ट करने के लिए हर संभव तरीका आजमाया है।
अब, अपने जीवन के उत्तरार्ध में, मुझे आखिरकार यह एहसास होने लगा है कि यह कभी भी मेरी मुक्ति की शुरुआत नहीं थी।",
    zh_title: "mìng zhōng zhù dìng",
    zh_content: "jǐ shí nián lái ， wǒ cháng shì le yī qiè kě néng de fāng fǎ lái cuī huǐ wǒ de jiù shú 。
 xiàn zài ， zài wǒ shēng mìng de hòu bàn duàn ， wǒ zhōng yú kāi shǐ yì shí dào ， zhè cóng lái dōu bú shì wǒ de jiù shú 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PREDESTINED"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE-SOVEREIGNTY->PREDESTINED"
RETURN t, parent;
```

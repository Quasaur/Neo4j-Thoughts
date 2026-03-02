---
type: THOUGHT
name: "thought.PREDESTINED"
alias: "Thought: PREDESTINED"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["sovereignty", "election", "lordship", "chosen", "jesus_christ"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PREDESTINED",
    alias: "Thought: PREDESTINED",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["sovereignty", "election", "lordship", "chosen", "jesus_christ"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PREDESTINED",
    ctype: "THOUGHT",
    en_title: "PREDESTINED",
 es_title: "PREDESTINADO",
 fr_title: "PRÉDESTINÉ",
 hi_title: "पूर्वनिर्धारित",
 zh_title: "mìng zhōng zhù dìng",
    en_content: "",
 es_content: "Durante décadas he probado todos los métodos posibles para destruir mi Salvación.
Ahora, en la última parte de mi vida, finalmente estoy empezando a darme cuenta de que, para empezar, nunca fue mi salvación.",
 fr_content: "Pendant des décennies, j’ai essayé toutes les méthodes possibles pour détruire mon salut.
Maintenant, dans la dernière partie de ma vie, je commence enfin à réaliser que cela n’a jamais été mon salut.",
 hi_content: "दशकों से मैंने अपनी मुक्ति को नष्ट करने के लिए हर संभव तरीका आजमाया है।
अब, अपने जीवन के उत्तरार्ध में, मुझे आखिरकार यह एहसास होने लगा है कि यह कभी भी मेरी मुक्ति की शुरुआत नहीं थी।",
 zh_content: "jǐ shí nián lái ， wǒ cháng shì le yī qiè kě néng de fāng fǎ lái cuī huǐ wǒ de jiù shú 。
 xiàn zài ， zài wǒ shēng mìng de hòu bàn duàn ， wǒ zhōng yú kāi shǐ yì shí dào ， zhè cóng lái dōu bú shì wǒ de jiù shú 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PREDESTINED" AND c.name = "content.PREDESTINED"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.PREDESTINED"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.PREDESTINED"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->PREDESTINED"}]->(child);
```
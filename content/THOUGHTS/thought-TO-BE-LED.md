---
type: THOUGHT
name: "thought.TO BE LED"
alias: "Thought: To Be Led"
parent: "topic.GRACE"
tags: ["led", "follow", "leadership", "holy_spirit", "travel"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TO BE LED",
    alias: "Thought: To Be Led",
    parent: "topic.GRACE",
    tags: ["led", "follow", "leadership", "holy_spirit", "travel"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TO BE LED",
    ctype: "THOUGHT",
    en_title: "To Be Led",
 es_title: "SER LED",
 fr_title: "A LED",
 hi_title: "द्वारा नेतृत्व",
 zh_title: "bèi LED",
    en_content: "",
 es_content: "Ser “guiado” por el Espíritu Santo significa DEJAR donde estás y lo que crees saber, e ir a algún lugar donde nunca has estado… hacia lo Desconocido (Las Partes del Reino de Dios que nunca has visto antes).",
 fr_content: "Être « conduit » par le Saint-Esprit signifie QUITTER où vous êtes et ce que vous pensez savoir, et aller quelque part où vous n’êtes jamais allé… dans l’Inconnu (les parties du Royaume de Dieu que vous n’avez jamais vues auparavant).",
 hi_content: "पवित्र आत्मा द्वारा \"नेतृत्व\" किए जाने का मतलब है कि आप जहां हैं और जो आप सोचते हैं कि आप जानते हैं उसे छोड़ दें, और ऐसी जगह चले जाएं जहां आप कभी नहीं गए हों... अज्ञात में (ईश्वर के राज्य के वे हिस्से जिन्हें आपने पहले कभी नहीं देखा है)।"नेतृत्व\" किए जाने का मतलब है कि आप जहां हैं और जो आप सोचते हैं कि आप जानते हैं उसे छोड़ दें, और ऐसी जगह चले जाएं जहां आप कभी नहीं गए हों... अज्ञात में (ईश्वर के राज्य के वे हिस्से जिन्हें आपने पहले कभी नहीं देखा है)।"नेतृत्व\" किए जाने का मतलब है कि आप जहां हैं और जो आप सोचते हैं कि आप जानते हैं उसे छोड़ दें, और ऐसी जगह चले जाएं जहां आप कभी नहीं गए हों... अज्ञात में (ईश्वर के राज्य के वे हिस्से जिन्हें आपने पहले कभी नहीं देखा है)।"नेतृत्व\" किए जाने का मतलब है कि आप जहां हैं और जो आप सोचते हैं कि आप जानते हैं उसे छोड़ दें, और ऐसी जगह चले जाएं जहां आप कभी नहीं गए हों... अज्ञात में (ईश्वर के राज्य के वे हिस्से जिन्हें आपने पहले कभी नहीं देखा है)।",
 zh_content: "bèi shèng líng “ yǐn dǎo ” yì wèi zhe lí kāi nǐ suǒ zài de dì fāng hé nǐ rèn wéi nǐ zhī dào de dōng xī ， qù nǐ cóng wèi qù guò de dì fāng …… jìn rù wèi zhī de dì fāng （ nǐ yǐ qián cóng wèi jiàn guò de shén guó dù de bù fèn ）。"नेतृत्व\" किए जाने का मतलब है कि आप जहां हैं और जो आप सोचते हैं कि आप जानते हैं उसे छोड़ दें, और ऐसी जगह चले जाएं जहां आप कभी नहीं गए हों... अज्ञात में (ईश्वर के राज्य के वे हिस्से जिन्हें आपने पहले कभी नहीं देखा है)।"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TO BE LED" AND c.name = "content.TO BE LED"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.TO BE LED"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.TO BE LED"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->TO BE LED"}]->(child);
```
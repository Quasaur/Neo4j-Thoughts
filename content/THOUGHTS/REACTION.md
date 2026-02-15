---
name: "thought.REACTION"
alias: "Thought: REACTION"
type: THOUGHT
parent: "topic.PSYCHOLOGY"

tags:
- react
- feeling
- flesh
- circumstance
- truth
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
// 
CREATE (t:THOUGHT {
    name: "thought.REACTION",
    alias: "Thought: REACTION",
    parent: "topic.PSYCHOLOGY",
    tags: ["react", "feeling", "flesh", "circumstance", "truth"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.REACTION",
    en_title: "Reaction",
    en_content: "Feeling is the reaction of the flesh to circumstance. Feeling is not Truth. Just because you feel angry it doesn't mean you should be.",
    es_title: "Reacción",
    es_content: "Sentir es la reacción de la carne ante las circunstancias. Sentir no es la Verdad. Que sientas ira no significa que debas sentirla.",
    fr_title: "Réaction",
    fr_content: "Le sentiment est la réaction de la chair face aux circonstances. Le sentiment n'est pas la vérité. Ce n'est pas parce que vous vous sentez en colère que vous devriez l'être.",
    hi_title: "रिएक्शन",
    hi_content: "फीलिंग, हालात के प्रति शरीर का रिएक्शन है। फीलिंग सच नहीं है। सिर्फ इसलिए कि आपको गुस्सा आ रहा है, इसका मतलब यह नहीं है कि आपको गुस्सा आना चाहिए।",
    zh_title: "Fǎnyìng",
    zh_content: "gǎnjué shì ròutǐ duì huánjìng de fǎnyìng. Gǎnjué bìngfēi zhēnlǐ. Jǐnjǐn yīnwèi nǐ gǎndào fènnù, bìng bù yìwèizhe nǐ jiù yīnggāi fènnù."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REACTION" AND c.name = "content.REACTION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.REACTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.REACTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->REACTION"}]->(child);
```
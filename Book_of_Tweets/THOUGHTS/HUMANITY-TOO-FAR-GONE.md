---
name: "thought.HUMANITY TOO FAR GONE"
alias: "Thought: Humanity Too Far Gone"
type: THOUGHT
en_content: "The Bible teaches that humanity is too far gone to have any desire for the One True God; God has to put it in us to save us."
parent: "topic.GRACE"
tags:
- salvation
- humanity
- grace
- god
- desire
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.HUMANITY TOO FAR GONE",
    alias: "Thought: Humanity Too Far Gone",
    parent: "topic.GRACE",
    tags: ['salvation', 'humanity', 'grace', 'god', 'desire'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMANITY TOO FAR GONE",
    en_title: "Humanity Too Far Gone",
    en_content: "The Bible teaches that humanity is too far gone to have any desire for the One True God; God has to put it in us to save us.",
    es_title: "La Humanidad Demasiado Perdida",
    es_content: "La Biblia enseña que la humanidad está demasiado perdida para tener algún deseo por el Único Dios Verdadero; Dios tiene que ponerlo en nosotros para salvarnos.",
    fr_title: "L'Humanité Trop Corrompue",
    fr_content: "La Bible enseigne que l'humanité est trop corrompue pour avoir le moindre désir pour le Seul Vrai Dieu ; Dieu doit le mettre en nous pour nous sauver.",
    hi_title: "मानवता अत्यधिक पतित",
    hi_content: "बाइबल सिखाती है कि मानवता एक सच्चे परमेश्वर के लिए कोई इच्छा रखने के लिए अत्यधिक पतित हो गई है; परमेश्वर को हमें बचाने के लिए हमारे अंदर इसे डालना पड़ता है।",
    zh_title: "Rén lèi guò yú duò luò",
    zh_content: "Shèng jīng jiào dǎo shuō rén lèi guò yú duò luò, wú fǎ duì dú yī zhēn shén chǎn shēng rèn hé kě wàng; Shàng dì bì xū jiāng cǐ fàng rù wǒ men xīn zhōng cái néng zhěng jiù wǒ men."
});

MATCH (t:THOUGHT {name: "thought.HUMANITY TOO FAR GONE"})
MATCH (c:CONTENT {name: "content.HUMANITY TOO FAR GONE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.HUMANITY TOO FAR GONE" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.HUMANITY TOO FAR GONE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >HUMANITY TOO FAR GONE" }]->(child);
```

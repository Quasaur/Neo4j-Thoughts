---
name: "thought.GOD THE ANSWER"
alias: "Thought: God The Answer"
type: THOUGHT
en_content: "The fact that God is That Single Answer does not in any way diminish the wonder of His Creation."
parent: "topic.THE GODHEAD"
tags:
- god
- creation
- wonder
- answer
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011h)
CREATE (t:THOUGHT {
    name: "thought.GOD THE ANSWER",
    alias: "Thought: God The Answer",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'creation', 'wonder', 'answer', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD THE ANSWER",
    en_title: "God The Answer",
    en_content: "The fact that God is That Single Answer does not in any way diminish the wonder of His Creation.",
    es_title: "Dios es la Respuesta",
    es_content: "El hecho de que Dios sea Esa Única Respuesta no disminuye en modo alguno la maravilla de Su Creación.",
    fr_title: "Dieu est la Réponse",
    fr_content: "Le fait que Dieu soit Cette Réponse Unique ne diminue en rien l'émerveillement de Sa Création.",
    hi_title: "परमेश्वर उत्तर है",
    hi_content: "यह तथ्य कि परमेश्वर वह एकमात्र उत्तर हैं, उनकी सृष्टि के विस्मय को किसी भी तरह से कम नहीं करता।",
    zh_title: "Shàngdì shì dá'àn  shàng dì shì dá àn",
    zh_content: "Shàngdì shì nà wéiyī dá'àn zhè yī shìshí, jué bù huì ǒnshǐ tā chuàngzào de qí migu.  shàng dì shì nà wéi yī dá àn zhè yī shì shí ， jué bú huì jiǎn ruò tā chuàng zào de qí jì 。"
});

MATCH (t:THOUGHT {name: "thought.GOD THE ANSWER"})
MATCH (c:CONTENT {name: "content.GOD THE ANSWER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD THE ANSWER" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD THE ANSWER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GOD THE ANSWER" }]->(child);
```

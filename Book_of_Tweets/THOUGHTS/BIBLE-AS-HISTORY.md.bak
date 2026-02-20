---
name: "thought.BIBLE AS HISTORY"
alias: "Thought: Bible As History"
type: THOUGHT
en_content: "The Bible says that God cannot lie. If therefore the Bible is not an ACCURATE HISTORICAL DOCUMENT, then it cannot be inspired by God."
parent: "topic.TRUTH"
tags:
- bible
- truth
- history
- inspiration
- document
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.BIBLE AS HISTORY",
    alias: "Thought: Bible As History",
    parent: "topic.TRUTH",
    tags: ['bible', 'truth', 'history', 'inspiration', 'document'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BIBLE AS HISTORY",
    en_title: "Bible As History",
    en_content: "The Bible says that God cannot lie. If therefore the Bible is not an ACCURATE HISTORICAL DOCUMENT, then it cannot be inspired by God.",
    es_title: "La Biblia como Historia",
    es_content: "La Biblia dice que Dios no puede mentir. Si por lo tanto la Biblia no es un DOCUMENTO HISTÓRICO PRECISO, entonces no puede ser inspirada por Dios.",
    fr_title: "La Bible comme Histoire",
    fr_content: "La Bible dit que Dieu ne peut pas mentir. Si donc la Bible n'est pas un DOCUMENT HISTORIQUE PRÉCIS, alors elle ne peut pas être inspirée par Dieu.",
    hi_title: "इतिहास के रूप में बाइबिल",
    hi_content: "बाइबिल कहती है कि परमेश्वर झूठ नहीं बोल सकता। इसलिए यदि बाइबिल एक सटीक ऐतिहासिक दस्तावेज़ नहीं है, तो यह परमेश्वर द्वारा प्रेरित नहीं हो सकती।",
    zh_title: "Shèngjīng zuòwéi lìshǐ 圣经作为历史",
    zh_content: "Shèngjīng shuō Shàngdì bùnéng sāhuǎng. Yīncǐ, rúguǒ Shèngjīng bùshì yīgè zhǔnquè de lìshǐ wénjiàn, nàme tā jiù bùnéng shì Shàngdì suǒ qǐfā de. 圣经说上帝不能撒谎。因此，如果圣经不是一个准确的历史文件，那么它就不能是上帝所启发的。"
});

MATCH (t:THOUGHT {name: "thought.BIBLE AS HISTORY"})
MATCH (c:CONTENT {name: "content.BIBLE AS HISTORY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.BIBLE AS HISTORY" }]->(c);

MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:THOUGHT {name: "thought.BIBLE AS HISTORY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH->BIBLE AS HISTORY" }]->(child);
```

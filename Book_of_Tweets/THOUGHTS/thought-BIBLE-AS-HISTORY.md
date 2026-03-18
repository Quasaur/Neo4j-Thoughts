---
type: THOUGHT
name: "thought.BIBLE AS HISTORY"
alias: "Thought: Bible As History"
parent: "topic.TRUTH"
en_content: "The Bible says that God cannot lie. If therefore the Bible is not an ACCURATE HISTORICAL DOCUMENT, then it cannot be inspired by God."
tags: ["bible", "truth", "history", "inspiration", "document"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Sep-2011a)
CREATE (t:THOUGHT {    name: "thought.BIBLE AS HISTORY",
    alias: "Thought: Bible As History",
    parent: "topic.TRUTH",
    tags: ['bible', 'truth', 'history', 'inspiration', 'document'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.BIBLE AS HISTORY",
    ctype: "THOUGHT",
    en_title: "Bible As History",
    en_content: "The Bible says that God cannot lie. If therefore the Bible is not an ACCURATE HISTORICAL DOCUMENT, then it cannot be inspired by God.",
    es_title: "La Biblia como Historia",
    es_content: "La Biblia dice que Dios no puede mentir. Si por lo tanto la Biblia no es un DOCUMENTO HISTÓRICO PRECISO, entonces no puede ser inspirada por Dios.",
    fr_title: "La Bible comme Histoire",
    fr_content: "La Bible dit que Dieu ne peut pas mentir. Si donc la Bible n'est pas un DOCUMENT HISTORIQUE PRÉCIS, alors elle ne peut pas être inspirée par Dieu.",
    hi_title: "इतिहास के रूप में बाइबिल",
    hi_content: "बाइबिल कहती है कि परमेश्वर झूठ नहीं बोल सकता। इसलिए यदि बाइबिल एक सटीक ऐतिहासिक दस्तावेज़ नहीं है, तो यह परमेश्वर द्वारा प्रेरित नहीं हो सकती।",
    zh_title: "Shèngjīng zuòwéi lìshǐ  shèng jīng zuò wéi lì shǐ",
    zh_content: "Shèngjīng shuō Shàngdì bùnéng sāhuǎng. Yīncǐ, rúguǒ Shèngjīng bùshì yīgè zhǔnquè de lìshǐ wénjiàn, nàme tā jiù bùnéng shì Shàngdì suǒ qǐfā de.  shèng jīng shuō shàng dì bù néng sā huǎng 。 yīn cǐ ， rú guǒ shèng jīng bú shì yí gè zhǔn què de lì shǐ wén jiàn ， nà me tā jiù bù néng shì shàng dì suǒ qǐ fā de 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BIBLE AS HISTORY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.TRUTH->BIBLE AS HISTORY"
RETURN t, parent;
```

---
type: THOUGHT
name: "thought.GOD IN CHARGE"
alias: "Thought: God in Charge"
parent: "topic.DIVINE-SOVEREIGNTY"
en_content: |
  I've been told my tweets are a bit ambiguous, so here's a moment of clarity:
   God is running your life...whether you believe He exists or not..
tags: ["belief", "truth", "control", "god", "sovereignty"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD IN CHARGE",
    alias: "Thought: God in Charge",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["belief", "truth", "control", "god", "sovereignty"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD IN CHARGE",
    ctype: "THOUGHT",
    en_title: "God in Charge",
    en_content: "I've been told my tweets are a bit ambiguous, so here's a moment of clarity:
 God is running your life...whether you believe He exists or not..",
    es_title: "DIOS A CARGO",
    es_content: "Me han dicho que mis tweets son un poco ambiguos, así que aquí hay un momento de claridad:
 Dios está dirigiendo tu vida... ya sea que creas que Él existe o no...",
    fr_title: "DIEU EN CHARGE",
    fr_content: "On m'a dit que mes tweets étaient un peu ambigus, alors voici un moment de clarté :
 Dieu dirige votre vie... que vous croyiez qu'il existe ou non.",
    hi_title: "प्रभारी भगवान",
    hi_content: "मुझे बताया गया है कि मेरे ट्वीट थोड़े अस्पष्ट हैं, इसलिए यहाँ स्पष्टता का क्षण है:
 ईश्वर आपका जीवन चला रहा है...चाहे आप विश्वास करें कि उसका अस्तित्व है या नहीं...",
    zh_title: "zhǎng guǎn zhī shén",
    zh_content: "wǒ bèi gào zhī wǒ de tuī wén yǒu diǎn hán hú ， suǒ yǐ zhè lǐ yǒu yí gè qīng xī de shí kè ：
  shàng dì zhèng zài zhǎng kòng nǐ de shēng huó …… wú lùn nǐ shì fǒu xiāng xìn tā cún zài ……"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD IN CHARGE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->GOD IN CHARGE"
RETURN t, parent;
```

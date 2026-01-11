---
name: "thought.GOD_IN_CHARGE"
alias: "Thought: GOD IN CHARGE"
type: THOUGHT
parent: topic.DIVINE-SOVEREIGNTY
tags:
- belief
- truth
- control
- god
- sovereignty
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GOD_IN_CHARGE",
    alias: "Thought: GOD IN CHARGE",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["belief", "truth", "control", "god", "sovereignty"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD_IN_CHARGE",
    en_title: "GOD IN CHARGE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD_IN_CHARGE" AND c.name = "content.GOD_IN_CHARGE"
MERGE (t)-[:HAS_CONTENT {name: "edge.GOD_IN_CHARGE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.GOD_IN_CHARGE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->GOD_IN_CHARGE"}]->(child);
```

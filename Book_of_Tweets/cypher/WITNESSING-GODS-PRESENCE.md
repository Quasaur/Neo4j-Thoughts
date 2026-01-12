---
name: "thought.WITNESSING GODS PRESENCE"
alias: "Thought: Witnessing Gods Presence"
type: THOUGHT
en_content: "We assemble to witness the manifestation of God's Presence; it is there that sins are forgiven, yokes are broken and bodies are healed."
parent: "topic.WORSHIP"
tags:
- presence
- healing
- miracles
- worship
- assembly
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2011a)
CREATE (t:THOUGHT {
    name: "thought.WITNESSING GODS PRESENCE",
    alias: "Thought: Witnessing Gods Presence",
    parent: "topic.WORSHIP",
    tags: ['presence', 'healing', 'miracles', 'worship', 'assembly'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WITNESSING GODS PRESENCE",
    en_title: "Witnessing Gods Presence",
    en_content: "We assemble to witness the manifestation of God's Presence; it is there that sins are forgiven, yokes are broken and bodies are healed.",
    es_title: "Siendo Testigos de la Presencia de Dios",
    es_content: "Nos congregamos para ser testigos de la manifestación de la Presencia de Dios; es allí donde los pecados son perdonados, los yugos son rotos y los cuerpos son sanados.",
    fr_title: "Témoigner de la Présence de Dieu",
    fr_content: "Nous nous assemblons pour témoigner de la manifestation de la Présence de Dieu; c'est là que les péchés sont pardonnés, les jougs sont brisés et les corps sont guéris.",
    hi_title: "परमेश्वर की उपस्थिति के साक्षी",
    hi_content: "हम परमेश्वर की उपस्थिति के प्रकटीकरण के साक्षी बनने के लिए एकत्रित होते हैं; यही वह स्थान है जहाँ पाप क्षमा किए जाते हैं, जूए टूटते हैं और शरीर चंगे होते हैं।",
    zh_title: "Jiànzhèng Shàngdì de Tóngzài",
    zh_content: "Wǒmen jùjí qǐlái jiànzhèng Shàngdì Tóngzài de xiǎnxiàn; zhèng shì zài nàlǐ, zuì'è dédào kuànshù, èzhòu bèi dǎpò, shēntǐ dédào yīzhì."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WITNESSING GODS PRESENCE" AND c.name = "content.WITNESSING GODS PRESENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WITNESSING GODS PRESENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WORSHIP" AND child.name = "thought.WITNESSING GODS PRESENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "WORSHIP >WITNESSING GODS PRESENCE" }]->(child);
```

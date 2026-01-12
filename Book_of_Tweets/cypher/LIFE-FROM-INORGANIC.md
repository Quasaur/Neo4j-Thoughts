---
name: "thought.LIFE FROM INORGANIC"
alias: "Thought: Life From Inorganic"
type: THOUGHT
en_content: "In 13 billion years 100 monkeys will never write a novel and life will never rise from inorganic matter without an Act of God."
parent: "topic.TRUTH"
tags:
- life
- biology
- creation
- origin
- god
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.LIFE FROM INORGANIC",
    alias: "Thought: Life From Inorganic",
    parent: "topic.TRUTH",
    tags: ['life', 'biology', 'creation', 'origin', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIFE FROM INORGANIC",
    en_title: "Life From Inorganic",
    en_content: "In 13 billion years 100 monkeys will never write a novel and life will never rise from inorganic matter without an Act of God.",
    es_title: "Vida de lo Inorgánico",
    es_content: "En 13 mil millones de años 100 monos nunca escribirán una novela y la vida nunca surgirá de la materia inorgánica sin un Acto de Dios.",
    fr_title: "La Vie à Partir de l'Inorganique",
    fr_content: "En 13 milliards d'années 100 singes n'écriront jamais un roman et la vie ne naîtra jamais de la matière inorganique sans un Acte de Dieu.",
    hi_title: "अकार्बनिक से जीवन",
    hi_content: "13 अरब वर्षों में 100 बंदर कभी कोई उपन्यास नहीं लिख सकेंगे और जीवन कभी भी अकार्बनिक पदार्थ से ईश्वर के कार्य के बिना उत्पन्न नहीं होगा।",
    zh_title: "Cong Wu Ji Wu Zhong Lai De Sheng Ming",
    zh_content: "Zai yi bai san shi yi nian li yi bai zhi hou zi yong yuan xie bu chu xiao shuo, er sheng ming ye yong yuan bu hui cong wu ji wu zhi zhong chan sheng, chu fei you Shang Di de shen ji."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LIFE FROM INORGANIC" AND c.name = "content.LIFE FROM INORGANIC"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIFE FROM INORGANIC" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.LIFE FROM INORGANIC"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >LIFE FROM INORGANIC" }]->(child);
```

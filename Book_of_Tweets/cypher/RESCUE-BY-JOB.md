---
name: "thought.RESCUE BY JOB"
alias: "Thought: Rescue By Job"
type: THOUGHT
en_content: "I wish to publicly thank God for rescuing us with a job that kept a roof over our heads and the lights on...Jesus is HOT STUFF!!!"
parent: "topic.SPIRITUALITY"
tags:
- provision
- miracle
- gratitude
- work
- god
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.RESCUE BY JOB",
    alias: "Thought: Rescue By Job",
    parent: "topic.SPIRITUALITY",
    tags: ['provision', 'miracle', 'gratitude', 'work', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.RESCUE BY JOB",
    en_title: "Rescue By Job",
    en_content: "I wish to publicly thank God for rescuing us with a job that kept a roof over our heads and the lights on...Jesus is HOT STUFF!!!",
    es_title: "Rescate Por Trabajo",
    es_content: "Deseo agradecer públicamente a Dios por rescatarnos con un trabajo que mantuvo un techo sobre nuestras cabezas y las luces encendidas...¡¡¡Jesús es INCREÍBLE!!!",
    fr_title: "Sauvé Par Un Emploi",
    fr_content: "Je souhaite remercier publiquement Dieu de nous avoir sauvés avec un emploi qui a gardé un toit au-dessus de nos têtes et les lumières allumées...Jésus est FORMIDABLE !!!",
    hi_title: "नौकरी द्वारा उद्धार",
    hi_content: "मैं सार्वजनिक रूप से परमेश्वर का धन्यवाद करना चाहता हूं कि उन्होंने हमें एक नौकरी देकर बचाया जिसने हमारे सिर पर छत और बत्तियां जलाए रखीं...यीशु अद्भुत हैं!!!",
    zh_title: "Gōngzuò Jiùshú",
    zh_content: "Wǒ xīwàng gōngkāi gǎnxiè Shàngdì yòng yī fèn gōngzuò jiùle wǒmen, ràng wǒmen yǒu wūdǐng zhē tóu, yǒu diàn kě yòng...Yēsū zhēn shì tài bàng le!!!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.RESCUE BY JOB" AND c.name = "content.RESCUE BY JOB"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RESCUE BY JOB" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.RESCUE BY JOB"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >RESCUE BY JOB" }]->(child);
```

---
name: "thought.SPARED ON FREEWAY"
alias: "Thought: Spared On Freeway"
type: THOUGHT
en_content: "I lost my brakes on the freeway last nite; but God spared me from accident and injury and I got the car home."
parent: "topic.SPIRITUALITY"
tags:
- providence
- protection
- miracle
- gratitude
- safety
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Nov-2011a)
CREATE (t:THOUGHT {
    name: "thought.SPARED ON FREEWAY",
    alias: "Thought: Spared On Freeway",
    parent: "topic.SPIRITUALITY",
    tags: ['providence', 'protection', 'miracle', 'gratitude', 'safety'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPARED ON FREEWAY",
    en_title: "Spared On Freeway",
    en_content: "I lost my brakes on the freeway last nite; but God spared me from accident and injury and I got the car home.",
    es_title: "Protegido en la Autopista",
    es_content: "Perdí los frenos en la autopista anoche; pero Dios me libró de accidentes y lesiones y logré llegar a casa con el carro.",
    fr_title: "Épargné sur l'Autoroute",
    fr_content: "J'ai perdu mes freins sur l'autoroute hier soir; mais Dieu m'a épargné d'un accident et de blessures et j'ai pu ramener la voiture à la maison.",
    hi_title: "राजमार्ग पर बचाव",
    hi_content: "कल रात राजमार्ग पर मेरी गाड़ी के ब्रेक फेल हो गए; लेकिन परमेश्वर ने मुझे दुर्घटना और चोट से बचाया और मैं गाड़ी को घर ले आया।",
    zh_title: "Zai Gaosu Gonglu Shang Bei Baohu",
    zh_content: "Zuowan wo zai gaosu gonglu shang shashe shiling le; dan Shangdi baohu wo mianyu shigu he shoushan, wo ba chezi kaihui le jia."
});

MATCH (t:THOUGHT {name: "thought.SPARED ON FREEWAY"})
MATCH (c:CONTENT {name: "content.SPARED ON FREEWAY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPARED ON FREEWAY" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.SPARED ON FREEWAY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >SPARED ON FREEWAY" }]->(child);
```

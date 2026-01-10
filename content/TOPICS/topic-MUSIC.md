---
name: topic.MUSIC
alias: "Topic: Music"
type: TOPIC
parent: topic.MUSICOLOGY
tags:
  - music
  - art
  - sound
  - harmony
  - melody
neo4j: true
ptopic: '"[[topic-MUSICOLOGY]]"'
level: 5
insert: true
---
# Topic: Music

```Cypher
CREATE (t:TOPIC {
    name: "topic.MUSIC",
    alias: "Topic: Music",
    parent: "topic.MUSICOLOGY",
    tags: ["music", "art", "sound", "harmony", "melody"],
    notes: "",
    level: 6
});

CREATE (d:DESCRIPTION {
    name: "description.MUSIC",
    en_title: "Music",
    en_content: "The art and science of combining vocal or instrumental sounds to produce beauty of form, harmony, and expression of emotion.",
    es_title: "Música",
    es_content: "El arte y la ciencia de combinar sonidos vocales o instrumentales para producir belleza de forma, armonía y expresión de emociones.",
    fr_title: "Musique",
    fr_content: "L'art et la science de combiner des sons vocaux ou instrumentaux pour produire une beauté de forme, d'harmonie et une expression d'émotion.",
    hi_title: "संगीत",
    hi_content: "संगीत रूप की सुंदरता, सद्भाव और भावना की अभिव्यक्ति का उत्पादन करने के लिए मुखर या वाद्य ध्वनियों के संयोजन की कला और विज्ञान।",
    zh_title: "yīn yuè",
    zh_content: "yīn yuè shì yī mén jié hé rén shēng huò lè qì shēng yīn yǐ chǎn shēng xíng tà sù fǎ 、 hé xié hé qíng gǎn biǎo dá de yì shù hé kē xué 。"
});

MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.MUSIC" AND d.name = "description.MUSIC"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.MUSIC"}]->(d);

MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.MUSICOLOGY" AND child.name = "topic.MUSIC"
MERGE (parent)-[:HAS_CHILD {name: "edge.MUSICOLOGY->MUSIC"}]->(child);
```

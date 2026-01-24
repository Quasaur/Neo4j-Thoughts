---
name: "thought.HOLLYWOOD VIOLENCE PREMISE"
alias: "Thought: Hollywood Violence Premise"
type: THOUGHT
en_content: The original premise of Hollywood violence was "If they're watching violence they're not committing it."...Oops!
parent: topic.WISDOM
tags:
  - violence
  - society
  - media
  - attitude
  - failure
level: 3
neo4j: true
ptopic: "[[topic-WISDOM]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jan-2013)
CREATE (t:THOUGHT {
    name: "thought.HOLLYWOOD VIOLENCE PREMISE",
    alias: "Thought: Hollywood Violence Premise",
    parent: "topic.ATTITUDE",
    tags: ['violence', 'society', 'media', 'attitude', 'failure'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HOLLYWOOD VIOLENCE PREMISE",
    en_title: "Hollywood Violence Premise",
    en_content: "The original premise of Hollywood violence was \"If they're watching violence they're not committing it.\"...Oops!",
    es_title: "Premisa de la Violencia de Hollywood",
    es_content: "La premisa original de la violencia de Hollywood era que podía mostrar la brutalidad del pecado sin glorificarla, sirviendo como una advertencia moral. Sin embargo, esta línea se ha difuminado considerablemente, y ahora gran parte del entretenimiento parece celebrar la violencia en lugar de condenarla.",
    fr_title: "Prémisse de la Violence d'Hollywood",
    fr_content: "La prémisse originale de la violence d'Hollywood était qu'elle pouvait montrer la brutalité du péché sans la glorifier, servant d'avertissement moral. Cependant, cette ligne s'est considérablement estompée, et maintenant une grande partie du divertissement semble célébrer la violence plutôt que de la condamner.",
    hi_title: "हॉलीवुड हिंसा का आधार",
    hi_content: "हॉलीवुड हिंसा का मूल आधार यह था कि यह पाप की क्रूरता को महिमामंडित किए बिना दिखा सकता है, एक नैतिक चेतावनी के रूप में काम करता है। हालांकि, यह रेखा काफी धुंधली हो गई है, और अब अधिकांश मनोरंजन हिंसा की निंदा करने के बजाय उसका जश्न मनाता प्रतीत होता है।",
    zh_title: "Hǎoláiwù Bàolì Qiántí",
    zh_content: "Hǎoláiwù bàolì de yuánshǐ qiántí shì tā kěyǐ zhǎnshì zuì'è de cánkù ér bù měihuà tā, zuòwéi dàodé jǐnggào. Rán'ér, zhè tiáo jièxiàn yǐjīng xiāngdāng móhu le, xiànzài dàbùfèn yúlè sìhū zài qìngzhù bàolì ér bùshì qiǎnzé tā."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HOLLYWOOD VIOLENCE PREMISE" AND c.name = "content.HOLLYWOOD VIOLENCE PREMISE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HOLLYWOOD VIOLENCE PREMISE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HOLLYWOOD VIOLENCE PREMISE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->HOLLYWOOD VIOLENCE PREMISE" }]->(child);
```

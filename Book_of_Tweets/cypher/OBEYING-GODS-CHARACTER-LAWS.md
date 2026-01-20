---
name: "thought.OBEYING GODS CHARACTER LAWS"
alias: "Thought: Obeying Gods Character Laws"
type: THOUGHT
en_content: "Just because it's legal, doesn't mean it's ethical or just or fair. God doesn't expect us to obey laws that violate His Character."
parent: "topic.MORALITY"
tags:
- law
- character
- god
- ethics
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.OBEYING GODS CHARACTER LAWS",
    alias: "Thought: Obeying Gods Character Laws",
    parent: "topic.MORALITY",
    tags: ['law', 'character', 'god', 'ethics', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OBEYING GODS CHARACTER LAWS",
    en_title: "Obeying Gods Character Laws",
    en_content: "Just because it's legal, doesn't mean it's ethical or just or fair. God doesn't expect us to obey laws that violate His Character.",
    es_title: "Obedeciendo las Leyes del Carácter de Dios",
    es_content: "Solo porque algo sea legal, no significa que sea ético o justo o equitativo. Dios no espera que obedezcamos leyes que violan Su Carácter.",
    fr_title: "Obéir aux Lois du Caractère de Dieu",
    fr_content: "Ce n'est pas parce que c'est légal que c'est éthique ou juste ou équitable. Dieu n'attend pas de nous que nous obéissions aux lois qui violent Son Caractère.",
    hi_title: "परमेश्वर के चरित्र नियमों का पालन",
    hi_content: "केवल इसलिए कि कुछ कानूनी है, इसका मतलब यह नहीं है कि यह नैतिक या न्यायसंगत या निष्पक्ष है। परमेश्वर यह अपेक्षा नहीं करता कि हम उन नियमों का पालन करें जो उसके चरित्र का उल्लंघन करते हैं।",
    zh_title: "Shùncóng Shàngdì Pǐngé Dìnglǜ",
    zh_content: "Jǐnjǐn yīnwèi mǒushì shì hélǐ de, bù yìwèizhe tā shì dàodé de huò gōngzhèng de huò gōngpíng de. Shàngdì bù qīwàng wǒmen zūnshǒu wéibèi Tā Pǐngé de fǎlǜ."
});

MATCH (t:THOUGHT {name: "thought.OBEYING GODS CHARACTER LAWS"})
MATCH (c:CONTENT {name: "content.OBEYING GODS CHARACTER LAWS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.OBEYING GODS CHARACTER LAWS" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.OBEYING GODS CHARACTER LAWS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >OBEYING GODS CHARACTER LAWS" }]->(child);
```

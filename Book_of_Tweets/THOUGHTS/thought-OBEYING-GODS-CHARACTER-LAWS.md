---
type: THOUGHT
name: "thought.OBEYING GODS CHARACTER LAWS"
alias: "Thought: Obeying Gods Character Laws"
parent: "topic.MORALITY"
en_content: "Just because it's legal, doesn't mean it's ethical or just or fair. God doesn't expect us to obey laws that violate His Character."
tags: ["law", "character", "god", "ethics", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Sep-2013a)
CREATE (t:THOUGHT {    name: "thought.OBEYING GODS CHARACTER LAWS",
    alias: "Thought: Obeying Gods Character Laws",
    parent: "topic.MORALITY",
    tags: ['law', 'character', 'god', 'ethics', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.OBEYING GODS CHARACTER LAWS",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.OBEYING GODS CHARACTER LAWS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->OBEYING GODS CHARACTER LAWS"
RETURN t, parent;
```

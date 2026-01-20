---
name: "passage.PRICELESS WISDOM"
alias: "Passage: The Greatest Treasure"
type: PASSAGE
parent: topic.WISDOM
tags:
- wisdom
- understanding
- riches
- treeoflife
- peace
neo4j: true
ptopic: "[[topic-WISDOM]]"
level: 3
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (p:PASSAGE {
	    name: "passage.PRICELESS WISDOM",
		alias: "Passage: The Greatest Treasure", 
		parent: "topic.WISDOM", 
		tags: ["wise", "inherit", "honor", "fools", "disgrace"], 
		source: "Proverbs 3:35",
		sortedsource: "Proverbs 03:35",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%203%3A35&version=ESV",
		notes: "",
		level: 3});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.PRICELESS WISDOM",
	ctype: 3, // 1=thought; 2=quote; 3=passage
	en_title: "PRICELESS WISDOM", 
	en_content: "Blessed is a person who finds wisdom,
And one who obtains understanding.
For her profit is better than the profit of silver,
And her produce better than gold.
She is more precious than jewels,
And nothing you desire compares with her.
Long life is in her right hand;
In her left hand are riches and honor.
Her ways are pleasant ways,
And all her paths are peace.
She is a tree of life to those who take hold of her,
And happy are those who hold on to her.", 
	es_title: "Sabiduría Invaluable", 
	es_content: "Bienaventurado el que halla sabiduría,
y el que alcanza entendimiento.
Porque sus ganancias son mejores que las de la plata,
y sus frutos, mejores que el oro.
Es más preciosa que las joyas,
y nada de lo que deseas se compara con ella.
Larga vida está en su mano derecha;
en su mano izquierda, riquezas y honor.
Sus caminos son agradables,
y todas sus sendas, paz.
Es árbol de vida para quienes se aferran a ella,
y dichosos los que se aferran a ella.", 
	fr_title: "Sagesse inestimable", 
	fr_content: "Heureux l'homme qui trouve la sagesse,
et celui qui acquiert l'intelligence.
Car son profit vaut mieux que le profit de l'argent,
et ses produits sont meilleurs que l'or.
Elle est plus précieuse que les joyaux,
et rien de ce que vous désirez ne lui est comparable.
Longue vie est dans sa main droite ;
Dans sa main gauche sont richesse et honneur.
Ses voies sont des voies agréables,
et tous ses sentiers sont paix.
Elle est un arbre de vie pour ceux qui la saisissent,
et heureux ceux qui la retiennent.", 
	hi_title: "अमूल्य बुद्धि", 
	hi_content: "धन्य है वह व्यक्ति जो बुद्धि पाता है,
और वह जो समझ प्राप्त करता है।
क्योंकि उसका लाभ चाँदी के लाभ से भी उत्तम है,
और उसकी उपज सोने से भी उत्तम है।
वह रत्नों से भी अधिक मूल्यवान है,
और उसकी कोई भी इच्छा उसकी बराबरी नहीं कर सकती।
उसके दाहिने हाथ में दीर्घायु है;
उसके बाएँ हाथ में धन और सम्मान है।
उसके मार्ग सुखद हैं,
और उसके सभी मार्ग शांतिमय हैं।
जो उसे थाम लेते हैं, उनके लिए वह जीवन का वृक्ष है,
और जो उससे जुड़े रहते हैं, वे धन्य हैं।", 
	zh_title: "Wú jià de zhìhuì", 
	zh_content: "xún dé zhìhuì de rén yǒufúle,
huòdé cōngmíng de rén yǒufúle.
Yīnwèi tā de yìchu shèngguò yínzǐ de yìchu,
tā de chūchǎn shèngguò huángjīn.
Tā bǐ zhūbǎo gèng zhēnguì,
nǐ suǒ kěwàng de yīqiè dōu wú kě bǐnǐ.
Tā yòushǒu wòzhe chángshòu,
tā zuǒshǒu wòzhe cáifù hé zūn róng.
Tā de dàolù shì ānlè zhī lù,
tā de yīqiè lùtú dōu shì píng'ān.
Tā duì nàxiē zhuā zhù tā de rén, jiùshì shēngmìng shù;
nàxiē jǐn jǐn zhuā zhù tā de rén yǒufúle."});
// link content to node
MATCH (p:PASSAGE {name: 'passage.PRICELESS WISDOM'})
MATCH (c:CONTENT {name: 'content.PRICELESS WISDOM'})
MERGE (p)-[:HAS_CONTENT {name: "p.edge.PRICELESS WISDOM"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC {name: 'topic.HUMILITY'})
MATCH (child:PASSAGE {name: 'passage.PRICELESS WISDOM'})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.HUMILITY->PRICELESS WISDOM"}]->(child)
RETURN *;

```

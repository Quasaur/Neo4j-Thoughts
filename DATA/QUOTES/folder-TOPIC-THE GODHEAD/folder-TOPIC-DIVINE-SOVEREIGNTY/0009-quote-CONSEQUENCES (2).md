```Cypher
//create the Thought with the same fields as a normal thought
CREATE (q:QUOTE {
	    name: "quote.CONSEQUENCES (2)",
		alias: "Quote: Decisiions have Consequences", 
		parent: "topic.DIVINE SOVEREIGNTY", 
		tags: ["decisions", "outcomes", "god", "sovereignty", "volition"], 
		source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide",
		booklink: "https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J",
		notes: "",
		level: 2});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.CONSEQUENCES (2)",
	ctype: 2, // 1=thought; 2=quote; 3=passage
	en_title: "CONSEQUENCES (2)", 
	en_content: "Every sentient being is a 'free-will' agent and can make decisions (acts of the will) to determine their destiny, but ONLY GOD DETERMINES THE CONSEQUENCES OF THOSE DECISIONS AND ACTIONS. The Jew who assisted in the weaponization of Zyklon gas for use in World War I had no idea his government would use the same gas to exterminate millions of European Jews in World War II. In the same way, neither you nor I can imagine the far-reaching consequences of the decisions we make today.", 
	es_title: "Consecuencias (2)", 
	es_content: "Todo ser sintiente es un agente con libre albedrío y puede tomar decisiones (actos de voluntad) para determinar su destino, pero SOLO DIOS DETERMINA LAS CONSECUENCIAS DE ESAS DECISIONES Y ACCIONES. El judío que colaboró ​​en la militarización del gas Zyklon para su uso en la Primera Guerra Mundial no tenía ni idea de que su gobierno usaría el mismo gas para exterminar a millones de judíos europeos en la Segunda Guerra Mundial. De la misma manera, ni tú ni yo podemos imaginar las consecuencias de gran alcance de las decisiones que tomamos hoy.", 
	fr_title: "Conséquences (2)", 
	fr_content: "Tout être sensible est un agent doté du libre arbitre et peut prendre des décisions (actes de volonté) pour déterminer son destin, mais SEUL DIEU DÉTERMINE LES CONSÉQUENCES DE CES DÉCISIONS ET DE CES ACTIONS. Le Juif qui a contribué à l'utilisation du gaz Zyklon comme arme pendant la Première Guerre mondiale ignorait que son gouvernement utiliserait ce même gaz pour exterminer des millions de Juifs européens pendant la Seconde Guerre mondiale. De même, ni vous ni moi ne pouvons imaginer l'ampleur des conséquences des décisions que nous prenons aujourd'hui.", 
	hi_title: "परिणाम (2)",
	hi_content: "प्रत्येक संवेदनशील प्राणी एक 'स्वतंत्र इच्छाशक्ति' वाला व्यक्ति है और अपनी नियति निर्धारित करने के लिए निर्णय (इच्छाशक्ति के कार्य) ले सकता है, लेकिन केवल ईश्वर ही उन निर्णयों और कार्यों के परिणाम निर्धारित करता है। जिस यहूदी ने प्रथम विश्व युद्ध में ज़ाइक्लोन गैस के हथियारीकरण में सहायता की थी, उसे इस बात का ज़रा भी अंदाज़ा नहीं था कि उसकी सरकार द्वितीय विश्व युद्ध में लाखों यूरोपीय यहूदियों का सफाया करने के लिए उसी गैस का इस्तेमाल करेगी। उसी तरह, न तो आप और न ही मैं आज हमारे द्वारा लिए गए निर्णयों के दूरगामी परिणामों की कल्पना कर सकते हैं।",
	zh_title: "Hòuguǒ (2)",
	zh_content: "měi gè yǒuyìshí de zhòngshēng dōu shì yǒngyǒu “zìyóu yìzhì” de zhǔtǐ, kěyǐ zuò chū juédìng (yìzhì xíngwéi) lái juédìng zìjǐ de mìngyùn, dàn zhǐyǒu shàngdì cáinéng juédìng zhèxiē juédìng hé xíngdòng de hòuguǒ. Zài dì yī cì shìjiè dàzhàn zhōng xiézhù jiāng qí kèlóng dúqì wǔqì huà de yóutàirén, gēnběn méi xiǎngdào tā de zhèngfǔ huì zài dì èr cì shìjiè dàzhàn zhōng shǐyòng tóngyàng de dúqì mièjué shù bǎi wàn ōuzhōu yóutàirén. Tóngyàng, nǐ wǒ dū wúfǎ xiǎngxiàng wǒmen jīntiān suǒ zuò de juédìng jiāng dài lái duōme shēnyuǎn de hòuguǒ."});
// link content to node
MATCH (q:QUOTE)
MATCH (c:CONTENT)
WHERE q.name = 'quote.CONSEQUENCES (2)' AND c.name = 'content.CONSEQUENCES (2)'
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CONSEQUENCES (2)"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:QUOTE)
WHERE parent.name = 'topic.DIVINE SOVEREIGNTY' AND child.name = 'quote.CONSEQUENCES (2)'
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE SOVEREIGNTY->CONSEQUENCES (2)"}]->(child)
RETURN *;

```
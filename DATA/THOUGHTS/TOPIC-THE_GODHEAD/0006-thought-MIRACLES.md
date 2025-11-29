```Cypher
//create the Thought with the same fields as a normal thought
CREATE (t:THOUGHT
    {
	    name: "thought.MIRACLES",
		alias: "Thought: Acts of God", 
		parent: "topic.THE GODHEAD", 
		tags: ["miracles", "acts_of_god", "divine_power", "glory_of_god", "signs"], 
		notes: "",
		level: 1});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.MIRACLES", 
	en_title: "MIRACLES", 
	en_content: "Miracles are...  
...the only Acts God has ever done,  
the only Acts God is doing,  
and the only Acts God will ever do!", 
	es_title: "MILAGROS", 
	es_content: "Los milagros son...
...los únicos actos que Dios ha hecho,
los únicos actos que Dios está haciendo,
y los únicos actos que Dios hará.", 
	fr_title: "MIRACLES", 
	fr_content: "Les miracles sont...
...les seuls actes que Dieu ait jamais accomplis,
les seuls actes que Dieu accomplit,
et les seuls actes que Dieu accomplira jamais !", 
	hi_title: "चमत्कार", 
	hi_content: "चमत्कार...
...केवल वही कार्य हैं जो भगवान ने कभी किए हैं,
केवल वही कार्य जो भगवान कर रहे हैं,
और केवल वही कार्य हैं जो भगवान कभी करेंगे!", 
	zh_title: "Qíjì", 
	zh_content: "qíjì shì……
……shì shàngdì céngjīng zuòguò de wéiyī shìjì,
shì shàngdì zhèngzài zuò de wéiyī shìjì,
yěshì shàngdì jiānglái yào zuò de wéiyī shìjì!"});
// link content to node
MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MIRACLES" AND c.name = "content.MIRACLES"
MERGE (t)-[:HAS_CONTENT {name: "edge.MIRACLES"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MIRACLES"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->MIRACLES"}]->(child)
RETURN *;

```
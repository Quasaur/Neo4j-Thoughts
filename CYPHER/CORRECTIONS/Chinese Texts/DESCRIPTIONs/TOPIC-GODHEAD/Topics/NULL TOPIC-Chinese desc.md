## The original Query:

```Cypher
CREATE (d:DESCRIPTION {
	name: "desc.NULL_TOPIC", 
	en_title: "Null Topic", 
	en_content: "This is the NULL TOPIC: the root of the Book of Thoughts graph database.", 
	es_title: "Tema Nulo", 
	es_content: "Este es el TEMA NULO: la raíz de la base de datos gráfica del Libro de Pensamientos.", 
	fr_title: "Thème racine", 
	fr_content: "Il s'agit du SUJET NULL : la racine de la base de données graphique du Livre des Pensées.", 
	hi_title: "मूल विषय", 
	hi_content: "यह शून्य विषय है: विचारों की पुस्तक ग्राफ डेटाबेस का मूल।", 
	zh_title: "根主题", 
	zh_content: "这是 NULL TOPIC：思想之书图形数据库的根"});
```

## Latine Text:

```Cypher
CREATE (d:DESCRIPTION {
	name: "desc.NULL_TOPIC", 
	en_title: "Null Topic", 
	en_content: "This is the NULL TOPIC: the root of the Book of Thoughts graph database.", 
	es_title: "Tema Nulo", 
	es_content: "Este es el TEMA NULO: la raíz de la base de datos gráfica del Libro de Pensamientos.", 
	fr_title: "Thème racine", 
	fr_content: "Il s'agit du SUJET NULL : la racine de la base de données graphique du Livre des Pensées.", 
	hi_title: "मूल विषय", 
	hi_content: "यह शून्य विषय है: विचारों की पुस्तक ग्राफ डेटाबेस का मूल।", 
	zh_title: "Zhēnlǐ", 
	zh_content: "chāoyuè de gēnběn huò jīngshén xiànshí."});
```

## Query to Change:

```Cypher
MATCH (en_title: "Null Topic"})
SET n.zh_title = 'Zhēnlǐ'
SET n.zh_content = "chāoyuè de gēnběn huò jīngshén xiànshí.";
```
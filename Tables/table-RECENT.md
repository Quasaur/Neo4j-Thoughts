---
title: "Table: RECENT"
draft: true
type: hiddentable
---
# Table: RECENT (hidden)
```dataview
TABLE 
	level AS "Level",
	ptopic AS "Topic",
	ptopic.level AS "Topic Level",
	dateformat(file.mtime, "yyyy.MM.dd") as "Last Modified*",
	type AS "Type"
   FROM "content"
   WHERE type != "PAGE" AND type != "TABLE" AND draft = false
   SORT file.mtime DESC
   LIMIT 108
```


## Dataview
parent:: [[content/index]]

## Snippets
```dataview
WHERE type = THOUGHT OR type = QUOTE OR type = PASSAGE OR type = TOPIC
```
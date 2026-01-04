---
title: "Table: MultiLingual"
draft: true
type: hiddentable
---
# Table: MultiLingual (hidden)
```dataview
TABLE 
	mling as "MultiLingual",
	level AS "Level",
	ptopic AS "Topic",
	ptopic.level AS "Topic Level",
	dateformat(file.mtime, "yyyy.MM.dd") as "Last Modified*",
	type AS "Type"
   FROM "content"
   WHERE draft = false AND mling = true
   SORT file.mtime DESC
   LIMIT 40
```


## Dataview
parent:: [[content/index]]

## Snippets

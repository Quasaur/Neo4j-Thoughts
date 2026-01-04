---
title: "Table: QUOTES (by File)"
draft: true
type: hiddentable
---
# Table: QUOTES (by File)
```dataview
TABLE WITHOUT ID
	file.link AS "File*",
	level AS "Level",
	source AS "Book",
	ptopic AS "Topic",
	ptopic.level AS "Topic Level"
FROM "content/QUOTES"
SORT title ASCENDING
```

## Dataview
parent:: [[content/index]]

## Snippets
```dataview

WHERE type != "THOUGHT"

social AS "Social Tags"

```
---
title: "Table: PASSAGES"
draft: true
type: hiddentable
---
# Table: PASSAGES (hidden)

```dataview
TABLE WITHOUT ID
	file.link AS "File*",
	source AS "Verse(s)",
	level AS "Passage Level",
	ptopic AS "Topic",
	ptopic.level AS "Topic Level"
   FROM "content/BIBLE"
   SORT file.link ASCENDING
```


## Dataview
parent:: [[content/index]]

## Snippets

```dataview
 WHERE type != "THOUGHT"

social AS "Social Tags"
```
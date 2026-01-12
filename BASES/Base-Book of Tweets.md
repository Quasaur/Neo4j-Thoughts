```base
view: View-Thoughts
folder: Book_of_Tweets/
columns:
views:
  - type: table
    name: Book of Thoughts
    filters:
      and:
        - file.folder == "Book_of_Tweets/cypher"
    groupBy:
      property: parent
      direction: ASC
    order:
      - file.name
      - name
      - parent
      - neo4j
      - level
      - ptopic
      - en_content
    sort:
      - property: parent
        direction: ASC
      - property: level
        direction: ASC
      - property: name
        direction: ASC
    columnSize:
      file.name: 178
      file.path: 334
      note.name: 287
      note.parent: 175
      note.insert: 104
      note.level: 101
      note.ptopic: 190
    rowHeight: medium

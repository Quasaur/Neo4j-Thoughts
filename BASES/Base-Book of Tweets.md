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
      note.name: 199
      note.parent: 175
      note.level: 78
      note.ptopic: 271
    rowHeight: medium

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
      - file.path
      - name
      - insert
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
      file.path: 300
      note.name: 287
      note.insert: 150
      note.level: 171
      note.ptopic: 153
    rowHeight: medium

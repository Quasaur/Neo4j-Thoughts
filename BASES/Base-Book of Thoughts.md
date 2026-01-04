```base
view: View-Thoughts
folder: Book_of_Thoughts/
columns:
views:
  - type: table
    name: Book of Thoughts
    filters:
      and:
        - file.folder == "Book_of_Tweets/cypher"
    order:
      - file.name
      - level
      - parent
      - en_content
    sort:
      - property: level
        direction: ASC
      - property: parent
        direction: ASC
    columnSize:
      file.name: 285
      note.type: 114
      note.parent: 302
      file.folder: 265

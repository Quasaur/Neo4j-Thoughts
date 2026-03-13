# Prompts
## Prompt 1
dos/reports/neo4j_auradb_descripancies.md contains a report you produced for me yesterday; I need you to run the report again (comparing the Neo4j AuraDB online instance with the content folder in this repo). For this report i need you to review the content folder exclusively. you may access the python folder recursively for access to existing scripts used to access the Neo4j AuraDB instance, along with any python environment resources you require. You may edit the current report markdown file with the new results.

## Prompt 2
docs/Naming/naming_01_file_names.md is finished; check all node markdown file names in both the content and Book_of_Tweets folder against that markdown file and make any necessary corrections in the file names. When you're done place the report in the docs/reports/filename_[corrections_27-Feb-2026@1505.md](mailto:corrections_27-Feb-2026@1505.md) and report to me.

## Prompt 3
In the document docs/reports/edge_case_issues.md i have added responses to the remaining edge case issues. Search the content folder recursively for every markdown file that contains a Cypher block. Audit and make corrections in every qualified file based on the material in the docs/Naming folder. Make a report of discrepancies found and how they were corrected, along a list of discrepancies that could not be corrected, and add them to a markdown file in the docs/reports folder; Make sure the file name containing the report includes a date & time stamp.

## Prompt 4
Compare the content folder (recursively) against the documents in the docs/Naming folder and identify discrepan
cies or violatiions of the standards established in the docs/Naming folder, and document those discrepancies in a
new markdown document in the docs/reports folder, including the file creation timestampt in its file name.

## Prompt 5
Compare the content/QUOTES folder against the documents in the docs/Naming folder and identify any errors, discrepancies or violations of the standards established by the markdown files in the docs/Naming folder, and document those discrepancies in a
new markdown document in the docs/reports folder, including the file creation timestamp in its file name.

## Prompt 6
The markdown files in the content/QUOTES folder are considered source of truth. Connect to the Neo4j AuraDB online instance and compare all of the QUOTE nodes and their connected CONTENT nodes against the Cypher blocks in the markdown files of the content/QUOTES folder and refactor or replace any AuraDB QUOTE node property or the QUOTE node's connected CONTENT node properties with those in the Cypher blocks of the markdown files in the content/QUOTES folder.

## Prompt 7
Whatever nodes that exist in the content/QUOTES folder that are missing in the AuraDB online instance you must upload to the AuraDB. When all is done, there should be 80 QUOTE nodes in the AuraDB; any QUOTE nodes in the AuraDB that do not exist in the content/QUOTES folder you must delete along with their relationships and child nodes.
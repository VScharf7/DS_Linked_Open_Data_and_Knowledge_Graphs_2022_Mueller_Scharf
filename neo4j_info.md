## loading csv with headers
## creating nodes one by one


__nodes existing__: 
ID	
SRNA_NAME	= Name der sRNA 
TARGET_NAME 	= Name des von der sRNA
TAXID		= Taxonomische ID
ORG_CODE 	= Organismus Code des Bakteriums
STRAIN_NAME 	= Erregerstamm
SRNA_TYPE 	= 0: NA, 1: trans-encoded antisense RNA, 2: cis-enoded -"-
SRNA_LENGTH 	= Länge der sRNA (Menge der Nukleotide)
SRNA_START 	= Startpunkt 
SRNA_END 	= Endpunkt
SRNA_STRAND 	= 
TARGET_TYPE 	=
TARGET_LENGTH 	= Länge des Targets
TARGET_START 	= Startpunkt
TARGET_END 	= Endpunkt
TARGET_STRAND 	= 
REGULATION	= Was durch die sRNA re



LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/VScharf7/DS_Linked_Open_Data_and_Knowledge_Graphs_2022_Mueller_Scharf/main/Data/sRNATarBase3short.csv' AS row
CREATE (a:sRNA {Name: row.SRNA_NAME, sRNA_start: row.SRNA_START, sRNA_end: row.SRNA_END})
CREATE (b:Target {Name: row.TARGET_NAME, Target_start: row.TARGET_START, Target_end: row.TARGET_END})
CREATE (c:Strain {Name: row.STRAIN_NAME, Code: row.ORG_CODE, TaxID: row.TAXID})
CREATE (d:sRNA_Start {Start_Position: row.SRNA_START})
CREATE (e:sRNA_Stop {Stop_Position: row.SRNA_END})
CREATE (f:sRNA_Length {sRNA_Lenght: row.SRNA_LENGHT})
CREATE (g:sRNA_Type {sRNA_Type: row.SRNA_TYPE})
CREATE (h:Target_Start {Start_Position: row.TARGET_START})
CREATE (i:Target_Stop {Stop_Position: row.TARGET_END})
CREATE (j:Target_Length {Target_Lenght: row.TARGET_LENGTH})
CREATE (c)-[:host_of]->(a)
CREATE (a)-[:hosted_by]->(c)
CREATE (a)-[:starts_at]->(d)
CREATE (a)-[:ends_at]->(e)
CREATE (a)-[:length]->(f)
CREATE (a)-[:is_of_type]->(g)
CREATE (b)-[:starts_at]->(h)
CREATE (b)-[:ends_at]->(i)
CREATE (b)-[:length]->(j)
CREATE (a)-[:affects]->(b)
CREATE (b)-[:is_affected]->(a)

return *

## Mögliche Abfragen:

- zeige alle srnas von gleichem Strain
- zeige Strains von gleicher srna


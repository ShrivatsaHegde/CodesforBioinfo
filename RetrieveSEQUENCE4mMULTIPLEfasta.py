import re
pattern_Accession = "^>\w\w\|(\w+)\|(\w+)" # Retrieve Uniprot Accession
print ("The list of protein Accession Ids: ")
with open('uniprot-rv0183.fasta') as fh:
    data=fh.readlines() # Discard the first line.
rgx_Acc = re.compile(pattern_Accession)
seq=''
seq_data={}
for line in data:
    #print (line.strip())
    result_Acc = rgx_Acc.search(line)
    if (result_Acc):
        print(result_Acc.group(1))#,"\t",result_Acc.group(2))
        accession=result_Acc.group(1)
        seq_data[accession]=""
        seq=''
        result_Acc=False
    elif not(result_Acc):
        seq+=line.strip()
        seq_data[accession]=seq
#print (dict(seq_data))        

print ("Enter the primary accession Id {case sensitive}")
accession=input().strip()
#print(accession)
try:
    print(seq_data[accession])
except KeyError:
    print("The UniProt Id does not exist in the sequence file")
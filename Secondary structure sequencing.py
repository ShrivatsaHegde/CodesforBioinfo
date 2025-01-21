from email import header
table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

def gen(seq,codon):
    protein=""
    for i in range(0, len(seq), 3):
            code=seq[i:i + 3]
            protein=protein+codon[code]
    return protein

def orf(seq):
    frames=[]
    frames.append([dnaseq[i:i + 3] for i in range(0,len(dnaseq),3)])
    frames.append([dnaseq[i:i + 3] for i in range(1,len(dnaseq),3)])
    frames.append([dnaseq[i:i + 3] for i in range(2,len(dnaseq),3)])
    frames.append([revdna[i:i + 3] for i in range(0,len(revdna),3)])
    frames.append([revdna[i:i + 3] for i in range(1,len(revdna),3)])
    frames.append([revdna[i:i + 3] for i in range(2,len(revdna),3)])
    return frames

f=open ("C:\python 2nd sem\RV3802C.txt")
header=f.readline()
dnaseq=f.read()
dnaseq=dnaseq.replace("\n","")
dnaseq=dnaseq.upper()
print("DNA sequence is:",dnaseq)
cdna=''
for i in dnaseq:
    if i=="T":
        cdna=cdna+"A"
    elif i=="A":
        cdna=cdna+"T"
    elif i=="C":
        cdna=cdna+"G"
    elif i=="G":
        cdna=cdna+"C"    
    else:
        cdna=cdna+i
print("Compliment is:",cdna)
revdna=cdna[::-1]
print("Reverse compliment is:",revdna)
rnaseq=''
for i in dnaseq:
    if i=="T":
        rnaseq=rnaseq+"U"
    else:
        rnaseq=rnaseq+i
print("RNA sequence is:",rnaseq) 
print("Protein sequence of gen:",gen(dnaseq,table))
print("Open Reading Frames are:\n",orf(dnaseq))
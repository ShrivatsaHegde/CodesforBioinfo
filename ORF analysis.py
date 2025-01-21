def gen1(seq):

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
    protein =""
    if len(seq)%3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein+= table[codon]
    return protein

def orf(seq):
    frames=[]
    frames.append([dna_seq[i:i + 3] for i in range(0,len(dna_seq),3)])
    frames.append([dna_seq[i:i + 3] for i in range(1,len(dna_seq),3)])
    frames.append([dna_seq[i:i + 3] for i in range(2,len(dna_seq),3)])
    frames.append([revdna[i:i + 3] for i in range(0,len(revdna),3)])
    frames.append([revdna[i:i + 3] for i in range(1,len(revdna),3)])
    frames.append([revdna[i:i + 3] for i in range(2,len(revdna),3)])
    return frames

f=open("RV3802C.txt")
header=f.readline()
dnaseq=f.read()
dnaseq=dnaseq.replace("\n","")
dna_seq=dnaseq.upper()
print("DNA sequence is:",dna_seq)
cdna=''
for i in dna_seq:
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
rna_seq=''
for i in dna_seq:
    if i=="T":
        rna_seq=rna_seq+"U"
    else:
        rna_seq=rna_seq+i
print("RNA sequence is:",rna_seq) 

proteinseq1= gen1(dna_seq)
print("Protein sequence of gen1:",proteinseq1)
print("Open Reading Frames are:\n",orf(dna_seq))

codons={"TTT":"F","TTC":"F","TTA":"L","TTG":"L","TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
"CTT":"L","CTC":"L","CTA":"L","CTG":"L","CAT":"H","CAC":"H","CAA":"Q","CAG":"Q","ATT":"I",
"ATC":"I","ATA":"I","ATG":"M","AAT":"N","AAC":"N","AAA":"K","AAG":"K","GTT":"V","GTC":"V","GTA":"V",
"GTG":"V","GAT":"D","GAC":"D","GAA":"E","GAG":"E","GGG":"G","GGA":"G","GGC":"G","GGT":"G","GCG":"A",
"GCA":"A","GCC":"A","GCT":"A","AGG":"R","AGA":"R","AGC":"S","AGT":"S","ACG":"T","ACA":"T","ACC":"T","ACT":"T",
"CGG":"R","CGA":"R","CGC":"R","CGT":"R","CCG":"P","CCA":"P","CCC":"P","CCT":"P","TGG":"W","TGA":"*","TGC":"C","TGT":"C",
"TCG":"S","TCA":"S","TCC":"S","TCT":"S"}
dnaseq="ATGGCCGCT"
def hello(dna,codons):
    protein=""
    for x in range(0,len(dna),3):
        code=dna[x:x+3]
        protein +=codons[code]
    return protein

print(hello(dnaseq,codons))


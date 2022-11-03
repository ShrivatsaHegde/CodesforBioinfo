f=open("C:\python 2nd sem\RV3802C.txt","r")
DNAsequence=f.read()
DNAsequence=DNAsequence.lower()
RNAsequence=""
for x in DNAsequence:
 if x=="t":
     RNAsequence=RNAsequence+"u"
 else:
     RNAsequence=RNAsequence+x
     print(RNAsequence)

f=open("RV3802C.txt","r")
DNAseq=f.read()
exons=[1,40,50,60,80,100]
start=0
end=1
DNAexons=""
DNAintrons=""
def count(number):
   find=0  
   for x in number:
    find=find +1 
   return find
print(count(exons))
while(end<count(exons)):
    print("\n",exons[start],"\t",exons[end])
    DNAexons=DNAexons+DNAseq[exons[start]-1:exons[end]]
    start=start+2
    end=end+2
    print(DNAexons)
    
    RNAseq=""
    for i in DNAexons:
        if i=="T":
           RNAseq=RNAseq+"U"
        else:
           RNAseq=RNAseq+i

    print("\n",RNAseq)  

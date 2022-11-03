DNAseq="atgcatgc"
DNAseq=DNAseq.upper()
exons=[1,3,5,7]
#this is the input to splice the DNAseq ...you can give any number which is present in the data
start=0
end=1
#here this the index number of the exons variable at 0 index 1 is present and 1st position or index 3 is present
DNAseq_exons=""
while(end<len(exons)):
    print("/n",exons[start],"/t",exons[end])
    #here we are printing what is present at 0th position to 3rd position of exons variable
    print(DNAseq_exons[exons[start]-1:exons[end]])
     #here we are just printing the DNA sequence from one step behind why because here irs only printing from one positon to 2nd position 3rd position data is cut
     #  so we need that 3rd position data so we are going one position back and printing the output.
    DNAseq_exons=DNAseq_exons+DNAseq[exons[start]-1:exons[end]]
     #here we are storing the spliced data into a variable
     #then we can not stop here we need to proceed with the loop and completely read the whole data so we are just changing the statrting point of the loop thats it .
     #here so if we just push the position value of start by 2 we will have the next position of exons variable.
    start=start+2
     #if we do 0+2=2 so it moves to the 2nd position of the exons variable where the value present is 5
    end=end+2
     #so here we are adding 1+2=3 so in index of exons the 3rd value is 7 so it takes up this value.we add 2 beacuse we considered 2 position first so we need to add 2
    print(DNAseq_exons)
     #after all this we need to chnage t with u for RNA seq so this is the program
    RNAseq=""
    for x in DNAseq_exons:
        if x=="T":
         RNAseq=RNAseq+"U"
        else:
         RNAseq=RNAseq+x
    print(RNAseq)    

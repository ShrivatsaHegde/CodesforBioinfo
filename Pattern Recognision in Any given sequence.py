pattern="GAATTCC"
seq=""
with open("C:\python 2nd sem\RV3802C.txt")as fh:
    fh.readline()
for i in fh:
    seq=i.strip()

site=re.compile(pattern)
result=site.search(seq)
pat_found=result.group()
spansite=result.span()


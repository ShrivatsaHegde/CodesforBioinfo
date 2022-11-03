import re
pattern="TTGCCTACACGGCCCAATTCCACAATCCGCT"
seq=""
with open("C:\python 2nd sem\RV3802C.txt")as fh:
    fh.readline()
    for i in fh:
        seq+=i.strip()
print(seq)
site=re.compile(pattern)
result= site.search(seq)
pat_found=result.group()
spansite=result.span()

print("restriction site found:",result)
print("RESTRICTION SITE PATTERN",pat)
print("RESTRICTION SITE LOCATION",spansite)
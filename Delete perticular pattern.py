import re
regex = re.compile("(?:GC){3,}")
seq = 'ATGATCGTACTGCGCGCTTCATGTGATGCGCGCGCGCAGACTATAAG'
print('Before: {0}'.format(seq))
print('After: {0}'.format(regex.sub('* 3 gc *', seq)))
#print('After: {0}'.format(regex.sub('', seq,1))) # total 2
#print('After: {0}'.format(regex.subn('', seq))) # total 2

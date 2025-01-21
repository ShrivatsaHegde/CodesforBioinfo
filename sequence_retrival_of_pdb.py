""" code for retrival of protein sequences from pdb files using MODELLER."""
from modeller import * # Load standard Modeller classes

code = 'qpdb'

e = Environ() # create a new MODELLER environment to build this model in
m = Model(e, file=code)
aln = Alignment(e)# Get the sequence of the  PDB file, and write to an alignment file
aln.append_model(m, align_codes=code)
aln.write(file=code+'.seq')
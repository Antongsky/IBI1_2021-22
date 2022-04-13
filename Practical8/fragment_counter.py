# Restriction fragment length counter
seq ='ATGCAATCGACTACGATCAATCGAGGGCC'
splited_seq=seq.split('GAATTC')  #Now the sequence is cut.
print(splited_seq) 
print(len(splited_seq)) #len(splited_seq)=1,showing EcoRI can't cut it. Piece=1.

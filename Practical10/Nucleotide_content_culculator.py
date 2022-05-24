#Create the function
def count(gene_sequence):
    A=0
    T=0
    C=0
    G=0
    error=False
    for i in range(0,len(gene_sequence)):
        if gene_sequence[i] in "Aa":
            A+=1
        elif gene_sequence[i] in "Tt":
            T+=1
        elif gene_sequence[i] in "Cc":
            C+=1
        elif gene_sequence[i] in "Gg":
            G+=1
        else: 
            error=True
            break
    if error==True:
        return "Sequence error!"
    else:
        A=A/len(gene_sequence)
        T=T/len(gene_sequence)
        C=C/len(gene_sequence)
        G=G/len(gene_sequence)
        return "The percentage of \nA is %f\nT is %f\nC is %f\nG is %f." %(A,T,C,G)

#Use the function
sequence="AATTCGAatcgc"
print(count(sequence))   #Test the function, sequence without error.
#Outcome: A is 0.333333 T is 0.250000 C is 0.250000 G is 0.166667.
sequence="AAGTcJK"
print(count(sequence))   #Test the function, sequence with error.
#Outcome: Sequence error!
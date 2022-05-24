import re

gene=open(r"Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
print(gene.readline()) #Trying to open the file and read the first line.


gene=gene.read()   # Now,"gene" is a gene sequence.
splitted_gene=gene.split('>')    #Using split method to split it. Each gene is stored in Python list.
cuttable_gene=[]
for i in range (0,len(splitted_gene)):
    if 'GAATTC' in splitted_gene[i]:
        cuttable_gene.append(splitted_gene[i])  # If these gene can be cut, they will be stored in another list "cuttable_gene".

new_data=[]
a=input("Please input the file name:")
cut_genes=open("D:\\IBI-githubspace\\IBI1_2021-22\\Practical8\\%s.fa" %(a),'w') #creat a new file to store the data
for i in range (0,len(cuttable_gene)):
    new_data=re.findall(r'(.+?)_.+](.+)',cuttable_gene[i],re.S)  
    seq=re.sub(r'\n','',new_data[0][1])
    splitted_seq=seq.split('GAATTC')  #Now the sequence is cut. The piece generated is len(splitted_seq).
    cut_genes.write(">"+new_data[0][0]+"_"+str(len(splitted_seq))+"_"+seq)
    cut_genes.write("\n")
    
    
cut_genes.close()
import re

gene=open(r"D:\IBI-githubspace\IBI1_2021-22\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
print(gene.readline()) #Trying to open the file and read the first line.


gene=gene.read()   # Now,"gene" is a gene sequence.
splitted_gene=gene.split('>')    #Using split method to split it. Each gene is stored in Python list.
cuttable_gene=[]
for i in range (0,len(splitted_gene)):
    if 'GAATTC' in splitted_gene[i]:
        cuttable_gene.append(splitted_gene[i])  # If these gene can be cut, they will be stored in another list "cuttable_gene".

new_data=[]
cut_genes=open(r"D:\IBI-githubspace\IBI1_2021-22\Practical8\cut_genes.fa",'w') #creat a new file to store the data
for i in range (0,len(cuttable_gene)):
    new_data=re.findall(r'(.+?)_.+](.+)',cuttable_gene[i],re.S)          #fine the gene name and the sequence and store them in "new_data". 
    cut_genes.write(">"+new_data[0][0]+"     "+str(len(new_data[0][1]))+new_data[0][1]) #Extract data from new_data and write into the file.
    print(new_data[0][0]+" stored!")
    
cut_genes.close()
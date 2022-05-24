import re
import pandas as pd
raw_seq1=open("DLX5_human.fa","r")
raw_seq2=open("DLX5_mouse.fa","r")
raw_seq3=open("RandomSeq.fa","r")
BLOSUM=pd.read_excel("BLOSUM.xlsx")

seq1=re.findall(r"\n(.+)",raw_seq1.read())[0]
seq2=re.findall(r"\n(.+)",raw_seq2.read())[0]
seq3=re.findall(r"\n(.+)",raw_seq3.read())[0]

def alignment_score(seq1,seq2):
    global BLOSUM
    score=0
    for i in range (0,len(seq1)):
        for j in range(0,21):
            if BLOSUM.iloc[j,0]==seq1[i]:
                score+=BLOSUM.loc[j,seq2[i]]
    return score

print(alignment_score(seq1, seq2))
print(alignment_score(seq2, seq3))
print(alignment_score(seq1, seq3))


def similarity_score(seq1,seq2):
    score=0
    for i in range (0,len(seq1)):
        if seq1[i]!=seq2[i]:
            score+=1
    return score

print((len(seq1)-similarity_score(seq1, seq2))/len(seq1))
print((len(seq1)-similarity_score(seq2, seq3))/len(seq1))
print((len(seq1)-similarity_score(seq1, seq3))/len(seq1))


    

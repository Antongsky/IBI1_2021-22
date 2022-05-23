from xml.dom.minidom import parse as xml_parse
import matplotlib.pyplot as plt
import numpy as np

document=xml_parse("go_obo.xml")
root=document.documentElement
term=root.getElementsByTagName("term")
len_term=len(term)
print(len_term) #Now, the number of terms is printed. =47340



id_list=[]
for i in range (0,len_term):
    id_value=term.item(i).getElementsByTagName("id")[0].childNodes[0]
    id_list.append(id_value.data)
       


def father_nodes(node,term,id_list,node_record_list):
    global uper_nodes_number_list
    sub_node_list=node.getElementsByTagName("is_a")
    if sub_node_list!=None:
        for i in range (0,len(sub_node_list)):
            j = id_list.index(sub_node_list[i].childNodes[0].data)
            if j <= len(uper_nodes_number_list)-1:
                node_record_list.extend(uper_nodes_number_list[j])
            else:
                node_record_list.append(j)
                node=term.item(j)
                node_record_list = father_nodes(node,term,id_list,node_record_list)
    return node_record_list

uper_nodes_number_list=[]
child_node_list1=[-1]*len_term
child_node_list2=[]

for i in range(0,len_term):
    node_record_list=[i]
    node=term.item(i)
    cleaned_node_record_list=list(set(father_nodes(node, term, id_list,node_record_list)))
    print("Procedure "+str(100*i/len_term)+" %.")
    uper_nodes_number_list.append(cleaned_node_record_list)
    for j in range (0,len(uper_nodes_number_list[i])):
        
        child_node_list1[uper_nodes_number_list[i][j]]+=1
        

for i in range(0,len(term)):
    node=term.item(i)
    def_node=node.getElementsByTagName("def").item(0)
    def_str_text=def_node.getElementsByTagName("defstr")[0].childNodes[0].data
    if "translation" in def_str_text:
        child_node_list2.append(child_node_list1[i])

    
        
plt.figure(figsize=(4,20))
plt.subplot(2,1,1)
plt.boxplot(child_node_list1)
plt.title("Distribution of the number of childnodes in each term")
plt.ylabel("Number of child nodes")


plt.subplot(2,1,2)
plt.boxplot(child_node_list2)
plt.title("Distribution of the number of childnodes in each term with gene expression")
plt.ylabel("Number of child nodes")

plt.tight_layout()

if np.average(np.array(child_node_list1))>np.average(np.array(child_node_list2)):
    print("Translated terms has a smaller number of childnodes.")
else:
    print("Translated terms has a bigger number of childnodes.")
# Translated terms has a bigger number of childnodes on average.



      
    
        

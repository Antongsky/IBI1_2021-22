from xml.dom.minidom import parse as xml_parse
import matplotlib.pyplot as plt
import numpy as np

document=xml_parse("go_obo.xml")
root=document.documentElement
term=root.getElementsByTagName("term")
print(len(term)) #Now, the number of terms is printed. =47340


id_list=[]
for i in range (0,len(term)):
    id_value=term.item(i).getElementsByTagName("id")[0].childNodes[0]
    id_list.append(id_value.data)
       


def child_nodes(node,term,id_list,count_base=0):
    global nodes_number_list1
    sub_node_list=node.getElementsByTagName("is_a")
    if sub_node_list!=None:
        count_base=count_base+len(sub_node_list)
        print(count_base)
        for i in range (0,len(sub_node_list)):
            j = id_list.index(sub_node_list[i].childNodes[0].data)
            if j <= len(nodes_number_list1)-1:
                count_base = count_base + nodes_number_list1[j] + 1
            else:
                node=term.item(j)
                count_base = child_nodes(node,term,id_list,count_base)
    return count_base
            
nodes_number_list1=[]
nodes_number_list2=[]
for i in range(0,len(term)):
    node=term.item(i)
    def_node=node.getElementsByTagName("def").item(0)
    def_str_text=def_node.getElementsByTagName("defstr")[0].childNodes[0].data
    sub_node_number=child_nodes(node, term, id_list)
    if "translation" in def_str_text:
        nodes_number_list2.append(sub_node_number)
    nodes_number_list1.append(sub_node_number)
    

plt.figure(figsize=(4,20))
plt.subplot(2,1,1)
plt.boxplot(nodes_number_list1)
plt.title("Distribution of the number of childnodes in each term")
plt.ylabel("Number of child nodes")


plt.subplot(2,1,2)
plt.boxplot(nodes_number_list2)
plt.title("Distribution of the number of childnodes in each term with gene expression")
plt.ylabel("Number of child nodes")

plt.tight_layout()

if np.average(np.array(nodes_number_list1))>np.average(np.array(nodes_number_list2)):
    print("Translated terms has a smaller number of childnodes.")
else:
    print("Translated terms has a bigger number of childnodes.")
# Translated terms has a bigger number of childnodes on average.



      
    
        

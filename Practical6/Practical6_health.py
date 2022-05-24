import numpy as np
import matplotlib.pyplot as plt

# create the dictionary "dic"
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]   #firstly import the original data
dic={}      #assign an empty dic
i=0
for i in range (0,10):    #I use for loop to assign each value to the according key.
    dic.update({paternal_age[i]:chd[i]})
    i=i+1
print(dic)  #now, dic is created.

#look for values(chd) by checking keys(peternal_age)
print(dic[30])   # Here,"30"can be modified into other keys.

#construct a scattered plot
plt.scatter(paternal_age,chd)
plt.title("The relationshoip of offspring CHD relative risk with paternal age.")
plt.xlabel("paternal age")
plt.ylabel("offspring CHD relative risk")
plt.show()




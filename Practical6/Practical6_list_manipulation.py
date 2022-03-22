import numpy as np
import matplotlib.pyplot as plt

#import data
marks=[45,36,86,57,53,92,65,45]
#print sorted marks
print(sorted(marks))
#create a boxplot
plt.boxplot(marks)
plt.show()
#check whether pass
np_marks=np.array(marks)
avg=np.average(np_marks)
print(avg)
if avg<60:
    print("score %f didn't pass" %(avg))
else:
    print("score %f passed!" %(avg))
    
    

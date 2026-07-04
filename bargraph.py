import matplotlib.pyplot as plt
import numpy as np

"""x=np.array(["a","b","c","d"])
y=np.array([4,6,3,10])
plt.bar(x,y,width=0.1)
#plt.barh(x,y,color="green")
plt.show()"""

#histograms
"""x=np.random.normal(170,10,250)#np.random.normal(mean,standard devation,size)
plt.hist(x)
plt.show()"""

#picharts

x=np.array((20,30,40,10))
lables=(["cherries","strawberries","apples","bananas"])
exp=[0.2,0,0,0]
plt.pie(x,labels=lables,startangle=90,explode=exp,shadow=True)
plt.legend(title="fruts")
plt.show()
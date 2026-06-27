import matplotlib.pyplot as plt
import numpy as np

x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors=np.array([0,10,20,30,35,40,50,60,65,70,80,90,100])
sizes=np.array([256,652,972,870,792,693,502,837,793,518,201,490,542])
plt.scatter(x,y,c=colors,cmap="CMRmap",s=sizes,alpha=0.5)
plt.colorbar()

"""x=np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y=np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x,y)"""
plt.show()



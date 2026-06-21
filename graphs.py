import matplotlib.pyplot as plt
import numpy as np

#x=np.array([1,8])
#y=np.array([3,10])
#line plot
#plt.plot(x,y)
#plt.plot(x,y,"o")

x=np.array([1,4,7,9])
y=np.array([4,8,2,0])
font={"family":"arial","color":"pink","size":20}
#plt.plot(y,marker="D")
#plt.plot(y,"o:g")
plt.subplot(2,1,1)
plt.plot(x,y)
x=np.array([3,6,2,7])
y=np.array([6,2,8,4])
plt.subplot(2,1,2)
plt.plot(x,y)
plt.suptitle("kfc")
"""plt.plot(x)
plt.plot(y,ls="dashed",lw=2,color="m",marker="*",ms=10,mec="r",mfc="g")
plt.xlabel("people",fontdict=font)
plt.ylabel("animals")
plt.title("creatures",loc="left")
plt.grid(color="pink",linestyle="--",linewidth=0.5)"""
plt.show()

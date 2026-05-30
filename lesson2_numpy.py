import numpy as np
#get a random numpy array of a specefied dimention inbetween 0 and 1
num=np.random.rand(2,3)
print(num)

#reshape lenier array
arr=np.arange(1,10).reshape(3,3)
print(arr)

arr2=np.arange(1,37).reshape(3,12)
print(arr2)

arr3=np.random.permutation(np.arange(1,10))
print(np.sort(arr3))

#creating an array of 0s
zero=np.ones((5,2,3),dtype="int32")
print(zero.shape)

#creating array of another number
nums=np.full((2,2),3)
print(nums)

#another variation
nums2=np.arange(1,10).reshape(3,3)
print(np.full_like(nums2,6))

print(np.random.randint(-4,8,size=(3,3)))

#identity matrix
print(np.identity(6))

#repeat an array
arr5=np.array([[2,5,3]])
arr4=np.repeat(arr5,3,axis=1)
print(arr4)
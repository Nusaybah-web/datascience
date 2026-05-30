import numpy as np
import sys

l=[2,4,1,3,5]

array=np.array(l,dtype="S")

print(array)
print(l)

listsize=sys.getsizeof(l)
arrsize=sys.getsizeof(array)
print("size of array: ", array.nbytes)
print(listsize)
print(arrsize)

#0-D array
arr=np.array(42)
#1-D array
arr1=np.array([12,53,24])
#2-D array
arr2=np.array([[29,39,12],[32,24,52]])

print(arr2)

#3-D array
arr3=np.array([[[12,42,64],[47,52,14]],[[13,14,19],[19,23,53]]])

print(arr3)

#check number of dimensions

print(arr3.ndim)

#define number of dimensions
arr5=np.array([1,2,3,4],ndmin=5)
print(arr5)

#performin mathematical calculations

print(array[2]+array[3])

print(arr2[0,2])
print(arr2[1,1])
print(arr3[-2,-1,-2])

#slicing 2-D arrays

arr2=np.array([[29,39,12],[32,24,52]],dtype="f")

print(arr2[0,1:])
print(arr2[:1,:1])

print(arr2.dtype)

ar=np.array(["hello","good","morning"])
print(ar.dtype)

print(array.dtype)

#shape
print(arr2.shape)
print(arr2.size)

#getting an array of numbers from one to 100
num=np.arange(0,100,2)
print(num)

#get a random arrangement of numbers
rand=np.random.permutation(np.arange(1,100))
print(rand)

#get a random number using numpy
randnum=np.random.randint(1,1000)
print(randnum)
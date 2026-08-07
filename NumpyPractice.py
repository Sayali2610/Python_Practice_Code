#Numpy array
import  numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(a+b)
print("\n")

#One dimensional arry
arr = np.array([10,20,30])
print(arr)
print("\n")

#Two dimensional array
arr = np.array([[1,2,3],
                [4,5,6]])
print(arr)
print("\n")

#Three Dimensional array
arr = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print(arr)
print("\n")

#Check number of dimensions and shape and size
arr = np.array([[1,2],[3,4]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print("\n")

#Create Special arrays
arr = np.zeros((2,3))
print(arr)
arr = np.ones((2,2))
print(arr)
arr = np.eye(3)
print(arr)
print("\n")


#Range of number
arr = np.arange(1,11)
print(arr)
arr = np.arange(2,21,2)
print(arr)
print("\n")

#Equally spaced numbers
arr = np.linspace(1,10,5)
print(arr)
print("\n")

#Indexing
arr = np.array([10,20,30,40])
print(arr[0])
print(arr[2])
print(arr[-1])
print("\n")

#Slicing
print(arr[1:4])
print("\n")

#2D Indexing
arr = np.array([
    [10,20],[30,40]
])
print(arr[1,0])
print("\n")

#Mathematical Operations
a = np.array([10,20,30])
print(a+5)
print(a+a)
print(a*2)
print(a/2)
print("\n")

#Aggregate Function
arr = np.array([10,20,30,40])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))
print("\n")

#Reshape Array
arr = np.arange(1,7)
print(arr.reshape(2,3))
print("\n")

#Flatten Array
arr = np.array([[1,2],[3,4]])
print(arr.flatten())
print("\n")

#Random Number
arr = np.random.randint(1,100,5)
print(arr)
print("\n")

#Copy vs View
a = np.array([1,2,3])
b = a.copy()

b[0]=100

print(a)
print(b)
print("\n")

#View
a=np.array([1,2,3])
b = a.view()

b[0]= 100
print(a)
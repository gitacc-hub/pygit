import numpy as np
#array=np.array([1,2,3])
#To check the version
"""print(np.__version__)"""
#To find its type
"""print(type(array))"""

#Check Number of dimension
"""a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)"""

#Higher Dimensional Arrays
#---When the array is created,
# you can define the number of dimensions by using the ndmin argument.
"""arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)"""

#Get the Shape of an Array
"""arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)"""

"""arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print("Shape of array: ",arr.shape)
"""
#Multidimensional Indexing
"""array=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array[1,0,2])"""

#String Concatenation
"""array = np.array([
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]
])
word=array[0,0,1]+array[0,0,0]+array[0,1,0]
print(word)"""

#Slicing
array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
#Add numbers in an index

print(array[1,1]+array[3,3])
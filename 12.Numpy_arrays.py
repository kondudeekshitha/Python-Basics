import numpy as np
#creating an array with numpy
#1D array
A1D=np.array([1,2,3,4,5])
print(A1D)

#2D array
A2D= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A2D)

#basic array information methods
print(A1D.ndim)
print(A2D.ndim)

#shape
print(A2D.shape)
print(A1D.shape)

#size
print(A1D.size)
print(A2D.size)

#dtype
print(A1D.dtype)
print(A2D.dtype)

#creating an array with numpy
#zeros:
print(np.zeros(12))

#ones
print(np.ones(12))

#arange
print(np.arange(1,11,1))
print(np.arange(0,11,2))
print(np.arange(1,11,2))

#linspace
print(np.linspace(0,1,3))
print(np.linspace(1,5,100))

#mathematical operations
A=np.array([1,2,3,4,5])
L=[1,2,3,4,5]
print(A+6)
print(A-6)
print(A*2)
print(A/2)
print(A//2)
print(A**2)

#aggregate functions
A=np.array([1,2,3,4,5])
#sum
print(np.sum(A))

#mean
print(np.mean(A))

#max&min
print(np.max(A))
print(np.min(A))

#median
print(np.median(A))

#std
print(np.std(A))

#cumulative product
print(np.cumprod(A))

#MATRIX OPERATIONS
mat1= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat1)

mat2=np.array([[9,8,7],[6,5,4,],[3,2,1]])
print(mat2)

print(mat1+mat2)
print(mat1**2)
print(mat1*mat2)
print(mat1/mat2)
print(mat1//mat2)
print(mat1&mat2)
print(np.dot(mat1,mat2)) #product
print(np.transpose(mat1))
import numpy as np

#Zad 1
# A = np.array([3, 5, 7, 9])
# B = np.array([2, 4, 6, 8])
# C = np.divide(A,B)
# print(C)

#Zad 2
# X = np.array([[1, 2, 3], [4, 5, 6]])
# skalar = 3
# tab = X+skalar
# print(tab)

#Zad 3
# C = np.array([10, 20, 30, 40])
# D = np.array([1, 2, 3])
# tab = np.subtract(D,C)
# print(tab)

#Zad 4
# M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# v = np.array([10, 20, 30])
# tab = np.add(M,v)
# print(tab)

#Zad 5
# Z = np.zeros((3, 4))
# ones = np.ones(4)
# tab = np.add(Z, ones)
# print(tab)

#Zad 6
# A = np.array([[1, 2, 3], [4, 5, 6]])
# B = np.array([10, 20])
# B = B[:, np.newaxis]
# # B = B.reshape(2,1)
# tab = A*B
# print(tab)

#Zad 7
# temps = np.array([0, 10, 20, 30, 40])
# F=temps * (9/5) + 32
# print(F)

#Zad 8
# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# tab = np.sqrt(data)
# print(tab)

#Zad 9
# pi = np.pi
# angles = np.array([0, pi/6, pi/4, pi/3, pi/2])
# print(np.sin(angles))
# print()
# print(np.cos(angles))
# print()
# print(np.tan(angles))

#Zad 10
# A = np.array([[1, 2], [3, 4]])
# B = np.array([5, 6])
# tab = A%B
# print(tab)

#Zad 11
# X = np.array([[2, 5, 8], [1, 3, 7], [4, 6, 9]])
# Y = np.array([1, 2, 3])
# tab = np.maximum(X,Y)
# print(tab)

#Zad 12
# values = np.array([-3, -2, -1, 0, 1, 2, 3])
# print(np.abs(values))

#Zad 13
# A = np.array([[1, 2, 3], [4, 5, 6]],dtype=np.uint64)
# B = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.uint64)
# print(B**A)

#Zad 14
# probabilities = np.array([0.1, 0.01, 0.001, 0.0001])
# print(np.log(probabilities))
# print(np.log10(probabilities))

#Zad 15
M = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([[10], [20]])
print(M+v)

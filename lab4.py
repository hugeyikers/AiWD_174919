import numpy as np

## Zad 1
# arr = np.array(["python", "NumPy", "data science", "machine learning"])
# print(np.strings.upper(arr))

## Zad 2
# arr = np.array(["PYTHON", "NUMPY", "DATA SCIENCE"])
# print(np.strings.lower(arr))
# print(np.strings.title(arr))

## Zad 3
# arr1 = np.array(["machine", "deep"])
# arr2 = np.array(["learning", "networks"])
# arr3 = np.strings.add(arr1, arr2)
# print(arr3)
# print(np.strings.replace(arr3, ["el", "pn"], ["e l", "p n"]))

## Zad 4
# arr = np.array(["python.data.science", "machine.learning"])
# print(np.char.split(arr, sep="."))

## Zad 5
# arr = np.array([" python ", " numpy ", " pandas "])
# print(np.strings.strip(arr))

## Zad 6
# a = np.array([2, 4, 6])
# b = np.array([1, 3, 5])
# print(np.dot(a,b))
# print(a@b)

## Zad 7
# A = np.array([[2, 3], [1, 4]])
# B = np.array([[5, 1], [2, 6]])
# print(np.matmul(A,B))
# #print(A@B)

## Zad 8
# A = np.array([[4, 2], [3, 5]])
# b = np.array([8, 7])
# print(np.linalg.solve(A,b))

## Zad 9
# M = np.array([[6, 2], [3, 9]])
# print(np.linalg.det(M))
# print(np.linalg.inv(M))
# #print(np.dot(M, np.linalg.inv(M)))
# #print(M@np.linalg.inv(M))

## Zad 10
# v1 = np.array([1, 2, 3])
# v2 = np.array([4, 5, 6])
# v3 = np.outer(v1, v2)
# eigenvals, eigenvecs = np.linalg.eig(v3)
# print(eigenvals)
# print(eigenvecs)

## Zad 11
# arr = np.array([[0, 5, 0], [2, 0, 3], [0, 0, 7]])
# indeksy = np.nonzero(arr)
# print(indeksy)
# wartosci = arr[indeksy]
# print(wartosci)

## Zad 12
# data = np.array([-3, 4, -1, 6, -8, 2])
# data2 = np.where(data < 0, -99, data)
# print(data2)

## Zad 13
# indices = np.array([2, 0, 1, 2, 0])
# options = [np.array([10, 20, 30, 40, 50]),np.array([60, 70, 80, 90, 100]), np.array([110, 120, 130, 140, 150])]
# tab = np.choose(indices, options)
# print(tab)

## Zad 14
# matrix = np.array([[5, 12, 8], [3, 7, 9], [15, 4, 2]])
# warunki = [matrix < 5, (matrix >= 5) & (matrix <= 10), matrix > 10]
# opcje = [0, 50, 100]
# tab = np.select(warunki,opcje)
# print(tab)

## Zad 15
values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np.putmask(values, values%2 == 0, 0)
print(values)
indeksy = [0, 4, 8]
np.put(values, indeksy, [100, 200, 300])
print(values)

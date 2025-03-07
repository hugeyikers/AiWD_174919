import numpy as np

# Zad 1
# tablica = np.arange(0,21,2)
# print(tablica)

# Zad 2
# macierz = np.arange(1,17).reshape(4,4)
# # macierz = np.array([np.arange(1,5), np.arange(5,9)...])
# print(macierz.ndim, macierz.shape)
# print(macierz)

# Zad 3
# macierz = np.arange(1,26).reshape(5,5)
# max = np.max(macierz)
# min = np.min(macierz)
# print(macierz)
# print(min, max)

# Zad 4
# tablica = np.linspace(0,1,10)
# print(tablica)

# Zad 5
# macierz_jednostkowa = np.eye(3)
# print(macierz_jednostkowa)

# Zad 6
# tablica = np.arange(1,13).reshape(3,4)
# print(tablica)
# tablica_2x6 = tablica.reshape(2,6)
# print(tablica_2x6)

# Zad 7
# tab1 = np.arange(1,6)
# tab2 = np.arange(6,11)
# tab3 = np.concatenate((tab1,tab2))
# print(tab3)

# Zad 8
# tab = np.zeros([3,3])
# np.fill_diagonal(tab,1)
# print(tab)

# Zad 9
# tab = np.arange(0,100).reshape(10,10)
# srodek = tab[2:7, 2:7]
# print(srodek)

# Zad 10
# tab = np.array([5, 2, 8, 1, 9, 3, 7, 4, 6, 0])
# tab = (tab-tab.min())/(tab.max()-tab.min())
# print(tab)


# Zad 11
# wektor = np.array([1, 2, 3, 4, 5])
# macierz = np.array([[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]])
# print(wektor+macierz)

# Zad 12
# tab = np.arange(1,17).reshape(4,4)
# transponowanie = np.transpose(tab)
# #print(tab.T)
# print(tab)
# print(transponowanie)

# Zad 13
# pierwsza = np.arange(1,7).reshape(2,3)
# druga = np.arange(1,13).reshape(3,4)
# print(pierwsza@druga)

# Zad 14
# tab = np.arange(1,101).reshape(10,10)
# sum_col = tab.sum(axis=0)
# sum_row = tab.sum(axis=1)

# Zad 15
# tab = np.array([3, 8, 2, 5, 1, 4, 9, 7, 6, 0])
# tab[tab < tab.mean()]=0
# print(tab)

# Zad 16
# wektor = np.array([10,20,30])
# macierz = np.array([[1], [2], [3], [4]])
# tab = wektor+macierz
# print(tab)

# Zad 17
# macierz = np.array([8, 3, 9, 5, 1, 7, 2, 0, 6, 4, 15, 13, 19, 12,
# 11, 17, 14, 10, 16, 18, 25, 21, 23, 20, 22]).reshape(5,5)
# posortowana = np.sort(macierz, axis=1)
# print(posortowana)

# Zad 18
# tablica = np.zeros((2, 3, 4))
# print(tablica)
# print(tablica.ndim, tablica.size)

# Zad 19
# tab1 = np.array([[2],[4],[6]]).reshape(3,1)
# tab2 = np.array([[1, 3, 5, 7]]).reshape(1,4)
# tab3 = (tab1@tab2).reshape(3,4)
# print(tab3)

# Zad 20
tab = np.arange(1,37).reshape(6,6)
tab2 = tab.reshape(3,4,3)
print(np.mean(tab2, axis=0))
print()
print(np.mean(tab2, axis=1))
print()
print(np.mean(tab2, axis=2))
